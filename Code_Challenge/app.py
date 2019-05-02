# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:52:15 2019

@author: PRINCE
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/home/<name>')
def name(name):
    return "Name : %s" %name

if __name__ == '__main__':
    app.run(debug=True)