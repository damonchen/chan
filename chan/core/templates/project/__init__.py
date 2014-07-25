#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from {{project}}.env import (STATIC_PATH, TEMPLATE_PATH)


app = Flask('apps', static_folder=STATIC_PATH, template_folder=TEMPLATE_PATH)
app.config.from_object('{{project}}.config')

db = SQLAlchemy(app)


from {{project}}.apps.home import mod_home
app.register_blueprint(mod_home)

