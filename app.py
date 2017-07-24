#!/usr/bin/env/python
# -*- coding: utf-8 -*-

import os
import sqlite3
from flask import Flask, request, session, redirect, url_for,\
render_template, flash
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
Bootstrap(app)

nav=Nav()
nav.register_element('top',Navbar(u'Flask入门',
                                    View(u'主页','home'),
                                    View(u'关于','about'),
                                    Subgroup(u'项目',
                                             View(u'项目一','about'),
                                             Separator(),
                                             View(u'项目二', 'service'),
                                    ),
))
nav.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/service')
def service():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)