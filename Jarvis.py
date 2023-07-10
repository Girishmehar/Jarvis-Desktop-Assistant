import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'Jarvis' in command:
                command = command.replace('jarvis','')
                print(command)

    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)

    elif 'who the heck is ' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a meeting.')
    elif 'are you single' in command:
        talk('Iam in a relationship with wifi.')
    elif 'why are you so cute ' in command:
        talk('Thank you so much for your kind word')
    elif 'what is my full name' in command:
        talk('Your full name is Girish Raj Meena')
    elif 'I am from ' in command:
        talk('You are from Jodhpur')
    elif 'height' in command:
        talk('Your height is 5.10')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'dhela' in command:
        talk('dhela is your sister')
    elif 'fathers' in command:
        talk('Mr Buddh Ram Meena')
    else:
        talk('Please say the command again.')

while True:
    run_jarvis()
