#coding=utf-8

from {{project}}.apps.{{app}} import mod_{{app}} as mod
from {{project}}.apps.{{app}} import models
from chan.utils.decorator import templated


@mod.route('/')
@templated()
def index():
    return {}
