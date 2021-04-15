#import all the libraries...
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechrecognition
import wikipedia #pip install wikipedia
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import pyautogui #pip install pyautogui
import json #pip install json
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
from urllib.request import urlopen
import wolframalpha #pip install wolframalpha
from requests import get
import pywhatkit as kit #pip install pywhatkit
import PyPDF2 #pip install PyPDF2
from playsound import playsound #pip install playsound
import speedtest #pip install speedtest-cli
import pywhatkit #pip install pywhatkit
import phonenumbers #pip install phonenumbers
import webbrowser
import time
import random
import os
import datetime
import sys

sayed = pyttsx3.init('sapi5')
voices = sayed.getProperty('voices')
sayed.setProperty('voice',voices[1].id)
sayed.setProperty('rate',180)

#text to speech
def speak(audio):
    sayed.say(audio)
    print(audio)
    sayed.runAndWait()

#show date
def telldate():
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    year = datetime.datetime.now().year
    speak(f'The Date Is : {month}-{date}-{year}')

#show which day
def tellday():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'} 

    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        speak(f'Today Is : {day_of_the_week}') 

#to wish us
def wishus():
    speak("Assalamu Alaikum Tetra S..Happy To See You..")
    speak("How Are You Tetra S??")
    OurCommand()
    speak("I Am Fine As Always..")
    #speak("Shall I Start Our Project Tetra S??")
    #OurCommand()
    telldate()
    tellday()
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:
        speak(f"Good Morning Tetra S!! It's : {tt}")
        speak("Plase Wake Up..It's Already Morning..")
        OurCommand()
        speak("Have You Done Your Breakfast??")
        OurCommand()
        speak("Have You Any Classes Today??")
        OurCommand()

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Tetra S!! It's : {tt}")
        speak("Have You Done Your Lunch??")
        OurCommand()
        speak("How Is Your Day Going Till Now..")
        OurCommand()

    else:
        speak(f"Good Evening Tetra S!! It's : {tt}")
        #speak("Have You Done Your Dinner??")
        #OurCommand()
        #speak("Have You Done Your Today's Preparation??")
        #OurCommand()
    
    #speak("Don't Worry Tetra S..")
    speak("I Am Always Here For You To Listen..Please Tell Me How Can I Help You!!")
    #OurCommand()
    #speak("Yes, Of Course..")

#to convert voice into text
def OurCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I Am Listening Tetra S..")
        r.pause_threshold = 1
        audio = r.listen(source)#timeout=4,phrase_time_limit=7

    try:
        print("Please Wait Few Moments For Recognising Your Command..")
        query = r.recognize_google(audio, language='en-US')
        print(f'We Said : {query}')

    except Exception as e:
        print(e)
        return "None"
    
    query = query.lower()
    return query

#take screenshots for us
def screenshot():
    speak("Tetra S, Please Tell Me The Name For This File..")
    name = OurCommand()
    speak("Please Tetra S Hold The Screen..I Am Taking Picture Of This File..")
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f'C://Users//User//Desktop//{name}.png')
    speak("Done Tetra S, You Can Check Now..")

#tell cpu condition for our pc
def cpu():
    usage = str(psutil.cpu_percent())
    speak(f'CPU Is At : {usage}')

#telling jokes for entertainning
def joke():
    speak(pyjokes.get_joke())

#reading a pdf for us
def pdf_reader():
    book = open('D://Object Oriented Programming II//(Week-2) Introduction//Lecture 1 - Introduction to Python.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f'Total Number Of Pages In This Book : {pages}')
    speak(f'Enter The Page Number That You Want Me To Read')
    pg = int(input("Please Enter The Page Number : "))
    p = pdfReader.getPage(pg)
    text = p.extractText()
    speak(text)

#sending message
def message():
    speak("Tell Me The Name Of The Person Tetra S..")
    name = input()

    if 'talha' in name:
        speak("Tell Me The Message..")
        msg = OurCommand()
        speak("Tell Me The Time In Hour..")
        hour = int(OurCommand())
        speak("Tell Me The Time In Minutes..")
        minu = int(OurCommand())
        pywhatkit.sendwhatmsg("+8801521-569361",msg,hour,minu,15)
        speak("Okay Tetra S, Sending The Message In Behalf Of You..")

#execution steps
def OurExecution():
    speak("Initializing Project Tetra S")
    wishus()
    while True:
        #all commands will be stored in lower case in query for easy recognition
        query = OurCommand()

        #logic building for tasks
        if 'set alarm' in query:
            speak("Tetra S Please Tell The Time To Set Alarm..")#set alarm to 12.01 p.m.
            time = input("Enter The Time : ")
            while True:
                hour = datetime.datetime.now()
                tt = hour.strftime("%I:%M:%S")
                
                if tt == time:
                    speak("Time To Wake Up Tetra S..")
                    playsound('Wake Up Alarm Sound Mp3 Ringtone Download.mp3')
                    speak("Alarm Closing For Now Tetra S..")
                
                elif tt > time:
                    break
        
        elif 'open command prompt' in query:
            os.system("start cmd")

        if 'open notepad' in query:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press("volumemute")

        elif 'wikipedia' in query:
            speak("Searching That You Want..")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=3)
            speak('According To Wikipedia..')
            speak(result)

        elif 'open code' in query:
            codepath = "C://Users//User//AppData//Local//Programs//Microsoft VS Code//Code.exe"
            os.startfile(codepath)
            speak("Openning Visual Studio Code For You..")

        elif 'close code' in query:
            os.system('TASKKILL /F /IM Code.exe')
            speak("Closed Visual Studio Code..")

        elif 'open chrome' in query:
            chromepath = "C://Program Files//Google//Chrome//Application//chrome.exe"
            os.startfile(chromepath)
            speak("Openning Google Chrome For You..")

        elif 'close chrome' in query:
            os.system('TASKKILL /F /IM chrome.exe')
            speak("Closed Google Chrome..")

        elif 'open telegram' in query:
            telegrampath = "C://Users//User//AppData//Roaming//Telegram Desktop//Telegram.exe"
            os.startfile(telegrampath)
            speak("Opening Telegram For You..")

        elif 'close telegram' in query:
            os.system('TASKKILL /F /IM Telegram.exe')
            speak("Closed Telegram..")

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'search in chrome' in query:
            speak("What Should I Search In Chrome For You??")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = OurCommand()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search youtube' in query:
            speak("What Should I Search In YouTube For You??")
            search_term = OurCommand()
            speak("Here we Go To YouTube Tetra S..")
            wb.open('https://www.youtube.com/results?search_query='+search_term)

        elif 'search google' in query:
            speak("What Should I Search In Google For You??")
            search_term = OurCommand()
            speak("Searching Your Desired Destination..")
            wb.open(f"{search_term}")

        elif 'send unlimited message' in query:
            import time
            while True:
                time.sleep(3)
                pyautogui.typewrite("Hello, How Are You??")
                pyautogui.press('enter')

        elif 'send message' in query:
            message()

        elif 'cpu' in query:
            cpu()

        elif 'countdown' in query:
            import time
            speak("Enter Time In Seconds..")
            t = int(OurCommand())
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end = "\r")
                time.sleep(1)
                t -= 1
            speak("Timer Completed..")
        
        elif 'number' in query:
            speak("Enter The Phone Number..")
            number = input()
            from phonenumbers import geocoder
            ch_number = phonenumbers.parse(number, "CH")
            say = geocoder.description_for_number(ch_number, "en")
            speak(f'The Location Is : {say}')
            from phonenumbers import carrier
            service = phonenumbers.parse(number, "RO")
            tal = carrier.name_for_number(service, "en")
            speak(f'The Operator Is : {tal}')
        
        elif 'open stackoverflow' in query:
            wb.open("stackoverflow.com")

        elif 'tell a joke' in query:
            joke()
        
        elif 'write a note' in query:
            speak('What Should I Write Tetra S??')
            notes = OurCommand()
            file = open('notes.txt','w')
            speak("Tetra S, Should I Include Date and Time In Your NoteBook??")
            ans = OurCommand()

            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done Taking Notes For You Tetra S..")

            else:
                file.write(notes)
        
        elif 'showing note ' in query:
            speak('The Notes Are..')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())
        
        elif 'take screenshot' in query:
            screenshot()

        elif 'read pdf' in query:
            pdf_reader()
        
        elif 'play music' in query:
            songs_dir = "F:\\New folder"
            music = os.listdir(songs_dir)
            rd = random.choice(music)
            os.startfile(os.path.join(songs_dir,rd))

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'Your IP Address is {ip}')

        elif 'play songs on youtube' in query:
            kit.playonyt("Obhiman Bangla Song")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif 'remember that' in query:
            speak("What Should I Remember??")
            memory = OurCommand()
            speak("Okay Tetra S I'll Do It For You.."+memory)
            remember = open("memory.txt",'w')
            remember.write(memory)
            remember.close()
        
        elif 'remember anything' in query:
            remember = open("memory.txt",'r')
            speak("You Asked Me To Remember That : "+remember.read())

        elif 'tell me news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ce290361dbf2486fb4375584f78e141c")
                data = json.load(jsonObj)
                i = 1
                speak ('Here Are Some Top Headlines..')
                print("##========Top Headlines=====##")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))
        
        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("You Asked Me To Locate "+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
            """
        elif 'where i am' in query or 'where we are' in query:
            speak("Wait Tetra S, Let Me Check For You")
            speak("Remember Tetra S It Is Not The Exact Location..It Is Approximate Location")
            OurCommand()
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f'Probably You Are In {city} City Of {country} Country')
            except Exception as e:
                speak("Sorry Tetra S!!Due To Network Issue I Am Not Able To Find Your Location..")
                pass"""

        elif 'calculate' in query:
            client = wolframalpha.Client('7RT8K6-JT8U2Y7EJ7')
            query = str(input("Query : "))
            #query = OurCommand()
            res = client.query(query)
            answer = next(res.results).text
            speak("The Answer Is : "+answer)

        elif 'internet speed' in query:
            speak("Calculating Internet Speed..")
            speak("Please Wait For Few Monments..")
            dd = speedtest.Speedtest()
            downl = dd.download()
            upl = dd.upload()
            speak(f"Tetra S In Your Pc You Have {downl} bps Download Speed..")
            speak(f"Tetra S In Your Pc You Have {upl} bps Upload Speed..")

        elif 'stop listening' in query:
            speak('How Many Seconds You Want Me To Stop Listening To Your Commands Tetra S..')
            ans = int(OurCommand())
            time.sleep(ans)
            print(ans)

        elif 'sleep now' in query:
            speak("Okay Tetra s, I Am Going To Sleep..")
            speak("You Can Call Me Anytime..")
            OurCommand()
            speak('Pleasure Is Always Mine..')
            break

#main function
if __name__ == "__main__":
    while True:
        tal = OurCommand()
        if 'wake up' in tal:
            OurExecution()
        
        elif 'goodbye' in tal:
            speak("Thanks For Using Me Tetra S, Have A Good Day Tetra S..")
            sys.exit()