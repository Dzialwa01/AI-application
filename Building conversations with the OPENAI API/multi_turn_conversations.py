# Dzialwa Nemakonde 
# 04 March 2026

# Practice and exercises using multi-turn conversations

### 📝 Practice Task 

# Build a chatbot that:

# - introduces itself
# - answers a Python question
# - summarizes its own previous answer

# 💡 Hint:

# - use a `messages` list
# - append both user and assistant messages

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found in env file")

client  = OpenAI(api_key = api_key)

user_qs = ["Introduce yourself as Python Master Tutor AI who helps you master python", "What is a list", "What is a tuple", "Explain the difference between mutable and immutable"]

messages = [
            {"role": "system", "content": "You are python tutor who explains python concepts briefly using bullet points and you always summarise the previous answer"},
            {"role": "assistant", "content": "A variable is a container that stores any data type. e.g temp = 40"}]


for prompt in user_qs:

    user_message = {"role": "user", "content": prompt}
    messages.append(user_message)

    response = client.chat.completions.create(

        model = "gpt-4o-mini",

        messages = messages
    )


    ans = response.choices[0].message.content

    assist_ans = {"role": "assistant", "content": ans}
    messages.append(assist_ans)

    print(prompt)
    print(ans)


# ************************************************************************************
# **Creating a conversation history** ( PROOF OF CONCEPT)

# An online math learning platform called *Easy as Pi* has contracted you to help them develop an AI tutor. You immediately see that you can build this application by utilizing the OpenAI API, and start to design a simple proof-of-concept (POC) for the major stakeholders at the company to review.

# To start, you'll demonstrate how responses to student messages can be stored in a message history, which will enable full conversations.

# • Send messages to the model in a chat request.
# • Extract the assistant message from response, convert it to a message dictionary, and append it to messages.

messages = [
    {"role": "system", "content": "You are a helpful math tutor that speaks concisely."},
    {"role": "user", "content": "Explain what pi is."}
]

# Send the chat messages to the model
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = messages,
    max_completion_tokens = 100
)

# Extract the assistant message from the response
assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}

# Add assistant_dict to the messages dictionary
messages.append(assistant_dict)
print(messages)


# Creating an AI chatbot

# To complete the proof the POC, we integraate the message history with a for loop, so reapeated prompts can be sent to the model, storing each response in the message history in series. 

# - Loop over the user messages.
# - Create a dictionary for the user message in each iteration, and append it to `messages`.
# - Send `messages` to the model in a chat request.
# - Append the assistant message dictionary to `messages`.

messages = [{"role": "system", "content": "You are a helpful math tutor that speaks concisely"}]

user_msgs = ["Explain what pi is. ", "Summarize this into two bullet points."]

# loop over the user questions

for q in user_msgs:
    print("User: ", q)

    # Create a dictionary for the user message from q and append to messages.
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)

    # create API request
    response = client.chat.completions.create(

        model = "gpt-4o-mini",
        messages = messages,
        max_completion_tokens = 100
    )

    # Append the assistant's message to messages
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    messages.append(assistant_dict)

    print("Assistant: " , response.choices[0].message.content, "\n")