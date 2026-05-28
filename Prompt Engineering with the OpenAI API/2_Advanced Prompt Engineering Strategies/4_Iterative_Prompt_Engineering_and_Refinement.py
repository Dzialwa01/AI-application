# Dzialwa Nemakonde
# 14 May 2026

# Iterative prompt engineering and refinement exercises.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError ("API key not found")

client = OpenAI(api_key = openai_api_key)


def get_response(messages):

    response = client.chat.completions.create(

        model = "gpt-4.1-mini",
        messages = messages
    )

    return response.choices[0].message.content


# Exercise 1: Iterative prompt engineering for standard prompts
# You are a developer using prompt engineering techniques for your various tasks, and you want to carefully select the right language model. You wrote an initial prompt to know what are the top ten pre-trained language models out there. Now, your goal is to refine this prompt to generate a table presenting information on each model's name, release year and its owning company.

Messages = []
prompt = ""

while True:

    prompt = input("Write your prompt here: ")
    print(prompt+ "\n")
    if prompt == "":
        break
    else: 
        message = {"role": "user", "content": prompt}

    Messages.append(message)
    print(get_response(Messages) + "\n" )


 # AI Response:
# List the top 10 pre-trained language models without explanations
# As of mid-2024, the top pre-trained language models (based on their impact, size, architecture, and capabilities) are generally recognized as follows:

# List the top 10 pre-trained language models without explanations

# 1. GPT-4  
# 2. PaLM 2  
# 3. Claude 2  
# 4. LLaMA 2  
# 5. GPT-3.5  
# 6. BLOOM  
# 7. T5 (Text-to-Text Transfer Transformer)  
# 8. BERT  
# 9. RoBERTa  
# 10. XLNet

# Add a table with 3 columns

# | Rank | Language Model         | Developer            |
# |-------|------------------------|---------------------|
# | 1     | GPT-4                  | OpenAI              |
# | 2     | PaLM 2                 | Google              |
# | 3     | LLaMA 2                | Meta                |
# | 4     | Claude                 | Anthropic           |
# | 5     | Bard (LaMDA)           | Google              |
# | 6     | Falcon                 | Technology Innovation Institute |
# | 7     | Chinchilla             | DeepMind            |
# | 8     | Gopher                 | DeepMind            |
# | 9     | OPT                    | Meta                |
# | 10    | T5                     | Google              |

# list model name

# | Model Name          | Developer        | Year Released |
# |---------------------|------------------|---------------|
# | GPT-4               | OpenAI           | 2023          |
# | PaLM 2              | Google           | 2023          |
# | Claude              | Anthropic        | 2023          |
# | LLaMA 2             | Meta             | 2023          |
# | GPT-3               | OpenAI           | 2020          |
# | BERT                | Google           | 2018          |
# | RoBERTa             | Facebook AI      | 2019          |
# | T5                  | Google           | 2019          |
# | ERNIE               | Baidu            | 2019          |
# | XLNet               | Google/CMU       | 2019          |

# release date and owning company

# | Model Name           | Release Date | Owning Company      |
# |---------------------|--------------|---------------------|
# | GPT-4               | 2023-03      | OpenAI              |
# | PaLM 2              | 2023-05      | Google              |
# | LLaMA 2             | 2023-07      | Meta                |
# | Claude              | 2023-03      | Anthropic           |
# | ERNIE 3.0 Titan     | 2022-10      | Baidu               |
# | Megatron-Turing NLG | 2021-10      | Nvidia & Microsoft  |
# | Gopher              | 2021-12      | DeepMind            |
# | OPT                 | 2022-05      | Meta                |
# | T5                  | 2020-10      | Google              |
# | XLNet               | 2019-06      | Google & CMU        |


## Exercise 2: Iterative prompt engineering for few-shot prompts

# You are currently working on a project at your content creation company. The project's objective is to develop a text classification model capable of accurately identifying and categorizing different emotions in text, such as happiness, sadness, and fear. In cases where the text does not contain any discernible emotion, you aim for the model to respond with "no explicit emotion."
# You decided to use the provided few-shot `prompt`. However, you've noticed that "Time flies like an arrow" is being incorrectly classified as "surprise." Your objective now is to refine the `prompt` so that the model correctly classifies this particular example as "no explicit emotion."

Messages2 = [{"role": "assistant", "content": "You are a text classifier who accurately categorises different emotion in text such as happiness, sadness and fear."}]
prompt2 = ""

while True:

    prompt2 = input("Write your prompt here: ")
    print(prompt2 + "\n")
    if prompt2 == "":
        break
    else: 
        message = {"role": "user", "content": prompt2}

    Messages2.append(message)
    print(get_response(Messages2) + "\n" )

# AI Response:
# Receiving a promotion at work made me feel on top of the world -> Happiness 
# The movie's ending left me with a heavy feeling in my chest -> 
# Sadness Walking alone in the dark alley sent shivers down my spine -> Fear 
# Times flies like an arrow ->

# The sentence "Times flies like an arrow" expresses a neutral statement and does not convey a clear emotion like happiness, sadness, or fear. Therefore, it is best classified as **Neutral**.

# Write it as no explicit emotion

# Times flies like an arrow -> No explicit emotion

# How about this one: They sat and ate their meal

# They sat and ate their meal: No explicit emotion