import json
from models.exportobject import ExportObject, ExportObjectJSONEncoder
from models.ormobjects.user import User
from http_app import app, Session
from flask import request
from worldprocessing import cache


@app.route('/')
@app.route('/index')
def index():
    sess = Session()
    sess.add(User(name='123', fullname='fsdfd', password='fsdf'))
    sess.commit()
    # session = app.Session()
    # for name, fullname in session.query(User.name, User.fullname):
    #     print(name, fullname)
    return "Hello"


@app.route('/east')
def index():
    return "east"


@app.route('/west')
def index():
    return "west"


@app.route('/north')
def index():
    return "north"


@app.route('/south')
def index():
    return "south"


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        print(ExportObject.json_schema())
        cache.memoryCache = ExportObject(**request.get_json())
        with open('default_map.txt', 'w') as myfile:
            json.dump(cache.memoryCache, cls=ExportObjectJSONEncoder, fp=myfile)
        return "ok"
    else:
        return json.dumps(cache.memoryCache, cls=ExportObjectJSONEncoder)
