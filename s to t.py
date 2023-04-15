import time
import translate as t
import speech_recognition as sr
from gtts import gTTS
import os
r = sr.Recognizer()
# time.sleep(5)
print("started")
with sr.Microphone() as source:
    audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        #Uncomment below code if you want to track data user data in txt file.
        # k = open("user ka text.txt", "a")
        # k.write(query)
        # k.close()
        u = input("Do you want to translate it to hindi text? Type Y to continue.").capitalize()
        if "Y" in u:
            k1 = t.Translator(to_lang="hi")
            k2 = k1.translate(query)
            print(k2)
    except Exception as e:
        print(e)


