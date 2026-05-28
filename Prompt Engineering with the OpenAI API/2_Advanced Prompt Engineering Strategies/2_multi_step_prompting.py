# Dzialwa Nemalonde
# 12 May 2026

# Multi-step prompting exercises.

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
        messages = [{"role": "user", "content":prompt}]     
    )

    return response.choices[0].message.content


# Exercise 1: Single-step prompt to plan a trip

prompt1 = " I have 2 weeks of break from my job. I need to plan for a beach vacation" # This leaves the model with so many question and it is unable to excute a well-structured plan for the trip

print(get_response(prompt1))
# response: 
# That sounds like a fantastic way to spend your break! To help you plan your beach vacation, here are a few questions:

# 1. **Destination Preferences:** Do you have a specific beach destination in mind, or are you open to suggestions? (e.g., tropical islands, coastal cities, secluded beaches)
# 2. **Budget:** What's your approximate budget for the trip? This helps in suggesting accommodations and activities.
# 3. **Travel Dates:** You mentioned 2 weeks—do you have exact dates set, or are they flexible?
# 4. **Activities:** What kind of activities do you enjoy? (e.g., relaxing on the beach, water sports, exploring local culture, dining)
# 5. **Accommodation:** Do you prefer hotels, resorts, vacation rentals, or something else?
# 6. **Travel Companions:** Are you traveling solo, with family, friends, or a partner?

# If you’d like, I can help you with destination ideas, itinerary suggestions, packing lists, or anything else you need!


# Exercise 2: Multi-step prompt to plan a trip
# You noticed that the single-step prompt was not effective, because the answer was too vague for what you had in mind. You improve your prompt by specifying the steps to follow for planning. The plan should have four potential locations for your beach vacation, and each location should have some accommodation options, some activities, and an evaluation of the pros and cons.

prompt2 = """
I need to plan for my 2 week beach vacation.
step 1: Have four potential locations.
step 2: Each location must have accommodation options and some activities.
step 3: Evaluate pros and cons for each location.
"""

print(get_response(prompt2))
# response:
#Great! Let's start planning your 2-week beach vacation step-by-step.

### Step 1: Four Potential Locations
# Here are four popular beach vacation destinations:

# 1. **Maui, Hawaii**
# 2. **Amalfi Coast, Italy**
# 3. **Bali, Indonesia**
# 4. **Tulum, Mexico**

# ### Step 2: Accommodation Options and Activities for Each Location

# #### 1. Maui, Hawaii
# - **Accommodation Options:**
#   - Luxury resorts (e.g., Four Seasons Resort Maui)
#   - Beachfront condos and vacation rentals
#   - Budget-friendly hotels and hostels in Kihei or Lahaina

# - **Activities:**
#   - Snorkeling and scuba diving at Molokini Crater
#   - Road to Hana scenic drive
#   - Whale watching (seasonal)
#   - Surf lessons
#   - Hiking in Haleakalā National Park

# #### 2. Amalfi Coast, Italy
# - **Accommodation Options:**
#   - Boutique hotels with sea views (e.g., Hotel Marincanto)
#   - Villas for rent in Positano or Amalfi
#   - Local guesthouses or B&Bs

# - **Activities:**
#   - Boat tours along the coast and to Capri island
#   - Visit picturesque towns (Positano, Ravello, Amalfi)
#   - Hiking the Path of the Gods trail
#   - Sampling local cuisine and wines
#   - Exploring historic churches and ruins

# #### 3. Bali, Indonesia
# - **Accommodation Options:**
#   - Luxury beach resorts in Nusa Dua or Seminyak
#   - Villas with private pools
#   - Budget guesthouses and hostels in Ubud or Canggu

# - **Activities:**
#   - Surfing at Kuta or Uluwatu
#   - Visiting temples like Tanah Lot and Uluwatu Temple
#   - Yoga retreats and wellness spas
#   - Exploring rice terraces and waterfalls
#   - Night markets and Balinese cultural shows

# #### 4. Tulum, Mexico
# - **Accommodation Options:**
#   - Eco-friendly beach cabanas
#   - Boutique hotels and resorts
#   - Vacation rentals

# - **Activities:**
#   - Visiting Mayan ruins near the beach
#   - Snorkeling or diving in cenotes (natural sinkholes)
#   - Relaxing on pristine beaches
#   - Exploring nearby Sian Ka’an Biosphere Reserve
#   - Enjoying local nightlife and restaurants

# ---

# ### Step 3: Evaluate Pros and Cons for Each Location

# | Location        |  Pros          |Cons            |
# 
# | **Maui**       | Beautiful diverse landscapes; great activities year-round; safe and accessible | Can be expensive; popular tourist destination (crowds)        |
# | **Amalfi Coast** | Stunning coastal views and charming towns; rich culture and cuisine | Peak season crowds; accommodations can be pricey; travel might be longer |
# | **Bali**       | Affordable; vibrant culture; many activities; good for wellness | Some areas crowded; tropical weather (rainy season); longer travel time from many countries |
# | **Tulum**      | Unique mix of beach and archaeological sites; eco-tourism; great nightlife | Infrastructure still developing; can get busy during peak seasons |


# Exercise 3: Analyse solution correctness
# You're back from your relaxing vacation and you've been assigned the task of reviewing and correcting some programming tasks, including a function to calculate of the area of a shape. You are provided with a code string that contains the function to calculate the area of a rectangle, and need to assess its correctness. The ideal function for you is a function that has correct syntax, receives two inputs, and returns one output.

code ='''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

prompt3 = f'''
Assess the function in the delimited code string.
Step 1: Check for correct syntax
Step 2: Check if the function receives two inputs
Step 3: Check if the functipn returns one output

{code}
'''

print(get_response(prompt3))
# response:
# Let's assess the function `calculate_rectangle_area` based on the three steps:

# **Step 1: Check for correct syntax**
# - The function syntax is correct: it uses the `def` keyword, a valid function name, parentheses with parameters, a colon, an indented block, and a return statement.
# - No syntax errors are present.

# **Step 2: Check if the function receives two inputs**
# - The function has two parameters: `length` and `width`.
# - This matches the requirement.

# **Step 3: Check if the function returns one output**
# - The function returns the variable `area`.
# - This means it returns one output as asked.

# ### Summary:
# - Syntax is correct.
# - Function receives two inputs.
# - Function returns one output.

# The function meets all the requirements.