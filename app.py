from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from book_model import BookModel 

app = Flask("BookManagementAPI")
api = Api(app)

obj = BookModel()

# parser = reqparse.RequestParser()
# parser.add_argument('title', required=True)

books = {
    'book1': {'title': 'Python 3.0','doi': '2011/1/1'},
    'book2': {'title': 'Web 3.0'}
}

class Book(Resource):

    def get(self, book_id):
        if book_id == "all":
            return books
        if book_id in books:
            return books[book_id]
        # if book_id not in books:
        #     abort(404, message=f"Book {book_id} not found")                
        return obj.book_getall_model(book_id)
        
    def put(self, book_id):
        # args = parser.parse_args()
        # new_book = {'title': args['title']}
        # books[book_id] = new_book
        title = request.form['title']
        doi = request.form['doi']        
        return obj.book_add_model(title, doi)

    def delete(self, book_id):
        if book_id not in books:
            abort(404, message=f"Book {book_id} not found")
        del books[book_id]
        return "", 204 

    def post(self, book_id):
        books[book_id] = request.form['data']
        return {book_id: books[book_id]},201

api.add_resource(Book, '/book/<book_id>')

if __name__ == '__main__':
    app.run()