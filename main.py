import os
import sys
from dotenv import load_dotenv
from google import genai

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
    model='gemini-2.0-flash-001', contents=prompt
)
usage = response.usage_metadata
if "--verbose" in flags:
    print(f"User prompt: {response.text}")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")