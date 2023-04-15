import datetime
import pyttsx3
import pyautogui
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import random
import playsound
import requests
import json
import imp
url = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=47ac9a7696c3418db41215900b790366'
read00 = requests.get(url=url).text
view00 = json.loads(read00)
data00 = view00["articles"]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
p=str(datetime.datetime.now().date())
d=p.split("-")[0]
m=p.split("-")[1]
y=p.split("-")[2]
m.split("0")

import time
timestamp = int(time.strftime('%H'))
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am moon. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold=300
        audio = r.listen(source)
        # r.energy_threshold = 3

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(subj, content, to):
    pywhatkit.send_mail(email_sender="krishnatanna41@gmail.com", password=imp.google_p["password"], subject=subj,
                        message=content, email_receiver=to)

if __name__ == "__main__":
    # callme()
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("oops somthing went wrong")
        elif "increase voice" in query:
            speak("done")
            pyautogui.press("volumeup")
        elif "decrease voice" in query:
            speak("done")
            pyautogui.press("volumedown")
        elif "mute" in query:
            speak("done")
            pyautogui.press("volumemute")
        elif "unmute" in query:
            speak("done")
            pyautogui.press("volumeunmute")
        # elif "back" in query:
        #     speak("done")
        #     pyautogui.press("backspace")
        elif "current location" in query:
            speak("opening google maps")
            webbrowser.open("https://www.google.com/maps")
        elif "ip address" in query:
            k = requests.get("https://api.ipify.org").text
            print(k)
            speak(k)
        elif "screenshot" in query:
            speak("okay! by what name should i save screenshot.")
            name=takeCommand()
            pywhatkit.take_screenshot(name, delay=2)
        elif "gana bajao" in query:
            speak("opening youtube.txt")
            pywhatkit.playonyt("hanuman chalisa")
        elif "send whatsapp message" in query:
            try:
                speak("what is receivers number")
                phone = takeCommand()
                print(f"is it correct {phone} if NO so please type number below or number is correct then press ENTER.")
                speak(f"is it correct {phone} if NO so please type number below or number is correct then press ENTER.")
                p=input("type here:")
                if p==None:
                    pass
                else:
                    phone=p
                speak("what is the message?")
                message = takeCommand()
                pywhatkit.sendwhatmsg_instantly(phone_no=(f"+91{phone}"), message=message, wait_time=15, tab_close=False, close_time=3)
            except Exception as e:
                print(("OOPS! something went wrong."))
                speak("OOPS! something went wrong.")
        elif 'open youtube.txt' in query:
            speak("opening youtube.txt")
            webbrowser.open("youtube.txt.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            try:
                speak("opening pycharm")
                codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3\\bin\pycharm64.exe"
                os.startfile(codePath)
            except Exception as e:
                speak("OOPS! something went wrong")
                print("OOPS! something went wrong")

        elif 'open chrome' in query:
            try:
                speak("opening chrome")
                codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)
            except Exception as e:
                speak("OOPS! something went wrong")
                print("OOPS! something went wrong")
        elif "search" in query:
            st = query.replace("search", " ")
            speak("searching...")
            webbrowser.open(f"https://www.google.com/search?q={st}")
        elif 'send email' in query:
            try:
                speak("what is receivers email id?")
                # to = input("Type here.\n")
                to = takeCommand()
                print(f"is it correct {to} if NO so please type number below or number is correct then press ENTER.")
                speak(f"is it correct {to} if NO so please type number below or number is correct then press ENTER.")
                t = input("type here:")
                if t == None:
                    pass
                else:
                    to = p
                speak("What is Subject")
                print("What is Subject?")
                subj = takeCommand()
                speak("What is content")
                print("What is content?")
                content = takeCommand()
                sendEmail(subj=subj, content=content, to=to)

                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("OOPS! something went wrong.")

        elif "what" in query:
            if "your age" in query:
                if d == "2023":
                    if int(m) > 1:
                        k = 1 - int(m)
                        k = k + int(m)
                        speak(f"i am {k} month old")
                    else:
                        cd = int(y) - 1
                        speak(f"i am {cd} days old")
                else:
                    if d > "2023":
                        speak(f"I am {int(d) - 2023} years old.")
            elif "your name" in query:
                speak("My name is moon")
            else:
                qu = query.replace(" ", "+")
                speak("searching...")
                webbrowser.open(f"https://www.google.com/search?q={qu}")
        elif "play" in query:
            qu = query.replace(" ", "+")
            speak("opening youtube.txt")
            pywhatkit.playonyt(qu)
        elif "how" in query:
            if "old" in query:
                if d == "2023":
                    if int(m) > 1:
                        k = 1 - int(m)
                        k = k + int(m)
                        speak(f"i am {k} month old")
                    else:
                        cd = int(y) - 1
                        speak(f"i am {cd} days old")
                else:
                    if d > "2023":
                        speak(f"I am {int(d) - 2023} years old.")
            else:
                qu = query.replace(" ", "+")
                speak("searching...")
                webbrowser.open(f"https://www.google.com/search?q={qu}")
        elif "why" in query:
            qu = query.replace(" ", "+")
            speak("searching...")
            webbrowser.open(f"https://www.google.com/search?q={qu}")
        elif "who" in query:
            if "developed" in query:
                speak("I'm developed by krishna and my first version was released on 1 january 2023")
            else:
                qu = query.replace(" ", "+")
                speak("searching...")
                webbrowser.open(f"https://www.google.com/search?q={qu}")
        elif "which" in query:
            if "language" in query:
                speak("Kindly contact developer.")
            else:
                qu = query.replace(" ", "+")
                speak("searching...")
                webbrowser.open(f"https://www.google.com/search?q={qu}")
        # elif "hindi" in query:
        #     speak("namaste")
        # elif "gujarati" in query:
        #     speak("Mane Gujarati nathi Avadh Tu")
        elif "bored" in query or "start game" in query or "play game" in query or "boring" in query or "lets play game" in query:
            speak("ok lets have some fun ")
            speak("lets play game snake,gun,water")
            start = 0
            limit = 10
            my_point = 0
            bot_point = 0
            bot = ["Gun", "Snake", "Water"]
            print("Choice anyone:-", "Gun", "Snake", "Water")
            while start < limit:
                speak("choice anyone - Gun or Snake or Water")
                input1 = takeCommand().capitalize()
                botselect = random.choice(bot)
                if input1 == "Gun":
                    start = start + 1
                    if "Gun" in botselect:
                        print(input1, ",", botselect)
                        print("Game tie")
                        speak("Game tie")
                        my_point = my_point + 0
                        bot_point = bot_point + 0
                        print("No. of chance left-", 10 - start)
                        print("Your point-", my_point, "and bot point-", bot_point)
                    elif "Snake"in botselect:
                        print(input1, ",", botselect)
                        print("You won")
                        speak("You won")
                        playsound.playsound("C:\\Users\\krish\\Downloads\\flappy\gallery\\audio\\point.wav")
                        my_point = my_point + 1
                        bot_point = bot_point + 0
                        print("No. of chance left-", 10 - start)
                        print("Your point-", my_point, "and bot point-", bot_point)
                    else:
                        print(input1, ",", botselect)
                        print("Bot won")
                        speak("Bot won")
                        playsound.playsound("C:\\Users\\krish\\Downloads\\flappy\gallery\\audio\hit.wav")
                        playsound.playsound("C:\\Users\\krish\\Downloads\\flappy\gallery\\audio\\die.wav")
                        my_point = my_point + 0
                        bot_point = bot_point + 1
                        print("No. of chance left-", 10 - start)
                        print("Your point-", my_point, "and bot point-", bot_point)
                elif input1 == "Snake":
                    start = start + 1
                    if "Snake" in botselect:
                        print(input1, ",", botselect)
                        print("Game tie")
                        speak("Game tie")
                        my_point = my_point + 0
                        bot_point = bot_point + 0
                        print("No. of chance left-", 10 - start)
                        print("Your point-", my_point, "and bot point-", bot_point)
                    elif "Gun" in botselect:
                        print(input1, ",", botselect)
                        print("Bot won")
                        speak("Bot won")
                        playsound.playsound("C:\\Users\\krish\\Downloads\\flappy\gallery\\audio\hit.wav")
                        my_point = my_point + 0
                        bot_point = bot_point + 1
                        print("No. of chance left-", 10 - start)
                        print("Your point-", my_point, "and bot point-", bot_point)
                    else:
                        print(input1, ",", botselect)
                        print("You won")
                        speak("You won")
                        playsound.playsound("C:\\Users\\krish\\Downloads\\flappy\gallery\\audio\\point.wav")
                        my_point = my_point + 1
                        bot_point = bot_point + 0
                        print("No. of chance left-", 10 - start)
                        print("Your point-", my_point, "and bot point-", bot_point)
                elif "Water"in botselect:
                    start = start + 1
                    if "Water" in botselect:
                        print(input1, ",", botselect)
                        print("Game tie")
                        speak("Game tie")
                        my_point = my_point + 0
                        bot_point = bot_point + 0
                        print("No. of chance left-", 10 - start)
                        print("Your point-", my_point, "and bot point-", bot_point)
                    elif "Snake"in botselect:
                        print(input1, ",", botselect)
                        print("Bot won")
                        speak("Bot won")
                        playsound.playsound("C:\\Users\\krish\\Downloads\\flappy\gallery\\audio\hit.wav")
                        my_point = my_point + 0
                        bot_point = bot_point + 1
                        print("No. of chance left-", 10 - start)
                        print("Your point-", my_point, "and bot point-", bot_point)
                    else:
                        print(input1, ",", botselect)
                        print("You won")
                        speak("You won")
                        playsound.playsound("C:\\Users\\krish\\Downloads\\flappy\gallery\\audio\\point.wav")
                        my_point = my_point + 1
                        bot_point = bot_point + 0
                        print("No. of chance left-", 10 - start)
                        print("Your point-", my_point, "and bot point-", bot_point)
                else:
                    start = start - 1
                    print("OOPS! something went wrong")
                    speak("OOPS! something went wrong")
                if start == limit:
                    print("Game Over")
                    speak("Game Over")

                print("Your total score is ", my_point, "Bot total score is ", bot_point)
                speak(f"Your total score is {my_point} Bot total score is  {bot_point}")
            if my_point > bot_point:
                print("Congratulations, you won.")
                speak("Congratulations, you won.")
            elif my_point < bot_point:
                print("Better luck next time.")
                speak("Better luck next time.")
            elif my_point >= bot_point:
                print("Game tie.")
                speak("Game tie.")
        elif "yourself" in query:
            speak("myself moon assistant i am developed by krishna on 1 january 2023.")
        elif "jay shri ram" in query:
            speak("jai shri ram")
        elif "hare krishna" in query:
            speak("hare krishna")
        elif "jay bajrangbali" in query:
            speak("jai bajrangbali")
        elif "jay shri krishna" in query:
            speak("jai shri krishna")
        elif "jay hanuman" in query:
            speak("jai hanumanji")
        elif query=="exit":
            speak("thank you for using our service have a good day.")
            break
        elif "read news" in query:
            if timestamp in range(00, 11):
                speak("good morning ")
            elif timestamp in range(12, 16):
                speak("good afternoon sir")
            elif timestamp in range(17, 23):
                speak("good evening sir")
                speak(f"todays headline is")

            for artic in data00:
                speak({artic['title']})
                print(artic['title'])
                speak("Now next news is")
        elif "shutdown" in query:
            speak("device will shut down in 20 seconds to cancel shutdown say cancel")
            pywhatkit.shutdown(time=20)
        elif query=="cancel":
            pywhatkit.cancel_shutdown()
            speak("Done")
        elif "message" in query:
            try:
                speak("what is receivers number")
                phone = takeCommand()
                print(f"is it correct {phone} if NO so please type number below or number is correct then press ENTER.")
                speak(f"is it correct {phone} if NO so please type number below or number is correct then press ENTER.")
                p=input("type here:")
                if p==None:
                    pass
                else:
                    phone=p
                speak("what is the message?")
                message = takeCommand()
                pywhatkit.sendwhatmsg_instantly(phone_no=(f"+91{phone}"), message=message, wait_time=15, tab_close=False, close_time=3)
            except Exception as e:
                print(("OOPS! something went wrong."))
                speak("OOPS! something went wrong.")
        elif 'mail' in query:
            try:
                speak("what is receivers email id?")
                print("what is receivers email id?")
                to = takeCommand()
                print(f"is it correct {to} if NO so please type number below or number is correct then press ENTER.")
                speak(f"is it correct {to} if NO so please type number below or number is correct then press ENTER.")
                p = input("type here:")
                if p == None:
                    pass
                else:
                    phone = p
                speak("What is Subject")
                print("What is Subject?")
                subj = takeCommand()
                speak("What is content")
                print("What is content?")
                content = takeCommand()
                sendEmail(subj=subj, content=content, to=to)

                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("OOPS! something went wrong.")
        elif "" in query:
            pass
        else:
            speak("OOPS! something went wrong.")
            pyautogui.alert("OOPS! something went wrong.")






