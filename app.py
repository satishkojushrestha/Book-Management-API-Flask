from flask import Flask, request
from flask_restful import Resource, Api
from book_model import BookModel 

app = Flask("BookManagementAPI")
api = Api(app)

obj = BookModel()

@app.route('/<book_id>/')
def get(book_id):          
    return obj.book_getall_model(book_id)
    
@app.route('/create/<book_id>', methods=['POST'])    
def post(book_id):
    data = request.form  
    return obj.book_add_model(book_id, data)

@app.route('/delete/<book_id>', methods=['DELETE'])
def delete(book_id):      
    return obj.book_delete_model(book_id) 

@app.route('/update/<book_id>', methods=['PUT'])
def put(book_id):
    data = request.form  
    return obj.book_update_model(book_id, data)

if __name__ == '__main__':
    app.run()