# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:57:44 2019

@author: PRINCE
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Anshul Mehta'

@app.route('/about')
def about():
    return 'Prince'

if __name__ == '__main__':
    app.run(debug=True)
