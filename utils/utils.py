#!/usr/bin/python
# -*- coding: utf8 -*-
import os

DEBUG = True

APP_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))


def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
