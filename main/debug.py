import datetime
import os
from threading import Thread
from multiprocessing import Process
import platform
import gtts
from playsound import playsound

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

def run():
    while True:
        command = str(input('Enter the command :- '))
        for thread in threading.enumerate(): 
            print(thread.name)
        if 'the date' in command:
            # t1 = threading.Thread(target=date, name='t1')
            # t1.start()
            try:
                if p2.is_alive()==True:
                    print('terminate p1')
                    p2.terminate()
                    p1 = Process(target=date ,name='p1')
                    p1.start()
            except:
                p1 = Process(target=date ,name='p1')
                p1.start()
        elif 'who are you' in command or 'what can you do' in command:
            # t2 = threading.Thread(target=system, name='t2')
            # t2.start()
            try:
                if p1.is_alive()==True:
                    print('terminate p1')
                    p1.terminate()
                    p2 = Process(target=system,name='p2')
                    p2.start()

            except:
                p2 = Process(target=system,name='p2')
                p2.start()


if __name__ == '__main__':

    thread = Thread(target=run, name = 'RUN')
    thread.setDaemon(True)  
    print(thread.isDaemon()) 
    thread.start()
    thread.join()   

  