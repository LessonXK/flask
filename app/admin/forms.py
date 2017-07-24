#!/usr/bin/env/python
# -*- coding: utf-8 -*-


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError

class LoginForm(FlaskForm):
    username = StringField('username', validators=[Length(0, 64)])
    password = StringField('password', validators=[Length(0, 64)])
    submit = SubmitField('submit')