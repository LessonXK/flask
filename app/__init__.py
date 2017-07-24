#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from flask import Flask, request, session, redirect, url_for,\
render_template, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    bootstrap.init_app(app)
    db.init_app(app)

    app.config.from_object(DevelopmentConfig)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
