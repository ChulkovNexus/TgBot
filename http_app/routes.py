import json
from models.exportobject import ExportObject, ExportObjectJSONEncoder
from models.ormobjects.user import User
from http_app import app, Session, engine, Base
from flask import request
from worldprocessing import cache, mapviewer

viewer = mapviewer.MapViewer()


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

@app.route('/drop')
def drop_users():
    User.__table__.drop(engine)
    User.__table__.create(engine)
    return "recreated"


@app.route('/east')
def move_to_east():
    sess = Session()
    user = sess.query(User).filter_by(name='123').first()
    x_position = user.xPosition or 0
    y_position = user.yPosition or 0
    if x_position < cache.memoryCache.map.getXLenght() - 1:
        user.xPosition = x_position + 1

    return viewer.get_nearest_description(cache.memoryCache.map.getTile(x_position, y_position))


@app.route('/west')
def move_to_west():
    return "west"


@app.route('/north')
def move_to_north():
    return "north"


@app.route('/south')
def mode_to_south():
    return "south"


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
