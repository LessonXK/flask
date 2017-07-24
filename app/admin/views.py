#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from . import admin
from .. import db
from ..models import Login
from forms import LoginForm

@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Login.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            #login_user(user, form.remember_me.data)
            flash('valid username or password.')
            return render_template('login.html', title_name=u"后台登陆", form=form)
        flash('Invalid username or password.')
        
    return render_template('login.html', title_name=u"后台登陆", form=form)

