import json
from models.exportobject import ExportObject, ExportObjectJSONEncoder
from http_app import app
from flask import request
from worldprocessing import cache


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


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
