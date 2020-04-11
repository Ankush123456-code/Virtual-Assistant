import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from PIL import ImageGrab
import webbrowser
import random,os
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
info=['I am cortona, a simple but efficient virtual assistant made by Ankush who is  20 year old programmer in the epidemic of covid 19 of 2020']
#print(voices[0])
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour <12:
        speak("good morning") 
    elif hour>=12 and hour<=18:
        speak("good evening")  
    else:
        speak("good evening")

    speak("i am your assistant please tell me how may i help you sir")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)



    try:
        print('Reconizing..')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        speak("say that again please.....")
        return "none"
    return query
def time(data):
    current=datetime.datetime.now().strftime("%H:%M:%S")
    engine.say("The current time is "+current)



def ss():
    speak("taking screenshot")
    name=random.randint(1000,300000)
    time.sleep(5)
    ImageGrab.grab().save("screenshot"+str(name),"JPEG")
    speak("screenshot saved"+name)

def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.login('youremail@gmail.com','your password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()



if __name__ =="__main__":
    wishme()
    #while True:
    if 1:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia',"")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            speak('opening sir...')
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak('opening sir...')
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak('opening sir...')
            webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
            speak('opening sir...')
            webbrowser.open("facebook.com")
        elif 'open github' in query:
            speak('opening sir...')
            webbrowser.open('github.com')
            
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        elif 'who are you' in query:
            speak(info)
        elif 'take Screenshot' in query:
            speak("screenshot is taking"+ss())
           

        elif 'send email to ankush' in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to="ankushkumar1840@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                speak("sorry my friend Ankush bhai. no internet connection")



