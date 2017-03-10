# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, Response

app = Flask(__name__)


#Devuelve por el navegador texto plano
@app.route('/un_texto_plano')
def text():
    return render_template('basic-content.html',contenido="Sirviendo texto plano")


#Devuelve en el navegador codigo html
@app.route('/contenido_html')
def html():
    return render_template('basic-content.html',contenido='Sirviendo <b>html</b>')



#Devuelve por en navegador una imagen
@app.route('/archivo')
def ima():
    response = Response()
    response.headers['Content-Type']='image/jpg'
    f= open('app/static/images/imagen.jpg', 'rb')
    ima=f.read()
    response.set_data(ima)
    return response


#Devuelve por el navegador una variable que le pase en la ruta
@app.route('/sirviendo_variables/<variable>')
def variable(variable):
    return render_template('basic-content.html',contenido=variable)


#Devuelve una lista de items
@app.route('/lista')
def lista():

    usuarios = []
    usuarios.append({'name':'pepe','dni':2345})
    usuarios.append({'name':'jose','dni':2323})
    usuarios.append({'name':'pablo','dni':2356})

    return render_template('list.html', usuarios=usuarios)


#Página de error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug='true')
