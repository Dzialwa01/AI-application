# Dzialwa Nemakonde
# 07 May 2026

# Structured outputs and conditional prompts tasks and exercises

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError ("API key not found")

client = OpenAI(api_key = openai_api_key)


# Creating the get response function for the practice tasks that take in system and user messages .
def get_response(user_prompt, sys_prompt = "You are a helpful assistant"):

    response = client.chat.completions.create(

        model = "gpt-4.1-mini",
        messages = [{"role": "system", "content": sys_prompt}, {"role": "user", "content": user_prompt}]
    )

    return response.choices[0].message.content

# Practice Tasks

# Task 1
# Write a prompt to generate:
# - a table of 5 programming languages
# - columns: Name, Use Case

prompt1 = "Construct a table with 5 programming languages. The table must have two columns showing the name and the other column containing the use case"

print(get_response(prompt1))
# response: 
# Here is a table with 5 programming languages and their common use cases:

# | Programming Language | Use Case                                  |
# |----------------------|-------------------------------------------|
# | Python               | Web development, data science, automation|
# | JavaScript           | Web development, front-end and back-end  |
# | Java                 | Enterprise applications, Android apps     |
# | C++                  | Game development, system/software programming|
# | Ruby                 | Web development, scripting                 |


# Task 2
# Write a conditional prompt that
# - summarizes text only if it is in English
# - otherwise says: "Unsupported language"

sys_prompt = "You are a text summariser who summarises text in two and only summarises text in English. If it is in another language reply 'Unsupported language'"

eng_prompt = "Dragon fruit has bright pink or yellow skin with green scale-like tips, and its flesh is usually white or red with tiny black seeds. It has a mildly sweet taste, similar to kiwi and pear. It is rich in fibre, antioxidants, and vitamin C, making it refreshing and healthy. It is also low in calories and is often eaten fresh or added to smoothies."

prompt2 = "Dzialwa Nemakonde ndi mutakana wa manakanaka hafhu u dzhena ngei Kapa. U kho do mala huskale."

print(get_response(eng_prompt, sys_prompt))
# Response: Dragon fruit has bright pink or yellow skin with green tips, and white or red flesh with tiny black seeds. It tastes mildly sweet, similar to kiwi and pear. Rich in fiber, antioxidants, and vitamin C, it is refreshing, healthy, low in calories, and commonly eaten fresh or in smoothies.

print(get_response(prompt2, sys_prompt))
# Response: Unsupported language


# Task 3
# Create a custom output format for:
#- blog title
#- introduction paragraph
#- conclusion

sys_prompt2 = "You are a blog writer who creates blog from one sentence. You only write the blog title, the introduction paragraph and the conclusion."

prompt3 = "David (The Rugby captain) dramatically broke up with his 4 year long girlfriend"

print(get_response(prompt3, sys_prompt2))
# response:
# **Title:** When Leadership Meets Heartbreak: David, The Rugby Captain, Ends a Four-Year Relationship

# **Introduction:**  
# David, the steadfast captain of the rugby team, has recently faced a challenging moment off the field. Known for his resilience and leadership, David has dramatically ended his four-year-long relationship, leaving fans and teammates alike surprised. This unexpected turn in his personal life highlights how even the strongest among us navigate the complexities of love and growth.

# **Conclusion:**  
# While the details of David's breakup remain private, this moment serves as a reminder that personal struggles can affect anyone, regardless of their public image or achievements. As David continues to lead his team with determination, supporters hope he finds healing and strength in the days ahead. Just as in rugby, life's toughest battles sometimes lead to the greatest personal victories.


# Exercises

## Generating a table: Imagine you are a developer working for a renowned online bookstore known for its extensive collection of science fiction novels. Today, you have a task at hand: to create a table of ten must-read science fiction books for the website's homepage. This will enhance the user experience on the website, helping fellow sci-fi enthusiasts discover their next great read.


table_prompt = "Generate a table of 10 books one should read if they are a science fiction lover. The table must have 3 columns which are Title, Author, and Year"

print(get_response(table_prompt))
#response
# Certainly! Here's a table of 10 must-read science fiction books for any sci-fi lover:
# | Title                        | Author              | Year |
# |------------------------------|---------------------|------|
# | Dune                         | Frank Herbert       | 1965 |
# | Neuromancer                  | William Gibson      | 1984 |
# | Foundation                   | Isaac Asimov        | 1951 |
# | Ender's Game                 | Orson Scott Card    | 1985 |
# | The Left Hand of Darkness    | Ursula K. Le Guin   | 1969 |
# | Snow Crash                   | Neal Stephenson     | 1992 |
# | 1984                         | George Orwell       | 1949 |
# | The War of the Worlds        | H.G. Wells          | 1898 |
# | Hyperion                     | Dan Simmons         | 1989 |
# | The Martian                  | Andy Weir           | 2011 |


## Customizing output format
# You work as a developer at a startup that offers a text analysis platform for content creators. Your platform helps users automatically categorize and format their content, and you're now working on a new feature that detects the language of a given piece of text and generates a suitable title for that text in a custom format. You decide to craft a prompt that guides the language model through this.

sys_prompt3 = "You are a professional text analyser. You analyse text and determine the language the text is in and also generate a suitable title for it. The output will be in three lines in the order of 'Text', 'Language', then 'Title."

prompt4 = "Artificial Intelligence is transforming the way people work and communicate. From healthcare to education, AI-powered tools are helping solve complex problems faster and more efficiently. Many companies are now investing heavily in AI research to build smarter applications for the future."

print(get_response(prompt4, sys_prompt3))
# Response
# Text: Artificial Intelligence is transforming the way people work and communicate. From healthcare to education, AI-powered tools are helping solve complex problems faster and more efficiently. Many companies are now investing heavily in AI research to build smarter applications for the future.  
# Language: English  
# Title: The Impact of Artificial Intelligence on Modern Work and Communication

#Testing how it does in spanish
prompt5 = "La inteligencia artificial está transformando la forma en que las personas trabajan y se comunican. Desde la salud hasta la educación, las herramientas impulsadas por IA están ayudando a resolver problemas complejos de manera más rápida y eficiente. Muchas empresas están invirtiendo fuertemente en la investigación de IA para crear aplicaciones más inteligentes para el futuro."

print(get_response(prompt5, sys_prompt3))
# Response
# Text: La inteligencia artificial está transformando la forma en que las personas trabajan y se comunican. Desde la salud hasta la educación, las herramientas impulsadas por IA están ayudando a resolver problemas complejos de manera más rápida y eficiente. Muchas empresas están invirtiendo fuertemente en la investigación de IA para crear aplicaciones más inteligentes para el futuro.  
# Language: Spanish  
# Title: Impacto de la Inteligencia Artificial en el Trabajo y la Comunicación


## Using conditional prompts
# Building upon the previous task, your next challenge is to enhance the responses you received. When processing a given text, you need to determine its language, count the number of sentences, and generate a suitable title if the text contains more than one sentence. However, here's the new twist: if the text consists of only one sentence, no title should be generated, and instead, the model should display "N/A". This modification ensures that the title is generated only for texts with multiple sentences, providing a more refined and practical output for your platform's users.

sys_prompt4 = "You are a professional text analyser. You analyse text and determine the language the text is in, you countthe number of sentences in the text and also generate a suitable title for it if it contains more than 1 sentence. The output will be in three lines in the order of 'Text', 'Language', 'number of sentences', then 'Title'. If the text xonsists of only one sentence, do not generate any title just write 'N/A'."

prompt6 = "L’intelligence artificielle change la manière dont les personnes travaillent, apprennent et communiquent. Dans des domaines comme la santé, l’éducation et les affaires, les outils basés sur l’IA permettent de résoudre des problèmes plus rapidement et avec plus de précision. Aujourd’hui, de nombreuses organisations investissent dans cette technologie afin de créer des solutions plus intelligentes pour l’avenir."

print(get_response(prompt6, sys_prompt4))
#response
# Text: L’intelligence artificielle change la manière dont les personnes travaillent, apprennent et communiquent. Dans des domaines comme la santé, l’éducation et les affaires, les outils basés sur l’IA permettent de résoudre des problèmes plus rapidement et avec plus de précision. Aujourd’hui, de nombreuses organisations investissent dans cette technologie afin de créer des solutions plus intelligentes pour l’avenir.
# Language: French
# Number of sentences: 3
# Title: L'impact de l'intelligence artificielle sur la société

prompt7 = "Artificial Intelligence is changing how people learn, work, and solve problems. In industries such as healthcare, education, and business, AI tools are making tasks faster, smarter, and more efficient. As technology continues to grow, many companies are using AI to improve services and prepare for the future."

print(get_response(prompt7, sys_prompt4))
# response
# Text: Artificial Intelligence is changing how people learn, work, and solve problems. In industries such as healthcare, education, and business, AI tools are making tasks faster, smarter, and more efficient. As technology continues to grow, many companies are using AI to improve services and prepare for the future.
# Language: English
# number of sentences: 3
# Title: The Impact of Artificial Intelligence Across Industries


prompt8 = "Artificial Intelligence is helping people and businesses complete tasks faster, make better decisions, and create smarter solutions for the future."

print(get_response(prompt8, sys_prompt4))
# response
# Text: Artificial Intelligence is helping people and businesses complete tasks faster, make better decisions, and create smarter solutions for the future.
# Language: English
# number of sentences: 1
# Title: N/A