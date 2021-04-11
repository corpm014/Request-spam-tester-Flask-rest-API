from flask import Flask
from flask_restful import Api
import logging

app = Flask(__name__)
api = Api(app)
log = logging.getLogger('werkzeug')
log.disabled = True

from server.module import controller