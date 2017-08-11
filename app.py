#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

from core import *

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Service is running'


@app.route('/handle')
def handle():
    pass


def demo():
    s = '  Hello   Khoa    dep  trai   eh  \r\n\r\n\n\n\n\n\r\n ANC    \nKhoa'
    debug([normalize_text(s)])
    return


if __name__ == '__main__':
    demo()
    # app.run(threaded=True, host='0.0.0.0', port=5000, debug=DEBUG)
