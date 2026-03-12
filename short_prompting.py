# Dzialwa Nemakonde
# 26 February 2026

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found in env file")

# Shot prompting Exercise

# **Zero-shot prompting with reviews**

# As well as answering questions, transforming text, and generating new text, OpenAI's models can also be used for classification tasks, such as categorization and sentiment analysis.
# In this exercise, you'll explore using OpenAI's chat models for sentiment classification using reviews from an online shoe store called *Toe-Tally Comfortable*.

# **Instruction**
# - Define a `prompt` to classify the sentiment of the statements provided using the numbers `1` to `5` (positive to negative).
# - Create a request to the Chat Completions endpoint to send this prompt to `gpt-4o-mini`.

client = OpenAI(api_key = api_key)

def get_response(prompt):

    response = client.chat.completions.create(

        model = "gpt-4o-mini",
        messages = [{"role": "user", "content": prompt}],
        max_completion_tokens = 100
    )
    return response.choices[0].message.content

prompt1 = """Classify the sentiment of each review from 1 to 5.:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable. 
4. Can't wait to show them off!"""

print(get_response(prompt1))
# answer: Sure! Here are the sentiment classifications for each review from 1 to 5, with 1 being the most negative and 5 being the most positive:
# 1. Unbelievably good! - **5**
# 2. Shoes fell apart on the second use. - **1**
# 3. The shoes look nice, but they aren't very comfortable. - **3**
# 4. Can't wait to show them off! - **5**


# Exercise
# **One-shot prompting: will it be enough?**
# As you saw, there's room for improvement in your initial prompt. Try adding an example `Love these! = 5` and including `=` after each review to see if you can get more consistent formatting and more accurate numbers.**Instructions100 XP**
# • Add the example `Love these! = 5` to the start of the prompt, and add `=` after each review in the prompt to indicate how the result should be formatted.

prompt2 = """Classify sentiment as 1-5 (negative to positive):
1. Love these! = 5
2. Unbelievably good! = 
3. Shoes fell apart on the second use. = 
4. The shoes look nice, but they aren't very comfortable. = 
5. Can't wait to show them off! ="""

print(get_response(prompt2))
# Answer:
# Here are the sentiment classifications:
# 1. Love these! = 5
# 2. Unbelievably good! = 5
# 3. Shoes fell apart on the second use. = 1
# 4. The shoes look nice, but they aren't very comfortable. = 2
# 5. Can't wait to show them off! = 5


# Exercise: Few-shot prompting
# Now for the finale! Try adding the example Comfortable, but not very pretty = 2 to the prompt. As this example is more moderate, it might help the model with the troublesome second-to-last review.

prompt3 = """Classify sentiment as 1-5 (negative to positive):
1. Comfortable, but not very pretty = 2
2. Love these! = 5
3. Unbelievably good! = 
4. Shoes fell apart on the second use. = 
5. The shoes look nice, but they aren't very comfortable. = 
6. Can't wait to show them off! = 
"""

print(get_response(prompt3))
# Answer:
#  Here are the classifications for the given sentiments:
# 1. Comfortable, but not very pretty = 2
# 2. Love these! = 5
# 3. Unbelievably good! = 5
# 4. Shoes fell apart on the second use. = 1
# 5. The shoes look nice, but they aren't very comfortable. = 2
# 6. Can't wait to show them off! = 5