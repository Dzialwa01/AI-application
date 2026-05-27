# Dzialwa Nemakonde
# 11 May 2026

# Few-shot prompting Exercises

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError ("API key not found")

Client = OpenAI(api_key = openai_api_key)


def get_response(prompt):

    response = Client.chat.completions.create(

        model = "gpt-4.1-mini",
        messages = prompt
    )

    return response.choices[0].message.content


# Exercise 1: Controlling output structure

# One way to control the output structure provided by a language model is to give it a sample question-answer in the prompt. The model will learn from it and follow it when generating responses for similar questions. This exercise aims to let you build a one-shot prompt that extracts odd numbers from a given set of numbers and displays them as a set of numbers between brackets, separated by commas as shown in the instructions.

# Instructions: Create a one-shot prompt that provides an example showing how to extract the odd numbers from the set {1, 3, 7, 12, 19}, and seeks an answer for the set {3, 5, 11, 12, 16}.

prompt1 =[{
    "role": "user", "content":"""
     Q: Extract the odd numbers from {1, 3, 7, 12, 19}. A: Odd numbers = 
     {1, 3, 7, 19}
     Q: Extract the odd numbers from {3, 5, 11, 12, 16}. A:"""
     }]

print(get_response(prompt1))
# Response
# Odd numbers = {3, 5, 11}


# Exercise 2: Sentiment analysis with few-shot prompting
# You're working on market research and your goal is to use few-shot prompting to perform sentiment analysis on customer reviews. You are assigning a number for a given customers conversation: -1 if the sentiment is negative, 1 if positive. 
# You provide the following examples as previous conversations for the model to learn from:
# - The product quality exceeded my expectations -> 1
# - I had a terrible experience with this product's customer service -> -1

prompt2 = [
           {"role": "user", "content": "The product quality exceeded my expectations"}, 
           {"role": "assistant","content": "1"},
           {"role": "user", "content": "I had a terrible experience with this product's customer service"}, 
           {"role": "assistant", "content": "-1"}, 
           {"role": "user", "content": "The price of the product is really fair given its features"}
           ]

print(get_response(prompt2))
# Response: 1