Here are the python codes for automated lecture notes generator extension "Earlens" 

Python Library Requirements for this codes are:-

- requests

- os

- sys

- time

- string

- nltk

- yake

- keybert

- dotenv

- openai

All of these can be installed by using

```
pip install  "name of the requirement"(Without Inverted Comas)

```

so after installing all the requirements:-

1) Need to have a MP3 FILE of a recorded lecture

2) Then you need to put your AssemblyAI's Free Speech To Text Conversion API Key and MP3 FILE into speechToText.py and it will return a transcribed file

3) Afterwards you need to upload that transcribed file to OpenAi-Summariser.py which will give you a summary and then to kw_and_wiki.py which will give you summarized
   notes as well as hyperlinks to keywords in a single pdf file :)
