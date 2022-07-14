import pyttsx3,datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randrange

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("добрый вечер!")

    speak("How can I Help You?")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='ru')
        print("You Said : ",query)

    except Exception as e:
        print("Say that again please....")
        return 'None'

    return query


def jokes():
    response = ["Циля, забери своего бесстыжего кота. Он опять изображал голодный обморок у рыбного отдела.",
                "Хожу к стоматологу, ставят обезболивающее, чтоб с деньгами не больно было расставаться."
                ][
        randrange(2)]
    return response

def quote():
    response = ["«Чем умнее человек, тем легче он признает себя дураком». Альберт Эйнштейн",
                "«Никогда не ошибается тот, кто ничего не делает». Теодор Рузвельт",
                "«Менее всего просты люди, желающие казаться простыми». Лев Николаевич Толстой"
                ][
        randrange(3)]
    return response

















if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        
        
        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)
            
        elif 'open google' in query:
            query=query.replace('open',"")
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            query=query.replace('open',"")
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            pass
        
        elif 'скажи' and 'время' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak("Время")
            speak(strTime)
            
        elif 'open code' in query:
            codepath="C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open firefox' in query:
            path1="C:\Program Files\Mozilla Firefox\firefox.exe"
            os.startfile(path1)

        elif 'open chrome' in query:
            path2="C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(path2)

        elif 'open setting' in query:
            path3="%windir%\System32\Control.exe"
            os.startfile(path3)


        elif 'open bluestacks' in query:
            path4="C:\Program Files\BlueStacks_nxt\HD-Player.exe --instance Nougat32"
            os.startfile(path4)

        elif 'шутка' or 'скажи' and 'шутку' in query:
            speak(jokes())

        elif 'цитата' or 'скажи' and 'цитату' in query:
            speak(quote())

        else : 
            print("Didn't recognized! Please say it again...")
            takeCommand()