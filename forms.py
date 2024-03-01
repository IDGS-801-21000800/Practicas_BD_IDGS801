from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, EmailField, FloatField

from wtforms import validators 

class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message="Valor no valido")])
    nombre = StringField("nombre", validators=[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=15, message="Ingresa un nombre válido")
    ])
    direccion = StringField("direccion", validators=[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=100, message="Ingresa una dirección válida")
    ])
    telefono = StringField("telefono", validators=[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message="Ingresa un número válido")
    ])
    email = StringField("email", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])
    sueldo = FloatField("sueldo", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])
