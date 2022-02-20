from flask import *
app = Flask(__name__)
import cv2 #opencv
import urllib.request #para abrir y leer URL
import numpy as np

#PROGRAMA DE CLASIFICACION DE OBJETOS PARA VIDEO EN DIRECCION IP 


@app.route('/')
def entrada():
   return app.send_static_file('entrada.html')

@app.route('/principal', methods=['GET'])
def prin():
   return app.send_static_file('principal.html')


@app.route('/home', methods=['GET'])
def home():
   return app.send_static_file('home.html')


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)