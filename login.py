from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, PasswordField
from wtforms.validators import DataRequired, Length,NumberRange,ValidationError
from wtforms import validators
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    email = EmailField('Correo', validators = [DataRequired(), validators.Email()])
    password = PasswordField('Contraseña', validators = [DataRequired()])
    submit = SubmitField('Login')