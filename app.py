from flask import Flask, request
from flask_restful import Resource, Api
from book_model import BookModel 

app = Flask("BookManagementAPI")
api = Api(app)

obj = BookModel()

class Book(Resource):

    def get(self, book_id):          
        return obj.book_getall_model(book_id)
        
    def post(self, book_id):
        data = request.form  
        return obj.book_add_model(book_id, data)

    def delete(self, book_id):      
        return obj.book_delete_model(book_id) 

    def put(self, book_id):
        data = request.form  
        return obj.book_update_model(book_id, data)

api.add_resource(Book, '/<book_id>/')

if __name__ == '__main__':
    app.run()