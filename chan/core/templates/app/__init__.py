#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

mod_{{app}} = Blueprint("{{app}}", __name__)


from {{project}}.apps.{{app}} import views
