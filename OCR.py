#you need to install Tesserac in your Windows
#https://github.com/UB-Mannheim/tesseract/wiki
#https://www.youtube.com/watch?v=k_tSO2qxAnU
#pip install -r requirements.txt

import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd=r'C:\Users\alexsandrooliveira\AppData\Local\Tesseract-OCR\tesseract.exe'

def read(result):
    readed = pytesseract.image_to_string(Image.open('static/Read_Input/{}'.format(result)))
    return readed






