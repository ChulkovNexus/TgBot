from flask import Flask

app = Flask(__name__)

from http_app import routes
