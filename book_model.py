from mysql import connector
import json

class BookModel():

    def __init__(self):
        #Connection establishment code
        try:
            self.conn = connector.connect(host="localhost", user="root", password="", database="flask")
            self.cur = self.conn.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("Error while connecting...")
            
    def book_getall_model(self, book_id):
        #Query execution code
        self.cur.execute(f"SELECT * FROM books WHERE idbooks={book_id}")
        result = self.cur.fetchall()
        if len(result) > 0:         
            return result   
            # return json.dumps(result)
        else:
            return "No Data Found"
        
    def book_add_model(self, title, doi):
        #Query execution code
        self.cur.execute(f"INSERT INTO books(title, doi) VALUES('{title}','{doi}')")
        result = self.cur.fetchall()
        if len(result) > 0:         
            return result   
            # return json.dumps(result)
        else:
            return "No Data Found"