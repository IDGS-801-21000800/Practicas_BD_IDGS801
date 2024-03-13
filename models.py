from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select
from sqlalchemy.orm import with_expression, query_expression
import datetime

db = SQLAlchemy()

class Empleado(db.Model):
    __tablename__ =  "empleado" 
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(10))
    email = db.Column(db.String(50))
    sueldo = db.Column(db.Float)
    created_date = db.Column(db.DateTime, default = datetime.datetime.now)
class Pizza(db.Model):
    __tablename__ =  "pizzas" 
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(10))
    total = db.Column(db.Float)

    tamano =  db.Column(db.String(20))
    jamon = db.Column(db.Integer)
    pina =  db.Column(db.Integer)
    champ =  db.Column(db.Integer)
    cantidad =  db.Column(db.Integer)
    vendido = db.Column(db.Integer)

    created_date = db.Column(db.DateTime)
