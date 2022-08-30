from flask import Flask, current_app, g, json
from pymongo.collection import Collection
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

def get_mongo() -> PyMongo:
    if 'mongo' not in g:
        g.mongo = PyMongo(current_app)

    return g.mongo

def get_exhibitions() -> Collection:
    return get_mongo().db.exhibitions

def all_exhibitions():
    return list(get_exhibitions().find({}))

def replace_exhibitions(exhibitions):
    get_exhibitions().drop()
    get_exhibitions().insert_many(exhibitions)

def close_mongo(e=None):
    mongo: PyMongo = g.pop('mongo', None)

    if mongo is not None:
        mongo.cx.close()

def init_app(app: Flask):
    app.teardown_appcontext(close_mongo)
    app.json_encoder = JSONEncoder

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
