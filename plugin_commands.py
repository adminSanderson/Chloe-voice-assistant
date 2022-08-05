from main import *
import random
from colorama import *
from time import *
from config import *
import config

def hello():
    hello_examples = ["Привет!", "Хай", "и тебе привет", "Приветствую вас!", "Салют!", "Хэлло!"]
    random_index = random.randrange(len(hello_examples))
    say_message(hello_examples[random_index])

def help():
    print(Fore.BLUE  +  f'----Инструкция Хлои v{config.VA_VER}----' )
    print(Fore.BLUE  + "#" + Fore.WHITE + '1. Установите программу или установщик с голосовым помощником "Хлоя" ')
    print(Fore.BLUE  + "#" + Fore.WHITE + "2. После включения скажите ваше имя. Если вы хотите сменить имя то произнесите команду: Хлоя измени имя.")
    print(Fore.BLUE  + "#" + Fore.WHITE + "3. Начните диалог с Хлоей.")
    say_message("Инструкция Хлои")
    say_message("№1. Установите программу или установщик с голосовым помощником Хлоя")
    say_message("№2. После включения скажите ваше имя. Если вы хотите сменить имя то произнесите команду: Хлоя измени имя")
    say_message("№3. Начните диалог с Хлоей!")

def commands():
    print(Fore.BLUE  +  f'----Команды Хлои v{config.VA_VER}----' )
    print(Fore.BLUE  +  '----Описания --- Команда----' )
    print(Fore.BLUE  + "#" + Fore.WHITE + "Перед или после того как сказать свою команду просто скажите 'Хлоя' ")
    print(Fore.BLUE  + "#" + Fore.WHITE + "1. Приветствие. --> Привет Хлоя")
    print(Fore.BLUE  + "#" + Fore.WHITE + "2. Команды Хлои. --> Хлоя команды")
    print(Fore.BLUE  + "#" + Fore.WHITE + "3. Инструкция по установке. --> Хлоя инструкция")
    print(Fore.BLUE  + "#" + Fore.WHITE + "4. Время. --> Хлоя время")
    # print(Fore.BLUE  + "#" + Fore.WHITE + "1. Привет.")
    say_message("Команды Хлои")
    say_message("Слева будут написанны описание , а справа сама команда.")
    say_message("Так же хочу сказать, что перед или после того как сказать свою команду просто скажите 'Хлоя' ")

def write_file(message):
    file_name = "TEXT.txt"
    file = open(file_name, "w", encoding="utf-8")
    say_message("Файл создан! Через 3 секунты вы должны будете сказать ваш текст.")
    say_message("3")
    sleep(1)
    say_message("2")
    sleep(1)
    say_message("1")
    sleep(1)
    x = input("Введите текст: ")
    file.write(x)
    file.close()
    say_message("Ваш текст сохранён")
