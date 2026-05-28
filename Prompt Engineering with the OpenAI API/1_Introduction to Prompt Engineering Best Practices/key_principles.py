# Dzialwa Nemakonde
# 09 March 2026

import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError ("API key not found")

client = OpenAI(api_key = api_key)



# Exercises on the key princples of prompt engineering

### Task 1
#Rewrite this prompt: (Think about CLimate Change)

def get_response(prompt):

    response = client.chat.completions.create(
        
        model = "gpt-4o-mini",
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


prompt1 = "Name and give a brief explantion, of no more than 1 sentence, of the main contributors to climate change."


print(get_response(prompt1))
# Ai answer:
# 1. **Fossil Fuels**: The burning of coal, oil, and natural gas for energy releases large amounts of carbon dioxide and other greenhouse gases into the atmosphere.

# 2. **Deforestation**: The clearing of forests for agriculture or urban development reduces the number of trees that can absorb CO2, exacerbating climate change.

# 3. **Agriculture**: Livestock production and certain agricultural practices release methane and nitrous oxide, potent greenhouse gases that contribute significantly to climate change.

# 4. **Industrial Processes**: Manufacturing and chemical production emit various greenhouse gases and pollutants that impact the climate.

# 5. **Waste Management**: The decomposition of organic waste in landfills produces methane, and improper waste disposal can lead to increased emissions from harmful chemicals. 

# 6. **Transportation**: The use of cars, trucks, airplanes, and ships powered by fossil fuels generates significant carbon emissions, contributing to global warming.


### Task 2
# Write a prompt that explains JavaScript, targets beginners and uses max 5 sentences.

prompt2 = "Explain JavaScript in simple language to a beginner who has no idea of it. Use a maximum of 5 sentences"

print(get_response(prompt2))
# AI response
# JavaScript is a programming language that helps make websites interactive and dynamic. It's like giving instructions to a web page, telling it how to respond when you click buttons or fill out forms. With JavaScript, you can create things like image sliders, pop-up messages, and games right in your browser. It's used alongside HTML and CSS, which handle the structure and style of a webpage. Learning JavaScript can help you build more engaging and user-friendly websites

# Using delimited prompts with f-strings

# You are a junior developer at a dynamic startup that generates content with the help of AI. The company believes this technology can revolutionize storytelling, and you are excited to be a part of it. Today, your task is to generate a continuation of a story with a delimited prompt using an f-string.

# Create a prompt asking to complete the variable story (provided to you as a string): use f-string, and delimit the story with triple backticks (```) to pass its content to the prompt.

# Create a prompt that completes the story
story = "There once was a boy who grew up in Rosario Argentina. His dream was to be the best footballer in the whole wide world."
prompt3 = f"""Complete the story delimited by triple backticks. 
 ```{story}```"""

# Get the generated response 
response = get_response(prompt3)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)

#Output

#  Original story: 
# There once was a boy who grew up in Rosario Argentina. His dream was to be the best footballer in the whole wide world.

#  Generated story: 
#  There once was a boy who grew up in Rosario, Argentina. His dream was to be the best footballer in the whole wide world. From the moment he could walk, his small feet were always adorned with a pair of scuffed, second-hand cleats. Every day after school, he would rush to the local park, where the sun-drenched dirt pitch seemed to beckon him, surrounded by the laughter and cheers of his friends.

# His name was Mateo, and he was blessed with an uncanny ability to dribble the ball. He could weave through defenders as if they were mere cones in his path. His passion was infectious, often inspiring other children in the neighborhood to join him. They spent countless afternoons playing until dusk, their laughter echoing in the warm Argentine air.

# Mateo's father, a baker, often lamented that he spent too much time on the pitch and not enough in school. But Mateo was determined to make his dream a reality. He watched every match he could, sat glued to the television during the World Cup, and even collected posters of his idols. He knew every detail about players like Diego Maradona and Lionel Messi, both legends who had come from the same town.

# One fateful day, a local youth club was holding tryouts, and Mateo knew this was his chance. He gathered his friends and made the short walk to the field, his heart racing with excitement and nerves. Coaches with clipboards watched closely as the boys displayed their skills. Mateo took a deep breath, feeling the pressure intensify as he stepped onto the pitch.

# The moment he received the ball, everything disappeared. It was just him, the ball, and his dream. He danced around opponents, his feet a blur, dribbling and passing with precision. He scored two goals that day and earned a spot on the team. The coaches praised his talent, and for the first time, Mateo felt that his dreams might just be within reach.

# As he trained with the club, Mateo's skills sharpened, and he began to attract attention from scouts. However, the journey was not without its challenges. He faced injuries, moments of self-doubt, and the fierce competition of other aspiring young players. Yet, there was always a fire in his heart that ignited every time he laced up his cleats.

# Years passed, and his devotion turned into undeniable talent. When he was fifteen, scouts from clubs around Argentina descended upon him, eager to sign the next star. After much deliberation, Mateo joined a prestigious academy in Buenos Aires, leaving behind his family and friends.

# At the academy, life was tough. The training was rigorous, and the pressure to succeed loomed larger than ever. There were days when he felt isolated, missing the warmth of his hometown and the carefree days spent playing with friends. But with every challenge, he reminded himself of the joy that football brought him.


# Building specific and precise prompts

# In the previous exercise, you generated text that completes a given `story`. Your team was happy with your achievement, however, they want you to follow specific guidelines when it comes to **length** and **style**. Your task now is to craft a more specific prompt that controls these aspects of the generated story.
#• Craft a prompt that completes the given `story` with **only two paragraphs** in the style of **Shakespeare**; use f-string, and delimit the `story` with **triple backticks (```)**.

prompt4 = f"""Complete the story delimited by triple backticks. 
 ```{story}``` Complete it with two  paragraphs. Complete it in the style of shakespeare."""

response2 = get_response(prompt4)

print("\n Original story: \n", story)
print("\n Generated story: \n", response2)

#  Original story: 
#  There once was a boy who grew up in Rosario Argentina. His dream was to be the best footballer in the whole wide world.

#  Generated story: 
#  In yonder sun-kissed lands of fair Rosario, a lad of humble birth didst tread upon the verdant fields, where dreams took wing upon the breath of zephyrs sweet. Each morn, as Aurora's golden rays didst grace the earth, his heart, aflame with hope, didst summon forth the spirit of the greats who trod before him — Maradona, Pelé, the idols of his fervent soul. With naught but a tattered ball, he danced 'neath the heavens, weaving through the shadows cast by seraphic aspirations, his feet a symphony of grace, and the sphere a dutiful lover to his will. Yet, alas, the path to glory was beset with trials; for every starlit dream, a tempest loomed, and often did despair's chill grip enfold him, whispering darkly, "Thou art but a boy — what claim hast thou to greatness?"

# But ere the sun did set on his thirteenth year, a glorious chance didst bestow its serendipitous favor. A scout, a man of repute, with eyes that glimmered like the stars above, did chance upon his fervent play. "Lo! What wondrous talent doth spring from this fine youth!" quoth he, and thus thenceforth, the boy was lifted, as Phaëthon ascended to the sun, to a club where bonds of brotherhood were forged in sweat and passion. There, he donned the colors of dreams, his heart entwined with the love of the game. As seasons turned, his name became a sonnet upon the tongues of men, and from the fields of his youth, he didst rise to challenge the very sun — a beacon of hope for all who dared to dream. In pursuit of immortality, he chased not just a ball, but the essence of the beautiful game, thus etching his name alongside the legends of yore, in a tale spun of glory and ambition, forever sung by the bards of time.