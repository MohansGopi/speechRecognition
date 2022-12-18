#!/usr/bin/env pypy
import sys
import pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import subprocess as sp
import requests

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
# Set Rate
engine.setProperty('rate', 190)
# Set Volume
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Very Glad to meet you all, My name is Stark, How can i help for you")
print("Very Glad to meet you all, My name is stark, How can i help for you")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def command_take():
        try:
            command = ''
            with sr.Microphone() as Source:
                print("listening....")
                listener.pause_threshold = 1
                listener.adjust_for_ambient_noise(Source, duration=1)
                voice = listener.listen(Source)
                print("recognizing....")
                command = listener.recognize_google(voice)
                command  = command.lower()
                if 'stark' in command:
                        command = command.replace('stark','')
                        print(command)

        except:
            print("some error occur or your connection is low")
        return command
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
def play_jarvis():
    command = command_take()
    if 'yourself' in command or 'tell me about yourself' in command:
        talk("iam the most beautiful personal assistant in the world, And my name is standard trignometry all radar kit, you can all mee stark, since 2022")
    elif 'what is your name' in command or 'your name' in command or 'pronounce your name' in command :
        talk("my name is standard trignometry all radar kit, you can all mee stark ")
    elif 'play' in command or 'youtube' in command:
        song = command.replace('play','')
        pywhatkit.playonyt( song)
    elif 'team' in command or 'team intro' in command:
        var = ['our team mentor is, mahadhevan sir','and our team Leader is Ragunath','vikram','mohan','pradeep','and finally the most beautiful mee, ha haa haa..']
        talk(var)
    elif 'time' in command and 'now' in command or 'what' in command and 'time' in command or 'current time' in command or 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(str(time))
        talk("the current time is " + time)
    elif 'what' in command or 'about' in command or 'what is' in command:
        info = wikipedia.summary(command,2)
        print(info)
        talk(info)
    elif 'who' in command or 'who is' in command:
        info = wikipedia.summary(command,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'open google' in command or 'search about' in command:
        pywhatkit.search(command)
    elif 'camera' in command and 'open' in command:
        sp.run('start microsoft.windows.camera:', shell=True)
    elif 'command prompt' in command or 'cmd' in command and 'open' in command:
        os.system('start cmd')
    elif 'advice' in command and 'give' in command:
        advice = get_random_advice()
        print(advice)
        talk(advice)
    elif 'sleep' in command:
        talk("thank you sir , see you soon")
        sys.exit()
    elif 'alexa' in command or 'siri' in command:
        talk("i hate him , don't talk about him")
    elif 'feel down' in command or 'feel sad' in command or 'feel' in command and 'sad' in command or 'feeling down' in command or 'feeling sad' in command:
        talk("i'm sorry to hear that sir, how can i help for you")
    else:
        print("can't understand , can you repeat it or ask with other pronunciation")
while True:
        play_jarvis()

