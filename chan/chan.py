#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from core import ExistError, NotExistError
from utils.cmd import make_project, make_app


PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(PATH, 'core', 'templates')
PROJECT_PATH = os.path.join(TEMPLATE_PATH, 'project')
APP_PATH = os.path.join(TEMPLATE_PATH, 'app')
PWD_PATH = os.path.abspath(os.getcwd())



@click.group()
def chan():
    pass


@chan.command()
@click.argument('name')
def startproject(name):
    try:
        make_project(PWD_PATH, name)
    except ExistError:
        click.echo('project name %s has already exist' % name)


@chan.command()
@click.argument('name')
def startapp(name):
    project = os.path.basename(PWD_PATH)
    try:
        make_app(PWD_PATH, project, name)
    except ExistError:
        click.echo('app name %s has already exist' % name)
    except NotExistError:
        click.echo('startapp should occur project path')


@chan.command()
@click.option('--host',  '-h', default='0.0.0.0')
@click.option('--port', '-p' , default=5000)
@click.option('--debug', '-d' ,default=True)
def runserver(host, port, debug):
    project = os.path.dirname(PWD_PATH)
    mod = __import__(project)

    mod.app.debug = debug
    mod.app.run(host=host, port=port)


def main():
    chan()


if __name__ == '__main__':
    main()


