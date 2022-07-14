# Голосовой помощник Хлоя 0.2


import pyttsx3,datetime
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import random
from config import USER_NAME

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Слушаю...")
            r.pause_threshold= 1
            audio=r.listen(source)
        
        try:
            print("Анализ...")
            query=r.recognize_google(audio, language='ru')
            print("Вы сказали : ",query)
    
        except Exception as e:
            print("Повтори....")
            return 'None'
    
        return query




file = open("config.py", "r", encoding="utf-8")
logins = file.read()
if USER_NAME == str('start'):
    speak("Здравствуйте! Меня зовут Хлоя. Как вас зовут?")
    file = open("config.py", "w", encoding="utf-8") # w - write
    query=takeCommand().lower() # слушаем 
    USER_NAME = query.replace("", "") # Возвращает копию строки, в которой заменены все вхождения указанной строки указанным значением.
    file.write(f"USER_NAME = str('{USER_NAME}') ")
    file.close()
    speak("Отлично! Настройка завершена. ")

else:
    def wishMe():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<=12:
            speak("Доброе Утро!")
        elif hour>=12 and hour<18:
            speak("Добрый День!")
        else:
            speak("Добрый Вечер!")
    
        speak("Как я могу вам помочь?")
    
    
    
    def jokes():
        jokes_examples = ["Лично мне клоуны совсем не кажутся смешными. По правде говоря, я их боюсь. Даже не знаю, когда это началось. Наверное, когда меня в детстве повели в цирк и клоун убил моего отца"]
        speak('Окей')
        speak(jokes_examples)
    
    
    if __name__=="__main__":
        wishMe()
        while True:
            query=takeCommand().lower()
    
            if 'открой гугл' in query:
                query=query.replace('отркой',"")
                webbrowser.open("google.com")
    
            elif 'скажи' and 'время' in query:
                strTime= datetime.datetime.now().strftime("%H:%M:%S")
                speak("Время")
                speak(strTime)
    
            elif 'шутка' in query:
                jokes()
    
    
            elif 'открой' and 'Chrome' in query:
                path2="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                os.startfile(path2)
                
            elif 'найди' in query or 'посмотри' in query:
                query = query.replace("найди", "")
                query = query.replace("играть", "")
                webbrowser.open(query)

    
            elif 'стоп' or 'выключись' in query:
                speak("Окей")
                exit()
    
            else : 
                print("...")
                takeCommand()
    
    
    
    
    
    