from flask import Flask, escape, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Book(Resource):    
  def get(self):         
    return {"book1":"HolaMundo"}  

api.add_resource(Book, '/books') 

if __name__ == '__main__':
    app.run(port='9999', debug=True)
