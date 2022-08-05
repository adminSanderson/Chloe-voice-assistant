from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr
import os
from user_set import user_settings
from config import *
import plugin_commands
import plugin_mark
import plugin_register_new_user

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

def say_message(message): #голос ассистента
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
    voice.save(file_voice_name) 
    playsound.playsound(file_voice_name)
    print("Голосовой ассистент: "+message)
    os.remove(file_voice_name)


if user_settings['name'] == '':
    file = open("user_set.py", "w", encoding="utf-8")
    say_message("Здравствуйте. Меня зовут Хлоя. Я ваш голосовой ассистент. Для вашего удобства напишите ваше имя.")
    name = input("---> ")

    say_message("Хорошо. Вы мужчина или женщина?")
    sex = input("---> ")

    say_message("Отлично! Теперь напишите ваш возраст:")
    age = input("---> ")

    say_message("Окей, теперь введите ваш вес.")
    weight = input("---> ")

    say_message("Хорошо. А теперь ваш рост.")
    height = input("---> ")

    file.write("user_settings = {")
    file.write(f'"name": "{name}",')
    file.write(f'" age": "{age}",')
    file.write(f'" sex": "{sex}",')
    file.write(f'" weight": "{weight}",')
    file.write(f'" height": "{height}"')
    file.write('}')
    file.close()
    
    say_message("Спасибо. Теперь мы можем начать наш разговор.")
    exit()

elif user_settings['name'] != '':
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
        elif "хлоя" and "версия" in message:
            plugin_mark.QRversion()
            say_message('Моя версия ' + VA_VER)
        elif "хлоя" and "команды" or "команда" in message:
            plugin_commands.commands()
        else:
            say_message("Команда не распознаётся!")



if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)