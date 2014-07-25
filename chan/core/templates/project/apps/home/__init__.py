#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

mod_home = Blueprint("home", __name__)


from {{project}}.apps.home import views
