'''from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


  return redirect(url_for('userarea_loged'))
'''
#app.run(host='0.0.0.0', port=8080)

from flask import Flask, render_template, url_for, request,send_from_directory
import pandas as pd
import lxml
import json
import requests
from datetime import date
from datetime import datetime
import xlrd
import os
import OCR as ocr

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/index')
def index():
  return render_template('index.html')


@app.route('/read_text', methods = ['POST', 'GET'])
def read_text():

  if request.method == 'POST':
    result = request.form
    var_read = result['input-text']
 
    return render_template("home.html", var_read=var_read)


@app.route('/handleUpload', methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
      photo = request.files['photo']
      #print(photo)
      if photo.filename != '':
        #print(photo.filename)
        photo.save(os.path.join('static/Read_Input/', photo.filename))

      cont = 0
      text_identify = ''
      pasta = 'static/Read_Input'
      for diretorio, subpastas, arquivos in os.walk(pasta):
          for arquivo in arquivos:
            if photo.filename == arquivo:
              #print('>>>>>>>>>',os.path.join(diretorio, arquivo))
              read = ocr.read(photo.filename)
              text_identify = 'Texto Identificado'
              return render_template('readed.html',read=read,text_identify=text_identify)
            else:
              cont += 1
      
      if cont == len(arquivos):
        text_identify = 'Nenhum Texto foi Identificado'
        return render_template('readed.html', text_identify=text_identify)

if __name__ == '__main__':
    app.run(debug=True)
  