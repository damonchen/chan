#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask('apps')
app.config.from_object('apps.config')

db = SQLAlchemy(app)


from apps.apps.index import mod_index

app.register_blueprint(mod_index)