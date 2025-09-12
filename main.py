import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
genai.types.GenerateContentResponseDict
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
)
usage = response.usage_metadata
print(response.text)
print(f"Prompt tokens: {usage.prompt_token_count}")
print(f"Response tokens: {usage.candidates_token_count}")