from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, FloatField, TelField, RadioField, BooleanField, DateField

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

class pizza(Form):
    id = IntegerField('id')
    nombre = StringField("nombre")
    direccion = StringField("direccion")
    telefono = TelField("telefono")
    tamano = RadioField("Tamaño", choices=[("chica","chica $40"), ("mediana","mediana $80"), ("grande","grande $120")])
    jamon = BooleanField("jamon $10")
    pina = BooleanField("pina $10")
    champ = BooleanField("champiñon $10")
    cantidad = IntegerField("Cantidad", [validators.number_range(min=1, max=9999, message="Valor no valido")])
    precio = FloatField("Total")
    vendido =  IntegerField("vendido")
    created_date = DateField("Fecha")