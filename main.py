from flask import Flask, render_template, request, redirect, url_for #importe de las librerias
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from sqlalchemy import func
from datetime import date
from config import DevelopmentConfig
from models import db, Empleado, Pizza
import forms

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/")
def load():
    empleado = forms.UserForm(request.form)
    return render_template("index.html", form = empleado)

@app.route("/cancelar")
def pizzacl():
    db.session.query(Pizza).filter(Pizza.vendido==0).delete()
    db.session.commit()
    return redirect(url_for("pizza"))


@app.route("/ventas", methods=["GET", "POST"])
def pizzave():
    if request.method == "POST":
        db.session.query(Pizza).filter(Pizza.vendido==0).update({"vendido":1}, synchronize_session='evaluate')
        db.session.commit()
        return redirect(url_for("pizza"))
    if request.method == "GET":
        pizza = forms.pizza(request.form)
        pizzas = db.session.query(Pizza).filter(Pizza.vendido==1)
        pizzasv = db.session.query(Pizza).filter(Pizza.vendido==0)
        return render_template("pizzeria.html", pizza=pizza, pizzas = pizzas, pizzasv=pizzasv)

@app.route("/eliminarPizza", methods=["GET", "POST"])
def pizzadw():
    pizzaf = forms.pizza(request.form)
    id=request.args.get('id')
    if request.method == "POST":
        id=pizzaf.id.data
        alum = Pizza.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("pizza"))
    if request.method == "GET":
        pizza = db.session.query(Pizza).filter(Pizza.id==id).first()
        pizzaf.id.data = id
        pizzaf.nombre.data=pizza.nombre
        pizzaf.direccion.data=pizza.direccion
        pizzaf.telefono.data=pizza.telefono
        pizzaf.precio.data = pizza.total
        pizzaf.tamano.data = pizza.tamano
        pizzaf.jamon.data = pizza.jamon
        pizzaf.champ.data = pizza.champ
        pizzaf.pina.data = pizza.pina
        pizzaf.cantidad.data = pizza.cantidad
        pizzaf.vendido.data = 0
        return render_template("eliminarPizza.html", pizza=pizzaf)

@app.route("/pizzeria", methods=["GET", "POST"])
def pizza():
    pizza = forms.pizza(request.form)
    pizzas_v2 = db.session.query(Pizza.nombre, func.sum(Pizza.total).label("total"), Pizza.created_date).group_by(Pizza.nombre).filter(Pizza.vendido==1).all()
    total = 0

    mes = request.args.get("filtMes")
    dia = request.args.get("filtDia")

    if(mes==""):
        pizzas_v3 = pizzas_v2
    else:
        pizzas_v3 = [x for x in pizzas_v2 if x.created_date.strftime("%m") == retFech(mes)]
    
    if(dia==""):
        pizzas_v4 = pizzas_v3
    else:
        pizzas_v4=[]
        for x in pizzas_v3:
            mi_fecha = date(int(x.created_date.strftime("%y")), int(x.created_date.strftime("%m")), int(x.created_date.strftime("%d")))
            if mi_fecha.isoweekday() == int(retFech(dia)):
                pizzas_v4.append(x) 

    for pizza_v4 in pizzas_v4:
        total = total + pizza_v4.total

    pizzasv = db.session.query(Pizza).filter(Pizza.vendido==0)
    totals = 0
    
    for pizzav in pizzasv:
        totals = totals + pizzav.total
    if request.method == "POST":
        total = 0
        if pizza.tamano.data == "chica":
            total += 40
        elif pizza.tamano.data == "mediana":
            total += 80
        else:
            total += 120
        
        if pizza.jamon.data == True:
            total += 10
        if pizza.champ.data == True:
            total += 10
        if pizza.pina.data == True:
            total += 10
        
        total = total * pizza.cantidad.data
        totals += total
        
        pizza_bd = Pizza( 
            nombre=pizza.nombre.data,
            direccion=pizza.direccion.data,
            telefono=pizza.telefono.data,
            total = total,
            tamano = pizza.tamano.data,
            jamon = pizza.jamon.data,
            champ = pizza.champ.data,
            pina = pizza.pina.data,
            cantidad = pizza.cantidad.data,
            created_date = pizza.created_date.data,
            vendido = 0
            )
        db.session.add(pizza_bd)
        db.session.commit()
        return render_template("pizzeria.html", pizza=pizza, pizzas = pizzas_v4, pizzasv=pizzasv, total=total, stotal=totals)
    return render_template("pizzeria.html", pizza=pizza, pizzas = pizzas_v4, pizzasv=pizzasv, total=total, stotal=totals)

def retFech(arg):
    if arg == "Lunes" or arg == "enero": return "01"
    elif arg == "Martes" or arg == "febrero": return "02"
    elif arg == "Miércoles" or arg == "marzo":return "03"
    elif arg == "Jueves" or arg == "abril":return "04"
    elif arg == "Viernes" or arg == "mayo":return "05"
    elif arg == "Sábado" or arg == "junio" :return "06"
    elif arg == "Domingo" or arg == "julio" : return "07"
    elif arg == "agosto" : return "08"
    elif arg == "septiembre" : return "09"
    elif arg == "octubre" : return "10"
    elif arg == "noviembre" : return "11"
    elif arg == "diciembre" : return "12"
    else: return "none"

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


@app.route("/EmpEliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id=request.args.get('id')
        alumn = db.session.query(Empleado).filter(Empleado.id==id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alumn.nombre
        create_form.direccion.data = alumn.direccion
        create_form.telefono.data = alumn.telefono
        create_form.email.data = alumn.email
        create_form.sueldo.data = alumn.sueldo

    if request.method == "POST":
        id=create_form.id.data
        alum = Empleado.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("abc"))
    
    return render_template("EmpEliminar.html", form=create_form)


@app.route("/EmpModificar", methods=["GET", "POST"])
def empModificar():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id=request.args.get('id')
        alumn = db.session.query(Empleado).filter(Empleado.id==id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alumn.nombre
        create_form.direccion.data = alumn.direccion
        create_form.telefono.data = alumn.telefono
        create_form.email.data = alumn.email
        create_form.sueldo.data = alumn.sueldo

    if request.method == "POST":
        id=create_form.id.data
        alumn = db.session.query(Empleado).filter(Empleado.id==id).first()
        alumn.nombre = create_form.nombre.data
        alumn.direccion = create_form.direccion.data
        alumn.telefono = create_form.telefono.data
        alumn.email = create_form.email.data
        alumn.sueldo = create_form.sueldo.data

        db.session.add(alumn)
        db.session.commit()
        return redirect(url_for("abc"))
    
    return render_template("EmpModificar.html", form=create_form)

@app.errorhandler(404)
def errorHandler(ex):
    return render_template("404.html"),404

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    app.run()