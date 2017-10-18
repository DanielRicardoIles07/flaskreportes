from flask import Flask, render_template, request, jsonify, redirect, url_for
import flask_excel as excel
from flask.ext import excel
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask import jsonify
from flask import g
from flask import abort
import pymysql
from functools import wraps
db = pymysql.connect("domiciliosurbanos.com", "joseluis", "597b9050653f3", "mu_domicilios")
app = Flask(__name__)
#database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reportesmensajeros'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#init database
mysql = MySQL(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/reportesTotalServiciosEmpresa')
def ServiciosEmpresa():
	cur = mysql.connection.cursor()
	result = cur.execute("select id_registro, fecha_inicio, fecha_fin, id_empresa, ciudad, estado_servicio from log_reporte;")
	servicios = cur.fetchall()
	return render_template('reportesTotalServiciosEmpresa.html', servicios=servicios)
	cur.close()

@app.route('/api/puntos/domicilios/v.1.0')
def puntos():
    cursor = db.cursor()
    sql = "select p.id, p.nombre, empresa_id, p.lat, p.long, p.direccion, p.ciudad, (e.nombre) as empresa, e.mu_ref from puntos p left join empresa e on p.empresa_id = e.id where mu_ref is not null group by mu_ref order by ciudad"
    cursor.execute(sql)
    results = cursor.fetchall()
    return jsonify(results=results)

if __name__ == '__main__':
	app.secret_key='secret123'
	app.run(debug=True, port= 8000)
