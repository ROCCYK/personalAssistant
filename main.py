import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', ' ')
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print (command)
    if 'play' in command:
        song = command.replace('play', ' ')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        time = time.replace(':', ' ')
        talk('current time is' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', ' ')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'best in rainbow' in command:
        talk('richard is the best in rainbow')
    elif 'biggest ben chode' in command:
        talk('michael is the biggest ben chode')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Pardon me sir kindly repeat that')
while True:
    run_jarvis()