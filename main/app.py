from flask import Flask,render_template, jsonify, request,redirect, url_for
from flask_cors import CORS 
import pywhatkit
import pickle
from flask_ngrok import run_with_ngrok
from chatbot import brain 
import subprocess
import sys
import datetime
import webbrowser
import time
import os
import pyjokes
import psutil
import platform
import random
import cv2
import gtts
from playsound import playsound

NAME = 'SUBHOMOY'
    
def jokes():
    speak(pyjokes.get_joke())

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at"+ str(battery.percent))

def speak(text):
    file = "hola.mp3"
    tts = gtts.gTTS(text, lang="en")
    tts.save(file)
    playsound(file)
    os.remove(file)
    return text

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current Date is")
    speak(str(date)+' '+str(month)+' '+ str(year))
    # speak("I am going to Fuck You",file)

def system():
    system_data = platform.uname()
    speak('I am THOR version 1 point O personal assistant.')
    speak('My Operating System is'+str(system_data.system))
    speak('My Machine is'+str(system_data.machine))
    speak('My Processor is'+str(system_data.processor))
    speak('My Release is'+str(system_data.release))
    speak('My Version is'+str(system_data.version))

app = Flask(__name__)
CORS(app)
# run_with_ngrok(app)               #this is needed to use ngrok for port forwarding
database={'subho':'hero','soham':'chomu','yash':'pagla','tublu':'7415'}

@app.route('/predict',methods=['GET','POST'])
def index():
    user_input = request.args.get('user_input')
    user_input = user_input.lower()
    print(user_input)
    if 'open google' in user_input:
        webbrowser.open("google.com")
        return jsonify({'user_input':str(user_input)})
    elif 'the time' in user_input:
        strTime = datetime.datetime.now().strftime("%I:%M:%S")    
        msg = speech1(f"Sir, the time is {strTime}")
        return jsonify({'user_input':str(msg)})
    elif 'the date' in user_input:
        date()
        return jsonify({'user_input':str(user_input)})
    elif 'who are you' in user_input or 'what can you do' in user_input:
        system()
        return jsonify({'user_input':str(user_input)})
    elif "who made you" in user_input or "who created you" in user_input or "who discovered you" in user_input:
        msg = speak("I am built by Subhomoy")
        print("I was built by Subhomoy")
        return jsonify({'user_input':str(msg)})
    elif 'cpu'in user_input:
        cpu()
        return jsonify({'user_input':str(user_input)})
    elif 'joke' in user_input:
        jokes()
        return jsonify({'user_input':str(user_input)})
    elif "search youtube" in user_input:
        user_input = user_input.replace('search youtube', '')  
        pywhatkit.playonyt(user_input)
        return jsonify({'user_input':str("searched youtube"+str(user_input))})
    elif "search" in user_input:
        user_input = user_input.replace('search', '')  
        pywhatkit.search(user_input) 
        return jsonify({'user_input':str("searched"+str(user_input))})
    else:
        mssg = speak(str(brain(user_input)))
        return jsonify({'user_input':str(mssg)})

if __name__ == '__main__':
    app.run()
    