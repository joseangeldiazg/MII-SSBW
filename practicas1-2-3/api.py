# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, Response

app = Flask(__name__)


#Devuelve por el navegador texto plano
@app.route('/un_texto_plano')
def text():
    response = Response()
    response.set_data('Sirviendo texto plano')
    return response


#Devuelve en el navegador codigo html
@app.route('/contenido_html')
def html():
    response = Response()
    response.set_data('Sirviendo <b>html</b>')
    return response



#Devuelve por en navegador una imagen
@app.route('/archivo')
def ima():
    response = Response()
    response.headers['Content-Type']='image/jpg'

    f= open('./static/ima/imagen.jpg', 'rb')

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
