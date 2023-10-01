from flask import Flask, render_template, request, url_for, redirect, session
from jinja2 import Template, FileSystemLoader, Environment
import mysql.connector


app = Flask(__name__)
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)



@app.route("/prueba", methods = ["GET", "POST"])
def prueba():
    if(request.method == "POST"):
        name = request.form['name']
        print(name)
        objetivo = request.form['objetivo']
        print(objetivo)
        descripcion = request.form['descri']
        print(descripcion)
        fecha_cierre = request.form['fecha']
        print(fecha_cierre)
        return render_template("crear_proyecto.html")
    
    return render_template("crear_proyecto.html")

@app.route("/p2", methods = ["GET", "POST"])
def sign_up():
    if(request.method == "POST"):
        name = request.form['name']
        last_name = request.form['l_name']
        e_mail = request.form['email']
        password = request.form['password']
        carrera = request.form['carrera']
        carne = request.form['carnet']
        # Atributos no pedidos en la página aún.
        celphone = request.form['cel']
        semester = request.form['semestre']
        date_birth = request.form['birth_date']
    
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
