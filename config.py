#!/usr/bin/env/python
# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
    SECRET_KEY = 'hard to guess string'