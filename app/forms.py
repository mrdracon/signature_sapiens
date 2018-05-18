# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SignatureForm(FlaskForm):
    first_name = StringField(u'Имя', validators=[DataRequired()])
    last_name = StringField(u'Фамилия', validators=[DataRequired()])
    position = StringField(u'Должность с маленькой буквы', validators=[DataRequired()])
    email = StringField(u'email, ...@sapiens.solutions', validators=[DataRequired()])
    mob = StringField(u'mobile, +7 xxx xxx xxxx', validators=[DataRequired()])
    submit = SubmitField(u'Скачать подпись')
