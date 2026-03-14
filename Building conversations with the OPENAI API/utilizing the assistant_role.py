# Dzialwa Nemakonde
# 03 March 2026

# Utilizing the system role exercises


## 📝 Practice Task

# Create a chatbot that:

# - teaches Python basics
# - gives short explanations
# - always includes an example

# Use:

# - system role → rules
# - assistant role → example answer
# - user role → question

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError ("API key not found in env file")

client = OpenAI(api_key = api_key)

response = client.chat.completions.create(

    model = "gpt-4o-mini",

    messages = [
        {"role": "system", "content": "You are a python teacher who teaches using short explanations and always include an example."},
        {"role": "user", "content": "What are tuples in python"},
        {"role": "assistant", "content": "A list is a mutable object which stores different object of different classes separated by commas. It is created using square brackets. e.g. ['cat', 1, [1, 5, 6]]"}
                ]
)

print(response.choices[0].message.content)
# Answer:
# Tuples in Python are immutable sequences of items. This means that once a tuple is created, its contents cannot be modified (you cannot add, change, or remove elements). Tuples are defined using parentheses `()` and can hold a mix of data types (like integers, strings, lists, etc.).

### Example:
# my_tuple = (1, "hello", 3.14)

# # Accessing elements
# print(my_tuple[1])  # Output: hello

# # Trying to modify an element (this will raise an error)
# # my_tuple[1] = "world"  # Uncommenting this line will cause a TypeError

# In summary, tuples are useful for storing a collection of items that should not change throughout the program.


# Adding Assistant messages
# Chat models are great for creating conversational applications, but they can be further improved by providing part of a conversation for the model to build on.

# Improve this geography tutor application by including this example student prompt and ideal model response in the messages:

# - Example Question: `Give me a quick summary of Portugal.`
# - Example Answer: `Portugal is a country in Europe that borders Spain. The capital city is Lisboa.`


response = client.chat.completions.create(

    model = "gpt-4o-mini",

    messages = [
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)
# Answer: Greece is a southeastern European country known for its rich history and cultural heritage, often considered the cradle of Western civilization. It consists of the mainland and numerous islands in the Aegean and Ionian Seas. The capital city is Athens, famous for ancient landmarks such as the Acropolis. Greece has a diverse landscape that includes mountains, coastline, and beautiful beaches, and it is known for its Mediterranean cuisine, vibrant traditions, and contributions to art, philosophy, and politics.


# More Assistant messages
# Expand on your previous messages to provide additional examples, stored as `example1`, `response1`, `example2`, `response2`, `example3`, and `response3`.

# Let's see if we can get this model outputting information in the desired format!

response = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
      
       {"role": "user", "content": "Give me a quick summary of Japan."},
       {"role": "assistant", "content": "Japan is an island nation in East Asia known for its advanced technology, rich culture, and capital city Tokyo."},
      
       {"role": "user", "content": "Give me a quick summary of Brazil."},
       {"role": "assistant", "content": "Brazil is the largest country in South America, famous for the Amazon rainforest and its capital Brasília."},
      
       {"role": "user", "content": "Give me a quick summary of Kenya."},
       {"role": "assistant", "content": "Kenya is an East African nation known for its diverse wildlife, Great Rift Valley, and capital Nairobi."},
      
       {"role": "user", "content": "Give me a quick summary of Greece."}
   ]
)

print(response.choices[0].message.content)

# Answer: Greece is a southeastern European country known for its ancient history, beautiful islands, and capital city Athens.