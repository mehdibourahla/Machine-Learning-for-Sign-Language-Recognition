from flask import Flask, render_template, url_for, request
import requests
import numpy as np
import pandas as pd
import json
from sklearn.preprocessing import LabelEncoder
from scipy.io import loadmat
import random
app = Flask(__name__)

# Settings
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
encoder = LabelEncoder()

# Import files
csi = loadmat('csi.mat')['test']
labels = pd.read_csv("labels.csv", header = None).iloc[:,0]
words = pd.read_csv("sign_labels.csv", header = None).iloc[:,0].tolist()
encoder.classes_ = np.load('classes.npy')

@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        # GET THE SENTENCE
        sentence = request.form['sentence']
        indexes = []
        for word in sentence.split(" "): # Gives each word in the given sentence its label value [1-276]
            indexes.append(label2index(word))

        # Get the CSI values for each word in the last sentence. Only one CSI instance is considered.
        csi_sequence = []
        for index in indexes:
            csi_sequence.append(csi[index])

        # Feed the CSI values one by one to CNN model and get their predictions in a form of a label sequence.
        predictions = csi2sentence(csi_sequence)

        # Use the sequence of labels to get the words in the sentence.
        sentence = []
        for index in predictions:
            sentence.append(index2word(index))

        # Feed the sequence of words (sentence) to the LSTM to get the command label.
        prediction = sentence2label(predictions)

        # Identify the command
        command = label2object(prediction)

        # Update on the environment
        seed[command['location']][command['object']] = command['action']

        return render_template("index.html", sentence =' '.join(sentence), seed = seed, command = command)
    else:
        return render_template("index.html")

def label2index(label):
    return words.index(label)

def label2object(label):
    if "ON" in label:
        action = 1
    elif "OFF" in label:
        action = 0
    else:
        action = -1
    if "BATH" in label:
        location = 1
    elif "KIT" in label:
        location = 2
    elif "ROOM" in label:
        location = 3
    elif "GAR" in label:
        location = 4
    elif "TOI" in label:
        location = 1
    else:
        location = -1
    if "DO" in label:
        obj = 1
    elif "SH" in label:
        obj = 2
    elif "AC" in label:
        obj = 3
    elif "FA" in label:
        obj = 4
    elif "RA" in label:
        obj = 5
    elif "TV" in label:
        obj = 6
    elif "REF" in label:
        obj = 7
    elif "WIN" in label:
        obj = 8
    elif "WA" in label:
        obj = 9
    elif "PC" in label:
        obj = 10
    else:
        obj = -1
    command = {
        "action": action,
        "location": location,
        "object": obj
    }
    return command

def index2word(index):
    return words[index]

def csi2sentence(csi_sequence):
    predictions = []
    for word in csi_sequence:
        word = np.array(word).reshape(1,200,60,3).tolist()
        post_data = {"instances": word}
        response = requests.post(
            'http://localhost:8501/v1/models/model:predict',
            data = json.dumps(post_data),
            headers=headers
            )
        content = json.loads(response.content)['predictions'][0]
        prediction = content.index(max(content))
        predictions.append(prediction)
    return predictions

def sentence2label(predictions):
    while(len(predictions)<4):
        predictions.append(0)
    predictions = np.array(predictions).reshape(1,4)
    post_data = {"instances": predictions.tolist()}
    response = requests.post(
        'http://localhost:8502/v1/models/model:predict',
        data = json.dumps(post_data),
        headers=headers
        )
    content = json.loads(response.content)['predictions'][0]
    prediction = encoder.inverse_transform([content.index(max(content))])[0]
    return prediction

# This variable is used to save the environment state.
seed = {
        3: {
            3:0,
            8:0,
            10:0,
            1:0
            },
        4:{
            1:0,
            4:0,
            5:0
        },
        2:{
            5:0,
            7:0,
            8:0
        },
        1:{
            9:0,
            2:0,
            8:0
        },
        -1:{
            3:0,
            6:0
        }
        }

if __name__ == "__main__":
    app.run(debug=True)