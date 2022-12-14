from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restful import Resource, Api

app = Flask(__name__) 
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost:5432/my_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
ma = Marshmallow(app)

class UserTrades(db.Model):
	person_id,first_name,last_name,email,date_added
    person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    date_added = db.Column(db.String(32))
    trade = db.Column(db.String(32))

    def __init__(self, person_id, first_name, last_name, date_added, trade):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_added = date_added
        self.trade = trade

class UserSchema(ma.Schema):
    class Meta:
        fields = ('person_id', 'first_name', 'last_name', 'date_added', 'trade')

user_trades_schema = UserTrades() 
users_trades_schema = UserTrades(many=True)

class PeopleTradesManager(Resource): 
    @staticmethod
	def get():
	    try: id = request.args['person_id']
	    except Exception as e:
	    	id = None
	    if not id:
	        users = UserTrades.query.all()
	        return jsonify(users_trades_schema.dump(users))
	    user = UserTrades.query.get(id)
	    return jsonify(user_trades_schema.dump(user))

api.add_resource(PeopleTradesManager, '/api/users')

if __name__ == '__main__':
    app.run(debug=True)