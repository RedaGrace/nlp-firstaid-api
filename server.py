# -*- coding: utf-8 -*-
"""
Created on Sun May 22 06:17:52 2022

@author: LAPTOP
"""
import speech_recognition as sr

from flask import Flask, request, jsonify
import random
import os
#from nlp_service import nlp_service  # model class


# initialize the recognizer
r = sr.Recognizer()

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': "Let's get started and send me your symptoms", 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return 

@app.route('/firstaid', methods=['POST'])
def predict():
    # get audio file and save it
    audio_file = request.files['file']
    file_name = str(random.randint(0, 10000))
    audio_file.save(file_name)
    # create instance of the model class 
    #model = nlp_service()
    # make prediction
    #instructions = model.predict(file_name)
    # open the file
    with sr.AudioFile(file_name) as source:
    # listen for the data (load audio to memory)
        audio_data = r.record(source)
    # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        #print(text)
    # remove the audio file
    os.remove(file_name)
    # send back the instructions in json format
    data = {'firstaid_instructions': text}
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)
