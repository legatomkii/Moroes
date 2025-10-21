import os
import sys
from dotenv import load_dotenv
from google import genai
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = genai.types.Tool(
    function_declarations=[
        schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
    ]
)

load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")
if len(sys.argv) < 2:
    print("Error: prompt is required")
    sys.exit(1)    
prompt = sys.argv[1] 
flags = sys.argv

client = genai.Client(api_key=api_key)
genai.types.GenerateContentResponseDict
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=[prompt], config=genai.types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
)
usage = response.usage_metadata
# if "--verbose" in flags:
if len(response.function_calls) == 0:
    print(f"User prompt: {response.text}")
else:
    print(f"Calling function:{response.function_calls[0].name}{response.function_calls[0].args}")
print(f"Prompt tokens: {usage.prompt_token_count}")
print(f"Response tokens: {usage.candidates_token_count}")