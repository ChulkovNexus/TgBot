import json
from models.exportobject import ExportObject, ExportObjectJSONEncoder
from http_app import app, engine
from flask import request
from worldprocessing import client_actions_processor


@app.route('/')
@app.route('/index')
def index():
    client_actions_processor.create_user()
    return "Hello"


@app.route('/drop')
def drop_users():
    User.__table__.drop(engine)
    User.__table__.create(engine)
    return "recreated"


@app.route('/east')
def move_to_east():
    client_actions_processor.move_to_east()
    return client_actions_processor.get_current_user_position()


@app.route('/west')
def move_to_west():
    client_actions_processor.move_to_west()
    return client_actions_processor.get_current_user_position()


@app.route('/north')
def move_to_north():
    client_actions_processor.move_to_north()
    return client_actions_processor.get_current_user_position()


@app.route('/south')
def mode_to_south():
    client_actions_processor.mode_to_south()
    return client_actions_processor.get_current_user_position()


@app.route('/available_worktypes')
def get_available_works():
    return json.dump(client_actions_processor.get_available_works())


@app.route('/get_another_persons_on_this_tile')
def get_another_persons_on_this_tile():
    return client_actions_processor.get_another_persons_on_this_tile()


@app.route('/start_work',  methods=['POST'])
def start_work():
    return client_actions_processor.start_work()


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        print(ExportObject.json_schema())
        cache.memoryCache = ExportObject(**request.get_json())
        with open(cache.WORLD_FILE_NAME, 'w') as myfile:
            json.dump(cache.memoryCache, cls=ExportObjectJSONEncoder, fp=myfile)
        return "ok"
    else:
        return json.dumps(cache.memoryCache, cls=ExportObjectJSONEncoder)
