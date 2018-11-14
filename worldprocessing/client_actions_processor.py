from http_app import Session

from models.ormobjects.user import User

from worldprocessing import cache, mapviewer, work_processor

viewer = mapviewer.MapViewer()


def create_user():
    sess = Session()
    sess.add(User(name='123', fullname='fsdfd', password='fsdf'))
    sess.commit()


def move_to_east():
    sess = Session()
    user = sess.query(User).filter_by(name='123').first()
    x_position = user.xPosition or 0
    if x_position < cache.memoryCache.map.getXLenght() - 1:
        user.xPosition = x_position + 1


def move_to_west():
    sess = Session()
    user = sess.query(User).filter_by(name='123').first()
    x_position = user.xPosition or 0
    if x_position > 0:
        user.xPosition = x_position - 1


def move_to_north():
    sess = Session()
    user = sess.query(User).filter_by(name='123').first()
    y_position = user.yPosition or 0
    if y_position > 0:
        user.xPosition = y_position - 1


def mode_to_south():
    sess = Session()
    user = sess.query(User).filter_by(name='123').first()
    y_position = user.yPosition or 0
    if y_position < cache.memoryCache.map.getYLenght() - 1:
        user.xPosition = y_position + 1


def get_current_user_position():
    sess = Session()
    user = sess.query(User).filter_by(name='123').first()
    x_position = user.xPosition or 0
    y_position = user.yPosition or 0
    return viewer.get_nearest_description(cache.memoryCache.map.getTile(x_position, y_position))


def get_available_works():
    sess = Session()
    user = sess.query(User).filter_by(name='123').first()
    available_worktypes = []
    for work_type in cache.memoryCache.workTypes:
        mapTile = cache.memoryCache.map.getTile(user.xPosition, user.yPosition)
        if work_type.main_skill == 0 or user.skill_exp_to_skill_level(user.get_userskill_by_id(work_type.main_skill)) > work_type.required_skill_level\
                and set(work_type.resources).issubset(mapTile.mapResources)\
                and set(work_type.buildings).issubset(mapTile.get_available_buildings()):
            available_worktypes.append(work_type)

    return available_worktypes


def start_work(worktype_id):
    w = next((worktype for worktype in get_available_works() if worktype.id == worktype_id), None)
    if w:
        work_processor.begin_work(w)
        return True
    else:
        return False


def get_another_persons_on_this_tile():
    return None