# -*- coding: utf-8 -*-
"""
Created on Sun May 22 06:17:52 2022

@author: LAPTOP
"""
import speech_recognition as sr
from googletrans import Translator, constants
from nlp_service import nlp_service


from waitress import serve
from flask import Flask, request, jsonify
import random
import os
import json
#from nlp_service import nlp_service  # model class


# initialize the recognizer
r = sr.Recognizer()
translator = Translator()

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': "Let's get started and send me your text", 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/predict/', methods=['GET'])
def request_page():
    symptoms = request.args.get('text') # /predict/?text=text
    #User_text = request.files['file']
    #file_name = str(random.randint(0, 10000))
    #User_text.save(file_name)
    # open the file
    #with sr.AudioFile(file_name) as source:
    # listen for the data (load audio to memory)
    #audio_data = r.record(source)
    # recognize (convert from speech to text)
    #text_in_arabic = r.recognize_google(audio_data, language="ar-EG")
    # translate into English
    #translation = translator.translate(User_text)
    # create instance of the model class
    #model = nlp_service()
    # making prediction and getting response
    #response = model.get_response(translation.text)
    # remove the audio file
    #os.remove(file_name)
    # send back the instructions in json format
    #data = {'source_text': User_text}
    '''
            , 'translation': translation.text,
            'firstaid_instructions': response,
            'firstaid_instructions_in_arabic': (translator.translate(response, dest="ar")).text}
    '''
    #return json.dumps(data)

    data = {'source_text': symptoms}
    data_set = json.dumps(data)
    return data_set

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port, debug=True)
    serve(app, host='0.0.0.0', port=port, debug=True)
