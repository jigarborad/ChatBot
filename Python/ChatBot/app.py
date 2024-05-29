import sys

import nltk

nltk.download('popular')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import re
import pandas as ps
from flask import Flask, render_template, request

model = pickle.load(open('d:/Work/NLP-ChatBot/Python/ChatBot/model.sav', 'rb'))
bow = pickle.load(open('d:/Work/NLP-ChatBot/Python/ChatBot/bow.sav', 'rb'))
data = ps.read_json('d:/Work/NLP-ChatBot/Python/ChatBot/intents.json')
import json
import random


def predict(userText):
    Input = userText
    tokens1 = nltk.word_tokenize(Input)
    tokens1 = [word.lower() for word in tokens1]
    x1 = bow.transform(tokens1)
    thresh = 0.5
    result = model.predict_proba(x1)
    y1_pred = model.predict(x1)
    max = np.amax(result)
    c = 0
    for i in result:
        if np.max(i) == max:
            break
        else:
            c += 1

    for i in data['intents']:
        if i['tag'] == y1_pred[c]:
            return random.choice(i['responses'])
        else:
            pass


app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText == 'quit':
        sys.exit()
    else:
        return predict(userText)


if __name__ == "__main__":
    app.run()
