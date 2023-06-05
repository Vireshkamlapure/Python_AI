# from email.mime import audio
# from http import server
# from unittest import result
# from pip import main

from datetime import *
import pyttsx3 
import speech_recognition as sr 
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    #setting audio of the speech 
    engine.say(audio)
    engine.runAndWait() 


def wishMe():
    #telling time and wishing at the start of program 
    hour = int(datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Aftrernoon")
    else:
        speak("Good evening")

    speak("I am jarvis sir . Please tell me how may i help you")


def takeCommand():
    #Taking the microphone input from user and return output 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        print("Said that again ")
        return"None"

    return query 

def sendEmail(to,content):
    #this function is used to send email 
    server = smtplib.SMTP("smtp.gmail.com",587)
    try:
        file = open("File1.txt","r")
        passcode = file.read()
        # print(passcode)
        file.close()
    except Exception as e:
        print(e)
    server.ehlo()
    server.starttls()
    server.login("vireshkamlapure7@gmail.com",passcode)
    server.sendmail('vireshkamlapure7@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    # speak("Harry is good boy and viraj is also good boy")
    wishMe()
    # while True:
        # query = takeCommand().lower()
    query="email to viresh".lower()
        #Logic for executing takes based on query 
    if 'wikipedia' in query:
        speak("Searching wikipedia...")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=3)
        speak("Accoeding to wikipedia")
        print(result)
        speak(result)

    
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open github' in query:
        webbrowser.open("github.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        Music_dir = "E:\\MUSIC"
        songs = os.listdir(Music_dir)
        print(songs)
        os.startfile(os.path.join(Music_dir,songs[0]))

    elif 'play video' in query:
        Video_dir = "E:\\Movies"
        video = os.listdir(Video_dir)
        # print(video)
        os.startfile(os.path.join(Video_dir,video[0]))

    elif 'the time' in query:
        strtime = datetime.now().strftime("%H:%M:%S")
        print(f"The Time is {strtime}")
        speak(f"sir the time is {strtime}")

    elif 'open code' in query:
        code_path = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
    
    elif "email to viresh" in query:
        try:
            speak("What should i said??")
            content = "Hello this is my program "
            # content = takeCommand()
            to = "vireshdiploma7@gmail.com"
            sendEmail(to,content)
        except Exception as e :
            print(e)
            speak("Sorry brother but i am not able to send this Email")

    elif 'quit' in query:
        exit()

        