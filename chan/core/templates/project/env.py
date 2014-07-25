#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

__all__ = ['PROJECT_PATH', 'WORK_PATH', 'STATIC_PATH', 'TEMPLATE_PATH']


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
WORK_PATH = os.path.dirname(PROJECT_PATH)
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
