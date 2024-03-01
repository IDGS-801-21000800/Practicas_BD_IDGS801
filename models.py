from flask_sqlalchemy import SQLAlchemy
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