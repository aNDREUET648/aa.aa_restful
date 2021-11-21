
from flask import Flask, escape, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import random 
from lorem_text import lorem

app = Flask(__name__)
api = Api(app)

book_collection = [lorem.words(random.randint(4,10)) for i in range(100)]

class Book(Resource):    #return a list of book-ids
  def get(self):       
    return jsonify(ids=list(range(len(book_collection))))

class GetBook(Resource): #return the title of a book
  def get(self,book_id):       
    return jsonify(id=book_id,title=book_collection[int(book_id)])

api.add_resource(Book, '/books') 
api.add_resource(GetBook, '/book/<book_id>') 

if __name__ == '__main__':
    app.run(port='9999', debug=True)
