#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from {{project}} import app as application


@click.command()
@click.option('--debug/--no-debug', default=True,
              envvar='REPO_DEBUG')
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=5000)
def main(debug, host, port):
    application.debug = debug
    application.run(host=host, port=port)


if __name__ == '__main__':
    main()
