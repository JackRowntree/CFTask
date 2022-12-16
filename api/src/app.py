from flask import Flask, json, Response
from flask_restful import Resource, Api
from helpers import get_first_chunk, log

app = Flask(__name__)
api = Api(app)


class ReadFirstChunk(Resource):
	"""
	Defines API response to return head of data
	"""
	@log
	def get(self):
	    return Response(
	        response=json.dumps({"data": get_first_chunk()}),
	        status=200,
	        mimetype="application/json",
	    )


api.add_resource(ReadFirstChunk, "/read/first-chunk")


def create_app():
	"""
	Sets Flask app for api and returns app object
	"""
	api.init_app(app)
	return app


if __name__ == "__main__":
	APP = create_app()
	APP.run(debug=True, host="0.0.0.0")
