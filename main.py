import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

if not api_key:
    raise ValueError("Open api key not found from env file")

def get_response(prompt):
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model = "gpt-4o-mini",  # The AI model we are using
        max_completion_tokens = 100, # Limits the answer given by AI
        messages = [{"role":"user", "content": prompt}]
    )
    return response.choices[0].message.content

response = get_response("What are the different roles in openai api that we can assign, explain pointwise")

print(response)