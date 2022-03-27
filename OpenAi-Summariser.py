#  use openai library to generate summary of a text file stored in a folder
#  and store the summary in a text file

# Load OPEN_AI_KEY from .env file
import os
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")


import openai

openai.api_key = OPEN_AI_KEY
prompt = "Summarise the text in 3 lines :"

with open("transcript.txt") as f:
    text = f.read()

prompt = "\n\n\n".join([prompt, text])

print(prompt)


response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.7,
    max_tokens=128,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print(response)
print(response.choices[0].text)

with open("response.txt", "w") as f:
    f.write(response.choices[0].text)
