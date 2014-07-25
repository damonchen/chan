#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
import shutil
from jinja2 import Template
from chan.utils import pkg
from chan.core import ExistError, NotExistError


def render(content, **context):
    template = Template(content)
    return template.render(**context)


def render_file(filename, **context):
    with open(filename, 'r') as fp:
        content = fp.read()

    with open(filename, 'w') as fp:
        fp.write(render(content, **context))


def render_folder(dst, **context):
    dst = os.path.abspath(dst)

    for root, dirnames, filenames in os.walk(dst):
        for filename in filenames:
            filename = os.path.join(root, filename)
            render_file(filename, **context)


def callback(*args, **kwargs):
    action = kwargs.pop('action')
    if action == 'extract_folder':
        print 'make folder %s' % args
    else:
        print 'copy file from %s to %s' % args

def make_project(path, name):
    project_path = os.path.join(path, name)
    if os.path.exists(project_path):
        raise ExistError(name)

    os.makedirs(project_path)

    src_path = os.path.join(project_path, name)

    pkg.extract_folder('chan', 'core/templates/project',  src_path, callback=callback)

    context = {'project': name}
    render_folder(project_path, **context)

    pkg.extract_file('chan', 'core/templates/uwsgi_handler.py',  project_path, callback=callback)
    render_file(os.path.join(project_path, 'uwsgi_handler.py'), **context)


def app_append(path, project, app):
    from_code = 'from %(project)s.apps.%(app)s import mod_%(app)s\n' % {'project': project, 'app': app}
    register_code = "app.register_blueprint(mod_%(app)s, '%(app)s')\n" % {'app': app}

    filename = os.path.join(path, project, '__init__.py')

    with open(filename, 'w') as fp:
        fp.write(from_code)
        fp.write(register_code)


def make_app(path, project, name):
    src_path = os.path.join(path, project)
    if not os.path.exists(src_path):
        raise NotExistError(project)

    apps_path = os.path.join(src_path,  'apps')
    if not os.path.exists(apps_path):
        raise NotExistError(name)

    app_path = os.path.join(apps_path, name)
    if os.path.exists(app_path):
        raise ExistError(name)

    pkg.extract_folder('chan', 'core/templates/app',  app_path, callback=callback)

    context = {'project': project, 'app': name}
    render_folder(app_path, **context)

    app_append(path, project, name)

