# Dzialwa Nemakonde
# 25 February 2026

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found in env file")

# Text generation Exercises


### **Content generation**

# AI is playing a much greater role in content generation, from creating marketing content such as blog post titles to creating outreach email templates for sales teams.

# In this exercise, you'll harness AI to generate a catchy slogan for a new restaurant. Feel free to test out different prompts, such as varying the type of cuisine (Italian, Chinese, etc.) or the type of restaurant (fine-dining, fast-food, etc.), to see how the response changes.

# - Create a request to create a slogan for a new restaurant; set the maximum number of tokens to `100`

client = OpenAI(api_key = api_key)

def get_response(prompt):

    response = client.chat.completions.create(

        model = "gpt-4o-mini",
        messages = [{"role": "user", "content": prompt}],
        max_completion_tokens = 100,
        
    )
    return response.choices[0].message.content

prompt1 = "Generate a catchy slogan for a new fast-food chinese restaurant"
prompt2 = "Generate a catchy slogan for a new fast-food italian restaurant"
prompt3 = "Generate a catchy slogan for a new fine-dining chinese restaurant"
prompt4 = "Generate a catchy slogan for a new fine-dining italian restaurant"


print(get_response(prompt1)) # "Wok This Way: Quick Bites, Bold Flavors!"
print(get_response(prompt2)) # "Slice into Italy: Fast Flavor, Freshly Made!"
print(get_response(prompt3)) # "Savor the Elegance: Where Tradition Meets Taste!"
print(get_response(prompt4)) # "Savor La Dolce Vita: Where Every Bite is a Masterpiece!"

## **Generating a product description**

# Imagine you're writing marketing copy for **SonicPro** headphones. Your goal is to generate a **persuasive product description** using the OpenAI API.

# Test how different **prompting techniques**, **response lengths**, and **temperature settings** influence the output!

# Instruction

# - Create a **detailed prompt** to generate a product description for SonicPro headphones, including:
#     - Active noise cancellation (ANC)
#     - 40-hour battery life
#     - Foldable design
# - Experiment with `max_completion_tokens` and `temperature` settings to see how they affect the output.

# Create a detailed prompt
prompt = """
I need a product description for SonicPro headphones, wireless headphone with 40 hour of battery life. Active noise cancellation (ANC) and a foldable design.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens = 200,
    temperature = 1 
)

print(response.choices[0].message.content)

# Examples of the AI responses

# **SonicPro Wireless Headphones** ## MCT = 100; T = 0

# Elevate your audio experience with the SonicPro Wireless Headphones, where cutting-edge technology meets exceptional comfort. Designed for the modern listener, these headphones boast an impressive 40-hour battery life, ensuring that your favorite tunes, podcasts, and calls last all day long without interruption.
# Experience sound like never before with our advanced Active Noise Cancellation (ANC) feature, which effectively blocks out ambient noise, allowing you to immerse yourself fully in your audio. Whether you're commuting, ## MCT = 100; T = 0

# **SonicPro Wireless Headphones** 

# Elevate your audio experience with the SonicPro Wireless Headphones, where cutting-edge technology meets exceptional comfort. Designed for the modern listener, these headphones boast an impressive 40-hour battery life, ensuring that your favorite tunes, podcasts, and calls last all day long without interruption.
# Experience the world like never before with Active Noise Cancellation (ANC) technology, which effectively blocks out ambient noise, allowing you to immerse yourself fully in your audio. Whether you're commuting, working, or simply relaxing at home, SonicPro headphones create a serene soundscape tailored just for you.
# The foldable design makes SonicPro headphones the perfect travel companion. Easily pack them in your bag or carry them in your hand, and enjoy high-quality sound wherever you go. With plush ear cushions and an adjustable headband, these headphones provide a comfortable fit for hours of listening pleasure.
# Discover the perfect blend of style, functionality, and performance with SonicPro Wireless Headphones—your ultimate audio solution for every occasion. 

# **Product Description: SonicPro Wireless Headphones** # T = 1, MCT = 200

# Experience unparalleled audio quality and comfort with the SonicPro Wireless Headphones. Designed for audiophiles and casual listeners alike, these headphones blend cutting-edge technology with sleek design to deliver an exceptional listening experience.

# **Key Features:**

# - **Extended Battery Life:** Enjoy up to 40 hours of continuous playback on a single charge, allowing you to immerse yourself in your favorite tunes or podcasts without interruptions. Perfect for long commutes, travel, or marathon listening sessions.
# - **Active Noise Cancellation (ANC):** Dive into your music without distractions. Our advanced Active Noise Cancellation technology effectively blocks out ambient noise, allowing you to focus on what matters most—your sound.
# - **Foldable Design:** The SonicPro headphones are designed with portability in mind. Their compact, foldable design makes them easy to carry in your bag or backpack, ensuring you can enjoy high-quality audio wherever you go.
# - **Comfortable Fit:** With plush ear cushions and an adjustable