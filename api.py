#!/usr/bin/env python

from os import getenv
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = getenv('MONGO_URI', 'mongodb://localhost:27017/bm')
mongo = PyMongo(app)


@app.route('/')
def index(): return jsonify(status='ok')


if __name__ == '__main__':
    app.run(**{
        'host': '0.0.0.0',
        'debug': getenv('DEBUG', 'True') == 'True',
        'port': int(getenv('PORT', "7766"))
    })
