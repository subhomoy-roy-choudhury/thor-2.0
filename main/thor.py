from speech import *
from heart_disease_predict import *
from chatbot import brain 
from face_func import face
from emotion_func import emotion
from gender_age import gender_age
from recording import voice_run
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
from plyer import notification

def jokes():
    speak(pyjokes.get_joke())

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at"+ str(battery.percent))

def wishMe(name,title):
    speak("Welcome"+ str(name))
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(str(date)+'/'+str(month)+'/'+ str(year))
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(str(date)+' '+str(month)+' '+ str(year))
    if hour>=6 and hour<12:
        speak("Good Morning"+ str(name)+str(title))

    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ str(name)+str(title))

    elif hour>=18 and hour<24:
        speak("Good Evening"+ str(name)+str(title))

    else:
        speak("Good Night"+ str(name)+str(title))

    speak(f"THOR at your Service. Please tell me how can I help You {title}")

def run():
    wishMe(NAME,TITLE)
    while True:
        command = take_command()
        print(command)
        if 'open google' in command:
            webbrowser.open("google.com")
        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'the date' in command:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(str(date)+' '+str(month)+' '+ str(year))
        elif 'who are you' in command or 'what can you do' in command:
            system_data = platform.uname()
            speak('I am THOR version 1 point O' +str(NAME)+ 'persoanl assistant.')
            speak('My Operating System is'+str(system_data.system))
            speak('My Machine is'+str(system_data.machine))
            speak('My Processor is'+str(system_data.processor))
            speak('My Release is'+str(system_data.release))
            speak('My Version is'+str(system_data.version))

        elif "who made you" in command or "who created you" in command or "who discovered you" in command:
            speak("I am built by Subhomoy")
            print("I was built by Subhomoy")
        elif 'cpu'in command:
            cpu()
        elif 'joke' in command:
            jokes()
        elif 'go to sleep' in command:
            speak("ok sir shutting down the system")
            break
        elif 'heart' in command:
            heart_disease_predict()
        else:
            talk(str(brain(command)))

def authentication():
    if str(face())=="SUBHO":
        number = random.randint(100000,999999)
        notification.notify(
        title = "Hacker",
        message = f"You OTP is {number}",
        timeout = 30
        )
        print(number)
        num = int(input("Enter the OTP : "))
        if num == number :
            talk("Voice Authentication")
            talk(f"Say your name")
            if (str(voice_run())=='subho'):
                talk("Access Granted")
                return 'unlocked'

if __name__ == '__main__':
    NAME = 'Subhomoy'
    WAKE = ["hey lex","wake up"]
    EXIT =["go offline"]
    TITLE = str(gender_age())
    if str(authentication()) == 'unlocked':
        while True:
            command = take_command()
            for phrase in WAKE:
                if phrase in command :
                    run()

            for phrase in EXIT:
                if phrase in command:
                    sys.exit()
