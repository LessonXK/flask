#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from app import create_app, db
from app.models import Admin, Login
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    """自动加载环境"""
    return dict(
        app=app,
        db=db,
        Admin=Admin,
        Login=Login
    )


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """运行测试"""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import upgrade

    # migrate database to latest revision
    upgrade()

    # create user roles
    Login.insert_user()


if __name__ == '__main__':
    app.debug = True
    manager.run()