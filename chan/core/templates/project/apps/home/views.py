#coding=utf-8

from {{project}}.apps.home import mod_home as mod
from {{project}}.apps import models
from chan.utils.decorator import templated


@mod.route('/')
@templated()
def index():
    return {}
