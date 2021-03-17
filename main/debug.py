import speech_recognition as sr
import pyttsx3
from recording import predict

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def talk(message):
    speak(message)
    print(message)


# try:
with sr.Microphone() as source:
    talk('listening...')
    listener.pause_threshold = 1
    listener.adjust_for_ambient_noise(source)
    voice = listener.listen(source)
    with open("test.wav",'wb') as f:
        fs = 44110              # use "test.wav" as the audio source
        f.write(voice.get_wav_data(),fs) 
        if str(predict('test.wav')) =='subho':
            print('yes')
    command = listener.recognize_google(voice, language='en-in')
    command = command.lower()
    if 'thor' in command:
        command = command.replace('thor', '')    
    print('this is the '+str(command))
        #return command
# except Exception as e:
#     # print(e)    
#     talk("Say that again please...")  
#     print('None') 