from main import *
from name import *
from main import say_message

def user_name():
    say_message("Здравствуйте! Меня зовут Хлоя. Как вас зовут?")
    file = open("name.py", "w", encoding="utf-8") # w - write
    query=listen_command().lower() # слушаем 
    USER_NAME = query.replace("", "") # Возвращает копию строки, в которой заменены все вхождения указанной строки указанным значением.
    file.write(f"USER_NAME = str('{USER_NAME}') ")
    file.close()
    say_message("Отлично! Настройка завершена. ")
    exit()