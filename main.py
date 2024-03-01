from flask import Flask, render_template, request #importe de las librerias
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
from models import db, Empleado
import forms

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/")
def load():
    return render_template("index.html")

@app.route("/empleado", methods=["GET", "POST"])
def empleados():
    empleado_clase = forms.UserForm(request.form)
    if request.method == "POST":
        emp = Empleado( 
            nombre=empleado_clase.nombre.data,
            direccion=empleado_clase.direccion.data,
            telefono=empleado_clase.telefono.data,
            email=empleado_clase.email.data,
            sueldo=empleado_clase.sueldo.data)
        
        db.session.add(emp)
        db.session.commit()       

    return render_template("index.html", form=empleado_clase)

@app.route("/empleados", methods=["GET", "POST"])
def abc():
    empleados = forms.UserForm(request.form)
    emp = Empleado.query.all()

    return render_template("empleados.html", empleados = emp)

@app.errorhandler(404)
def errorHandler(ex):
    return render_template("404.html"),404

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    app.run()