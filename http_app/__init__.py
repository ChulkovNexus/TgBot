from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///Z:\\database\\test.db', echo=True)
Session = sessionmaker()
Base = declarative_base()
app = Flask(__name__)

from http_app import routes

Base.metadata.create_all(engine)
Session.configure(bind=engine)
