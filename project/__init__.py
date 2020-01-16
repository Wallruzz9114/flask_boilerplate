from flask import Flask
from flask_restplus import Resource, Api

# Instanciate the app
app = Flask(__name__)

api = Api(app)

# Set config
app.config.from_object("project.config.DevelopmentConfig")


class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


api.add_resource(Ping, "/ping")
