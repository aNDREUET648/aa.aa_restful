from flask import Flask, escape, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify #install it

import random 

app = Flask(__name__)
api = Api(app)

class Book(Resource): 
  def get(self):       
    return jsonify(ids=[random.randint(0,100) for i in range(100)])

api.add_resource(Book, '/books') 

if __name__ == '__main__':
    app.run(port='9999', debug=True)
