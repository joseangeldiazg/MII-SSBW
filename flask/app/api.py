# -*- coding: utf-8 -*-
from flask import Flask, escape, redirect, render_template, request, session, url_for, Response

app = Flask(__name__)


#Devuelve por el navegador texto plano
@app.route('/un_texto_plano')
def text():
    if 'usermail' in session:
        return render_template('basic-content.html',contenido="Sirviendo texto plano")
    return render_template('login')

#Devuelve en el navegador codigo html
@app.route('/contenido_html')
def html():
    if 'usermail' in session:
        return render_template('basic-content.html',contenido='Sirviendo <b>html</b>')
    return render_template('login')


#Devuelve por en navegador una imagen
@app.route('/archivo')
def ima():
    if 'usermail' in session:
        response = Response()
        response.headers['Content-Type']='image/jpg'
        f= open('app/static/images/imagen.jpg', 'rb')
        ima=f.read()
        response.set_data(ima)
        return response
    return render_template('login')

#Devuelve por el navegador una variable que le pase en la ruta
@app.route('/sirviendo_variables/<variable>')
def variable(variable):
    if 'usermail' in session:
        return render_template('basic-content.html',contenido=variable)
    return redirect(url_for('login'))

#Devuelve una lista de items
@app.route('/lista')
def lista():
    if 'usermail' in session:
        usuarios = []
        usuarios.append({'name':'pepe','dni':2345})
        usuarios.append({'name':'jose','dni':2323})
        usuarios.append({'name':'pablo','dni':2356})
        return render_template('list.html', usuarios=usuarios)
    return redirect(url_for('login'))


#Página de error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


#Inicio
@app.route('/')
def hello():
    if 'usermail' in session:
        usermail = session['usermail']
        return render_template('hello.html', usuario=usermail)
    return redirect(url_for('login'))


#login
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['usermail'] = request.form['usermail']
    return redirect(url_for('hello'))
  return render_template('login.html')

 #logout

@app.route('/logout')
def logout():
    if 'usermail' in session:
        session.pop('usermail', None)
        return render_template('login.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', debug='true')
