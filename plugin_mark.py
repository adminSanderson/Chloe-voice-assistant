from config import *
import qrcode
from main import *

def QRversion():
    # пример данных
    data = f'CHLOE version.{VA_VER} '
    # имя конечного файла
    filename = "version.png"
    # генерируем qr-код
    img = qrcode.make(data)
    # сохраняем img в файл
    img.save(filename)
    