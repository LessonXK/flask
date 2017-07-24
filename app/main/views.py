#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from . import main
from .. import db

@main.route('/')
def index():
    return render_template('index.html', title='hello world')

