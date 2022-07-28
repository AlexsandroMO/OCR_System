
#you need to install Tesserac in your Windows
#https://github.com/UB-Mannheim/tesseract/wiki
#https://www.youtube.com/watch?v=k_tSO2qxAnU
#pip install -r requirements.txt

import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Users\alexsandrooliveira\AppData\Local\Tesseract-OCR\tesseract.exe'

img_ = 'Screenshot-2022-07-28-105138.png'
#img_ = 'TESTE_IMG.jpeg'

new_text = pytesseract.image_to_string(Image.open(img_)).split('\n')

print('\n')
#print(new_text)

print(new_text[0])
print(new_text[1])
print('\n')
cont = 0
for a in new_text:
    #print(a)
    if a != '' and cont > 1:
        new = a.split(';')
        for b in new:
            if b != '':
                print(b.replace(' ',''))
    cont +=1

print('\n')