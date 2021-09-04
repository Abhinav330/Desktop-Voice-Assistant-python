import pyttsx3
import datetime
import speech_recognition as sr
import time
import wikipedia
import webbrowser
import os
import random
import smtplib
from selenium import webdriver
import selenium
import serial

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)  # choose the voice accodingly 
#print(voices[0].id)
#print(voices[1].id)
#print(voices[2].id)
#print(voices[3].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    time.sleep(2)
    if hour >= 0 and hour <= 12:
        speak("Good morning! sir")
    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon! sir")        
    else :
        speak("Good Evening! sir")
   
    speak(" i am jarvis")             #change the name of your voice assistant
    speak("how can i help you ")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listning")
        r.pause_threshold = 0.8
        r.energy_threshold = 300 
        audio = r.listen(source)

    try:
        print("finding....")
        query = r.recognize_google(audio ,language ='en-IN')
        print("User said", query )
        
       
    
    except Exception as e:
        print(e)
        print("say that again please")
        #speak("say that again please")
        
        return "None"
               
    return query
 
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    con = ""                                                # password of your mail id
    server.ehlo()
    server.starttls()
    server.login('jharkhand30@gmail.com',con)               # your  mail id    
    server.sendmail('jharkhand30@gmail.com' , to , content)   # mail id of the person to whome you want to send the mail.
    server.close()

def schedule() :
    x = datetime.datetime.now()
    if x.strftime("%H") == "14" and x.strftime("%M") == "10" :
        speak("Initiating user's set alarm for ")
        speak(x.strftime("%X"))
        speak("Sir!  you should wash your face")
        time.sleep(5) 
        speak("Sir!  you should wash your face")
        time.sleep(20)

if __name__ == "__main__":
    greet()
    while True:
        schedule()
        
        query = takeCommand().lower()
         

        if 'wikipedia' in query :
            speak("searching wikipedia")
            query = query.replace("wikipedia" ,"" )
            results = wikipedia.summary(query, sentences = 2 )
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' == query or 'youtube kholo' in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")
        elif 'open google' in query or 'google kholo' in query:
            speak("opening google")
            webbrowser.open("www.google.com")
        #elif 'hi'  in query or 'how are you' == query or 'kaise ho' == query:
            #speak("hello sir i am fine")

        elif 'open attendance' in query:
            speak("opening  iemcrp")
            webbrowser.open("www.iemcrp.com")    
        elif 'open mail' in query or 'mel kholo' in query:
            webbrowser.open("https://mail.google.com/mail/u/2/#inbox")
        elif 'who are you' in query  or 'tum kaun ho' in query or 'kaun ho tum' in query :
            speak('''I am jarvis 1.0 , developed by Mr. Abhinav. Right now i am in development phase so i can only do following things .
            i can search in wikipedia. i can open web browsers .i can open applications  ,i  can tell you the time and i can send email and play musics.
            soon i will be upgraded with more features . stay tuned for more ''')
            # change the intro of your voice assistant.
            
        elif 'wish me luck' in query:
            speak("congratulations sir ")
        elif'play music' in query :
            music_dir = 'C:\\Users\\abhinav\\Music' # path of your music directory (change accordingly)
            songs = os.listdir(music_dir)
            #print(songs)
            ll = random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir , songs[ll]))
        elif'the time' in query  or 'time kya ho raha hai' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,the time is {strTime}")
        elif'open code' in query or 'code kholo' in query:
            codepath ="C:\\Users\\abhinav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif'open whatsapp' in query or 'whatsapp kholo' in query:
            wpath = "C:\\Users\\abhinav\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(wpath)   
        elif 'send email' in query or 'email bhejo' in query:
            try:
                speak("ok . What shoud i do ")
                content = takeCommand()
                to = "abhinav33303@gmail.com"
                sendEmail(to , content)
                speak("Email has been send")

            except Exception as e :
                print(e)
                speak("sorry Not able to send this Mail.")
        elif 'exit' in query or 'band ho jao' in query :
            speak("thank you sir for using me . Jarvis 1.o signing out")
            break
        elif 'lollipop bajao' in query:
            music_dir = 'C:\\Users\\abhinav\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir , songs[12]))
        elif 'on youtube' in query :
            driver = webdriver.Chrome()
            
            driver .get('https://www.youtube.com/')
            remove = ['search', 'on', 'youtube']   
            for i in remove : 
                query = query.replace(i, '')
            print(query)    
            searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
            searchbox.send_keys(query)
            search = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
            search.click()
