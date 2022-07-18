from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr
import os
import plugin_commands


def listen_command():
    # получить звук с микрофона
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите вашу команду: ")
        audio = r.listen(source)
    # распознавать речь с помощью Google Speech Recognition 
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"

def do_this_command(message):
    message = message.lower()
    if "xлоя" and "привет" in message:
        plugin_commands.hello()
    elif "хлоя" and "инструкция" in message:
        plugin_commands.help()
    elif "хлоя" and "файл" in message:
        plugin_commands.write_file(message)
    elif "хлоя" and "пока" in message:
        say_message("пока")
        exit()
    elif "хлоя" and "команды" or "команда" in message:
        plugin_commands.commands()
    else:
        say_message("Команда не распознаётся!")

def say_message(message): #голос ассистента
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print("Голосовой ассистент: "+message)
    os.remove(file_voice_name)

if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)