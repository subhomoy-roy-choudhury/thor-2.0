import speech_recognition as sr
import pyttsx3
from gender_age import gender_age
from emotion_func import emotion

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
t = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','ten':'10'}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def talk(message):
    speak(message)
    print(message)

def take_command():
    try:
        title = str(gender_age())
        emotion1 = str(emotion())
        print(emotion1)
        if emotion1 == 'Angry' or emotion1 == 'Sad':
            talk(f'Are you {emotion1} {title}')
        elif emotion1 == 'Surprise' or emotion1 == 'Happy':
            talk(f'Are you {emotion1} {title}')
        elif emotion1 == 'Neutral' :
            talk('hiii sir')
        with sr.Microphone() as source:
            talk('listening '+ str(title) +'...')
            listener.pause_threshold = 1
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'thor' in command:
                command = command.replace('thor', '')    
            for keys,value in t.items():
                if keys in command:
                    command = command.replace(keys,value)
            print('this is the '+str(command))
            #return command
    except Exception as e:
        print(e)    
        talk(f"Say that again please {title}...")  
        return "None"
    return command
    
def float_input(msg):
    try:
        talk(msg)
        command=take_command()
        if (command is None):
            return None
        command=float(command)
        print(type(command))
        talk("The input is " + str(command))
        return command
    except Exception as e:
        # print(e)
        talk(" please...")  

    

def gender_input(msg):
    try:
        talk(msg)
        patient_gender=take_command()
        if patient_gender is None:
            return None
        if patient_gender=='female':
            patient_gender=1
            print(type(patient_gender))
            talk("The input is Female")
        elif 'male' or 'mail' in patient_gender:
            patient_gender=0
            print(type(patient_gender))
            talk("The input is Male")
        return patient_gender
    except Exception as e:
        talk("gender please...")  



if __name__ == '__main__':
    x=take_command()
    num = float_input(x)
    talk("The input is " + str(num))

