# Dzialwa Nemakonde
# 02 March 2026

# Chat roles annd system messages exercises

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found in env file")

# **Utilizing systems messages**

# The Chat Completions endpoint supports three different roles to shape the messages sent to the model:

# - **System**: controls assistant's *behavior*
# - **User**: *instruct* the assistant
# - **Assistant**: *response* to user instruction

# In this exercise, you'll begin to design an AI system for helping people learn new skills, using a system message to set an appropriate model behavior.

# - Create a request using both *system* and *user* messages to create a study plan to learn to speak Dutch.
# - Extract and print the assistant's text response.

client = OpenAI (api_key = api_key)

response = client.chat.completions.create(

    model = "gpt-4o-mini",
    messages = [ {"role": "system", "content": "You are a study planning assistant that creates plans for learning new skills."},
                {"role": "user", "content": " I want to learn to speak Dutch"}
                ]
)

print(response.choices[0].message.content)
# Answer: Learning to speak Dutch can be an exciting and rewarding experience! Below is a structured 12-week study plan to help you develop your speaking skills in Dutch. The plan is divided into three phases: Introduction, Practice, and Immersion. Adjust the intensity and pace according to your schedule and learning preferences.

### Phase 1: Introduction (Weeks 1-4)

#### Week 1: Basics of Dutch
# - **Days 1-3:** 
#   - Learn the Dutch alphabet and pronunciation rules.
#   - Practice basic greetings and common phrases (e.g., “Hallo,” “Goedemorgen”).
#   - Use a language app (e.g., Duolingo, Babbel) for 15-20 minutes daily.
# - **Days 4-7:**
#   - Learn numbers (1-20) and days of the week.
#   - Start a vocabulary list of common nouns (e.g., household items).
#   - Practice pronunciation by repeating after language podcasts/videos.

#### Week 2: Simple Grammar and Vocabulary
# - **Days 1-3:**
#   - Learn subject pronouns and basic verb conjugation in the present tense.
#   - Expand vocabulary to include colors, food, and animals.
# - **Days 4-7:**
#   - Complete simple sentences using learned vocabulary.
#   - Introduce yourself in Dutch (name, age, origin).

#### Week 3: Building Sentences
# - **Days 1-3:**
#   - Learn the concepts of definite and indefinite articles (de, het, een).
# ...
# - Speak as often as possible, even to yourself, to build confidence.
# - Don't be afraid of making mistakes; they're essential for learning!

# Good luck with your Dutch learning journey! Enjoy the process, and don't hesitate to ask for help when needed.


# **Adding guardrails**

# One of the most popular uses of system messages is to add ***guardrails***, which places restrictions on model outputs.

# In this exercise, you'll place a restriction on model outputs preventing learning plans *not* related to languages, as your system is beginning to find its niche in that space. You'll design a custom message for users requesting these type of learning plans so they understand this change.

# • Complete the chat request, providing the system message in `sys_msg` and test a user message containing a non-language-related skill, such as rollerskating.

sys_msg = """You are a study planning assistant that creates plans for learning new skills. If these skills are non related to languages, return the message:

'Apologies, we focus on languages, we no longer create learning plans on other topics.'
"""

response = client.chat.completions.create(

    model = "gpt-4o-mini",
    messages = [{"role": "system", "content": sys_msg},
                {"role": "user", "content": "Help me learn python" }
                ]
)

print(response.choices[0].message.content)
# Answer : Apologies, we focus on languages, we no longer create learning plans on other topics.