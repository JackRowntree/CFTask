from flask import Flask, json, Response
from flask_restful import Resource, Api
from helpers import get_first_chunk, log

app = Flask(__name__)
api = Api(app)



class ReadFirstChunk(Resource):
	@log
	def get(self):
		return Response(
        response=json.dumps({
            "data": get_first_chunk()
        }),
        status=200,
        mimetype="application/json"
    )

api.add_resource(ReadFirstChunk, '/read/first-chunk')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')