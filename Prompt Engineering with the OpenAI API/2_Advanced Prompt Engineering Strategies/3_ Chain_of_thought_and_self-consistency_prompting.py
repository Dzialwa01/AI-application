# Dzialwa Nemakonde
# 13 May 2026

# Chain-of-Thought and self-consistency prompting exercises

# Writing the get response function to utilise in the exercises

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError ("API key not found")

client = OpenAI(api_key = openai_api_key)


def get_response(prompt):

    response = client.chat.completions.create(

        model = "gpt-4.1-mini",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


## Exercise 1: Reasoning with chain-of-thought prompts

# In this exercise, you will craft a chain-of-thought prompt to let the language model guess the age of your friend's father n 10 years, given that he is currently twice your friend's age, and your friend is 20.

prompt1 = '''
Guess the age of my friend's father in 10 years based  on below conditions.
1. My friend is 20.
2. My friend's father is twice his age
'''

print(get_response(prompt1))
# Response:
# Let's analyze the information:
# 1. Your friend is 20 years old.
# 2. Your friend's father is twice his age.

# So, your friend's father's current age = 2 × 20 = 40 years.

# In 10 years, the father's age will be:

# 40 + 10 = **50 years old**.

# **Answer:** Your friend's father will be 50 years old in 10 years.


## Exercise 2: Chain-of-thought prompts with one-shot prompting
# When you need to sum the even numbers within a given set, you first have to identify these even numbers and then sum them. 
# Your goal in this exercise is to teach the model how to apply this procedure on the following set: `{9, 10, 13, 4, 2}`, and then ask the model to perform it on a new set: `{15, 13, 82, 7, 14}`. 

# Defining the example
example = '''Q: Sum the even numbers in the following set: {9,10,13,4,2}
             A: Even numbers: (10,4,2). Adding them: 10+4+2 = 16'''

question = "Sum the even numbers in the following set: {15,13,82,7,14}"

prompt2 = f""" Answer this {question} guided by this {example}"""

print(get_response(prompt2))
# Response
# Let's identify the even numbers in the set {15,13,82,7,14}:
# Even numbers are: 82 and 14.
# Adding them: 82 + 14 = 96
# **Answer: 96**


# Exercise 3: Self-consistency prompts
# Imagine you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?
# Instruction: Create the self_consistency_instruction that allows the model to solve the problem with three experts and combine the results with a majority vote.

problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

prompt3 = f''' Imagine three independent experts solving a problem. With each expert explaining their reasoning in solving this problem {problem_to_solve}. Choose the final answer by majority vote'''

print(get_response(prompt3))
# Response: Let's analyze the problem step-by-step from the perspective of three independent experts, each providing their reasoning.
### Expert 1:

# Step 1: Initial numbers
# - Total devices = 50
# - Mobile phones = 60% of 50 = 0.6 * 50 = 30
# - Laptops = 50 - 30 = 20

# Step 2: Sales during the day
# - Three clients each bought 1 mobile phone → total mobile phones sold = 3
# - One of these clients also bought 1 laptop → laptops sold = 1

# Step 3: New arrivals
# - Added 10 laptops
# - Added 5 mobile phones

# Step 4: Final count
# - Mobile phones end of day = Initial (30) - Sold (3) + Added (5) = 32
# - Laptops end of day = Initial (20) - Sold (1) + Added (10) = 29

### Expert 2:

# Step 1: Initial calculation
# - Total = 50
# - Mobile = 60% * 50 = 30
# - Laptop = 50 - 30 = 20

# Step 2: Client purchases
# - 3 mobiles sold (one to each client)
# - 1 laptop sold (one client bought additional laptop)

# Step 3: Additions
# - Add 10 laptops
# - Add 5 mobiles

# Final tally:
# - Mobile phones: 30 - 3 + 5 = 32
# - Laptops: 20 - 1 + 10 = 29

### Expert 3:

# Starting data:
# - Total devices = 50
# - Mobile phones: 60% of 50 → 30
# - Laptops: 20

# During the day:
# - Sold 3 mobiles (1 per client)
# - Sold 1 laptop (since one client bought an additional laptop)

# Added devices:
# - 10 laptops added
# - 5 mobiles added

# Final:
# - Mobiles = 30 - 3 + 5 = 32
# - Laptops = 20 - 1 + 10 = 29

# Therefore, by the end of the day you have 32 mobile phones and 29 laptops.