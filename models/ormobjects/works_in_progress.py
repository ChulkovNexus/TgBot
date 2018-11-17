
from sqlalchemy import Integer, Column, Date, Sequence, String

from http_app import Base


class WorkInProgress(Base):
    __tablename__ = 'work_in_progress'

    user_id = Column(Integer, primary_key=True)
    worktype_id = Column(Integer)
    finish_time = Column(Date)

    def __init__(self, user_id, worktype_id, finish_time):
        self.user_id = user_id
        self.worktype_id = worktype_id
        self.finish_time = finish_time
