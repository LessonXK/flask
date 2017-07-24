#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Model):
    """图书类"""
    __searchable__ = ['name', 'tag', 'summary']
    __tablename__ = "Admin"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(164))

    @staticmethod
    def insert_user():
        user = Admin.query.filter_by(username='admin').first()
        if user is None:
            user = Admin(username='admin')
            user.password = 'admin'
            db.session.add(user)
            db.session.commit()

    def __repr__(self):
        return "%r :The instance of class Admin" % self.username

class Login(db.Model):
    """登陆类"""
    __tablename__ = "Login"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    @staticmethod
    def insert_user():
        login = Login.query.filter_by(username='admin').first()
        if login is None:
            login = Login(username='admin')
            login.password = 'admin'
            db.session.add(login)
            db.session.commit()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        #return '<Login {username}:{password}>'.format(username=self.username,password=self.password)
        return '<Login %r' % self.password_hash