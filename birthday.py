from speech import *
import sys
import datetime
import webbrowser
import time
import os
import pyjokes
import psutil
import platform

a=sys.argv[1]

def jokes():
    speak(pyjokes.get_joke())

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at"+ str(battery.percent))
    # speak(battery.percent )

def wishMe(name):
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
        speak("Good Morning"+ str(name))

    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ str(name))

    elif hour>=18 and hour<24:
        speak("Good Evening"+ str(name))

    else:
        speak("Good Night"+ str(name))

    speak("THOR at your Service. Please tell me how can I help You ")


def run():
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
        speak('I am THOR version 1 point O' +str(a)+ 'persoanl assistant.')
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
    elif 'go offline' in command:
        speak("ok sir shutting down the system")
        quit()



if __name__ == '__main__':
    
    wishMe(a)
    while True:
        run()