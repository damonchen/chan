#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from functools import wraps
from flask import jsonify
from flask import request, redirect, url_for, g, render_template


def templated(template=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint.replace('.', '/') + '.html'

            start = time.time()
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            end = time.time()
            render_time = int((end - start) * 1000)
            ctx['render_time'] = render_time

            return render_template(template_name, **ctx)

        return wrapper
    return decorator



def jsonp():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx

            ctx.setdefault('code', 200)
            ctx.setdefault('success', True)

            return jsonify(ctx)
        return wrapper
    return decorator
