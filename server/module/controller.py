from server import api
from flask_restful import Resource
from flask_restful import reqparse

requestTotal = 0

class Normal(Resource):
    def get(self):
        global requestTotal
        requestTotal += 1
        print(requestTotal)
        return {"data" : requestTotal}

api.add_resource(Normal, "/")
