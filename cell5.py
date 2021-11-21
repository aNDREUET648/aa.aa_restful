
from flask import Flask, escape, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

import random 
from lorem_text import lorem

app = Flask(__name__)
api = Api(app)

book_collection = [lorem.words(random.randint(4,10)) for i in range(100)]

class Books(Resource): 
  def get(self):       
    #return jsonify(ids=list(range(len(book_collection))))
    return jsonify({"titulo": book_collection})

class Book(Resource): 
  def get(self,book_id):       
    return jsonify(book_collection[int(book_id)])

  def post(self): #POST Method
    json_data = request.get_json(force=True) #obtain the data forcing JSON-type
    booktitle = json_data["title"]           #get the title key
    book_collection.append(booktitle)        #add the title in the collection
    new_id = len(book_collection)            #generate a new ID
    return jsonify({"id":new_id,"titulo":booktitle})                #return the ID

api.add_resource(Books, '/books') 

api.add_resource(Book, '/book/<book_id>','/addbook/') #BOTH METHODS.

if __name__ == '__main__':
    app.run(port='9999', debug=True)
