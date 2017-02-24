# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, Response

app = Flask(__name__)

@app.route('/archivo')
def ima():
    response = Response()
    response.headers['Content-Type']='image/jpg'

    f= open('./resources/imagen.jpg', 'rb')

    ima=f.read()
    response.set_data(ima)
    return response

@app.route('/')
def hello_world():

    usuarios = []
    usuarios.append({'name':'pepe','dni':2345})
    usuarios.append({'name':'jose','dni':2323})
    usuarios.append({'name':'pablo','dni':2356})

    return render_template('hola.html', usuarios=usuarios)

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug='true')
