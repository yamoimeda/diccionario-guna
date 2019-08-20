from flask import Flask,redirect,url_for,render_template,request,jsonify
from pymongo import MongoClient
import sqlite3 as sql
app = Flask(__name__)

#cliente = MongoClient("localhost", 27017)
#db = cliente.diccionarios

@app.route('/',methods=['GET','POST'])
def index():

	return render_template('inicios.html')
@app.route('/resultado',methods=['GET','POST'])
def resultados():
    if request.method == 'POST':
        palabra = request.form['palabra']
        conn = sql.connect("diccionarioguna.db")
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('''SELECT significado FROM palabras where palabra = ?''',(palabra,))
        signifi = cur.fetchall()
        if len(signifi) == 0:

            significado = 'no hay coincidencia'

        else:
            for ab in signifi:
                
                significado = ab['significado']
        
	
    return significado

if __name__ == '__main__':
    app.run()


