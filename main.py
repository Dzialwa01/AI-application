import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# if not api_key:
#     raise ValueError("Open api key not found from env file")

def get_response(prompt):
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model = "gpt-4o-mini",  # The AI model we are using
        max_completion_tokens = 500, # Limits the answer given by AI
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

response = get_response("What are the different roles in openai api that we can assign, explain pointwise")

print(response)

# Exercise 1
# Changing the prompt
prompt1 = "Explain MERN stack"
prompt2 = "What is REST API?"

print(get_response(prompt2))


# 4. System vs user message

def get_response(sys_prompt, user_prompt):
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model = "gpt-4o-mini",  # The AI model we are using
        max_completion_tokens = 500, # Limits the answer given by AI
        messages = [{"role": "user", "content": user_prompt},
                    {"role": "system", "content": sys_prompt}]
    )
    return response.choices[0].message.content

sys_prompt= "You are a programming teacher. Explain concepts simply with examples"
user_prompt = "Explain JavaScript closures"
print(get_response(sys_prompt, user_prompt))


# 5. Using System Prompts to Guide AI Behaviour - This is used to guide the AI on how it needs to answer the question.


## Example: Bullet-Point Answers Only

sys_prompt = "Answer only in bullet points. keep it short."
user_prompt = " Explain OOP concepts"
print(get_response(sys_prompt, user_prompt))

## Example : Code reviewer Bot
sys_prompt = "You are a code reviewer. Point out mistakes and suggest improvement politely"
user_prompt = "def add(a,b): return a+b"
print(get_response(sys_prompt, user_prompt))


# 6. Understanding tokens (with code)
user_prompt = "Explain tokens in LLMs brieflt using bullet points"
sys_prompt = "You are an AI trainer and explain things simply"
print(get_response(sys_prompt, user_prompt))



# 7. Mini project (Perfect for Assignment)
# Build a Teaching Bot

client = OpenAI (api_key = api_key) # creating an instance of the OpenAI library. Line is basically creating a connection to the OpenAI's server using the API key.

while True:
    user_input = input("\nAsk a question (or tyoe 'exit'): ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are a helpful programming teacher. Explain simply with examples."},
            {"role": "user", "content": user_input}
        ]
    )
    print("\nAnswer:")
    print(response.choices[0].message.content)