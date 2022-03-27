# set up a flask server

from flask import Flask, render_template, make_response, request
import json
from time import sleep
from random import random
from flask import Flask, render_template, make_response
import datetime
import os
from dotenv import load_dotenv
from speechToText import get_transcript
from OpenAi_Summariser import get_summary
from kw_and_wiki import get_kw_and_wiki

# create a flask app which recieves txt files from the client and extracts the text and processes it
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getfile", methods=["GET", "POST"])
def getfile():
    print(request.method)
    # print(request)
    # print(request.files)
    # print(dict(request.files))
    # print(request.files["myfile"])
    request.files["audio_recording"].save("audio_recording.mp3")
    print(request.files["audio_recording"])
    get_transcript()
    with open("transcript.txt", "r") as f:
        transcript = f.read()
    print(transcript)
    summary = get_summary()
    print(summary)
    kw_and_wiki = get_kw_and_wiki()
    print(kw_and_wiki)
    return render_template(
        "output.html", transcript=transcript, summary=summary, kw_and_wiki=kw_and_wiki
    )


if __name__ == "__main__":
    app.run(debug=True)
