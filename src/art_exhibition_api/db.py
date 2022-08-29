from flask import Flask, current_app, g
from pymongo.collection import Collection
from flask_pymongo import PyMongo

def get_mongo() -> PyMongo:
    if 'mongo' not in g:
        g.mongo = PyMongo(current_app)

    return g.mongo

def get_exhibitions() -> Collection:
    get_mongo().db.exhibitions

def close_mongo():
    mongo: PyMongo = g.pop('mongo', None)

    if mongo is not None:
        mongo.cx.close()

def init_app(app: Flask):
    app.teardown_appcontext(close_mongo)
