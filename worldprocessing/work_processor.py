import datetime
from abc import abstractmethod

from http_app import Session
from models.ormobjects.user import User
from models.ormobjects.works_in_progress import WorkInProgress
from models.worktype import WorkType


def calculate_finish_time(worktype: WorkType, user: User):
    skillLevel = user.get_userskill_by_id(worktype.main_skill)
    duration = worktype.baseWorkTime / skillLevel
    return datetime.datetime.now().timestamp() + duration


def begin_work(worktype):
    sess = Session()
    user = sess.query(User).filter_by(name='123').first()
    progress = WorkInProgress(user.id, worktype.id, calculate_finish_time(worktype, user))
    sess.add(progress)
    sess.commit()


def get_user_work():
    sess = Session()
    user = sess.query(User).filter_by(name='123').first()
    work = sess.query(WorkInProgress).filter_by(user_id=user.id).first()
    if work:
        return work
    else:
        return None


def check_work_finished(work):
    return work and datetime.datetime.now().timestamp() > work.finish_time


def get_work_executor(worktype_id):
    return {
        1: FirstExecutor(),
        2: FirstExecutor(),
    }[worktype_id]


def finish_work(work, user):
    executor = get_work_executor(work.worktype_id)
    executor.execute_work_finished(user)
    sess = Session()
    sess.delete(work)
    sess.commit()


class BaseExecutor:

    @abstractmethod
    def execute_work_finished(self, user): raise NotImplementedError


class FirstExecutor(BaseExecutor):

    def execute_work_finished(self, user):
        print("success")
        # cache.memoryCache.items find something
        # user.putItemToBackpack()
