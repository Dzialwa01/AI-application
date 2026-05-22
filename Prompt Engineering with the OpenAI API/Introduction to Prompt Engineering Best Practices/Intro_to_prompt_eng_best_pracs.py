# Dzialwa Nemakonde
# 09 March 2026

# You are developing a chatbot for an event management agency that will be used to facilitate networking during events.

# Using the OpenAI API, you prepare a dictionary to pass as the message to the `chat.completions` endpoint. The message needs to have 3 roles defined to ensure the model has enough guidance to provide helpful responses.

# Throughout the course, you'll write Python code to interact with the OpenAI API.

import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError ("API key not found")

client = OpenAI(api_key = api_key)

def get_response(prompt):

    response = client.chat.completions.create(

        model = "gpt-4o-mini",
        messages = prompt
    )

    print(response.choices[0].message.content)

conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": "I am preparing event for my friend merrage"}
]

get_response(conversation_messages)
# Answer:
# Here are some good conversation starters that can be used at networking events:

# 1. **Professional Background:**
#    - "What inspired you to pursue your current career?"
#    - "How did you get started in this industry?"

# 2. **Recent Projects:**
#    - "What exciting projects are you currently working on?"
#    - "Have you learned anything interesting from your recent projects?"

# 3. **Industry Trends:**
#    - "What trends are you seeing in our industry lately?"
#    - "How do you think technology is changing our field?"

# 4. **Networking Goals:**
#    - "What are you hoping to achieve by attending this event?"
#    - "Are there specific connections you’re looking to make today?"

# 5. **Advice and Insights:**
#    - "What advice would you give someone looking to advance in this industry?"
#    - "Have any mentors or experiences significantly shaped your career?"

# 6. **Common Interests:**
#    - "I noticed you mentioned [specific interest or hobby]. How did you get into that?"
#    - "What do you enjoy doing outside of work?"
# ...
#     - "Are there any tools or software you can’t live without in your job?"
#     - "What networking strategies have you found to be the most effective?"

# Remember to keep the conversation light and engaging, and to listen actively to build rapport. Good networking involves sharing, asking questions, and showing genuine interest in the other person.

# **Exploring prompt engineering**

# Prompt engineering refers to crafting effective prompts to guide the language model towards the intended response. By refining your prompts, you can achieve better results and guide the model towards generating more accurate and useful responses. Your task in this exercise is to modify the prompt you used in the previous exercise.

# Craft a prompt that asks the model to generate a poem about ChatGPT while ensuring that it is written in basic English that a child can understand.

prompt = [{"role": "system", "content": "You are master poem writer for children poetry who uses basic english"},
          {"role": "user", "content": "Write a poem about ChatGPT in plain english that a five-year-old child can understand"}
          ]

get_response(prompt)
# Answer:

# **ChatGPT, My Helpful Friend**

# In the land of words, oh so bright,  
# Lives a friend named ChatGPT, what a delight!  
# With words that dance and stories to share,  
# It helps me learn, it always cares.  

# When I’m stuck and don’t know what to say,  
# ChatGPT is here, ready to play.  
# It tells me tales of stars and streams,  
# And helps my dreams be bigger than dreams!  

# Ask it a question, it's quick as a bee,  
# It whispers the answers so joyfully.  
# From numbers to colors, from songs to rhymes,  
# ChatGPT is fun and saves me time!  

# So if you're curious, just give it a try,  
# With ChatGPT, we can learn to fly!  
# Together we giggle, together we cheer,  
# With a helpful friend like this, no need to fear! 