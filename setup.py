#!/usr/bin/env python
# -*- coding: utf-8 -*-


from . import chan
from setuptools import setup, find_packages

__doc__ =  open('README.md').read()

EXCULDE_PACKAGES = ['chan.templates.project',
                                                        'chan.templates.app']

setup(name='chan',
    version=chan.__version_str__,
    description="a flask manage tool ",
    long_description=__doc__,
    classifiers=[
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    ],
    platforms = 'any',
    keywords='flask manage tool',
    author=chan.__author__,
    author_email=chan.__author_email__,
    url=chan.__url__,
    license=chan.__license__,
    include_package_data=True,
    packages = find_packages(),
    package_dir={'chan': 'chan'},
    package_data={'chan':  ['*.html', "*.txt"]},
    install_requires = ['click', 'jinja2'],
    zip_safe=False,
    entry_points = {
      'console_scripts': [
          'chan = chan.chan:main',
      ],
    },
)
