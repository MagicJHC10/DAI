
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect,session,url_for, escape
import shelve


app = Flask(__name__)

app.secret_key = 'Secreto'


@app.after_request
def save_history(rsp):
        if 'miembro' in session and request.method == "GET" and rsp.mimetype == "text/html":
                        session['urls'].append(request.path)
                        session.modified = True
                        if(len(session['urls'])) > 3:
                                session['urls'].pop(0)
        return rsp


@app.route("/")
def template():
	return render_template('padre.html')



@app.route("/hijo1")
def hijo():
	return render_template('hijo1.html')

@app.route("/hijo2")
def hijo2():
	return render_template('hijo2.html')

@app.route("/hijo3")
def hijo3():
	return render_template('hijo3.html')

@app.route("/login", methods = ['GET', 'POST'])
def login():
	database = shelve.open('database.db')
	miembro = request.form['miembro']

	if request.method == 'POST' and miembro in database and database[miembro]['Contraseña'] == request.form['pass'] :
		session['miembro'] = request.form['miembro']
		session['urls'] = []

	database.close()
	return render_template('padre.html')

@app.route('/logout')
def logout():
   session.pop('miembro','urls')
   return render_template('padre.html')

@app.route('/nuevousuario', methods = ['GET', 'POST'])
def reg():
	if request.method == 'POST' :
		database = shelve.open('database.db')
		database[request.form['miembro']] = {'Nombre' : request.form['miembro'], 'Contraseña' : request.form['pass'], 'Telefono' : request.form['tel']}
		database.close()
	return render_template('registro.html')

@app.route('/verusuario')
def ver():
	database = shelve.open('database.db')
	datos = database[session['miembro']]
	database.close()
	return render_template('ver.html', Nombre = 'Nombre: ' + datos['Nombre'])
@app.route('/editar', methods = ['GET', 'POST'])
def editar():
	database = shelve.open('database.db',writeback=True)
	datos = database[session['miembro']]
	if request.method == 'POST' :
		datos['Nombre']=request.form['miembro']
		datos['Contraseña']=request.form['pass']
		datos['Telefono']=request.form['tel']
	database.close()
	return render_template('editar.html', Nombre = datos['Nombre'], Tel =datos['Telefono'], Contra =datos['Contraseña'])





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
