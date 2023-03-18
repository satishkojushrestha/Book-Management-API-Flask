from mysql import connector

class BookModel():

    def __init__(self):
        #Connection establishment code
        try:
            self.conn = connector.connect(host="localhost", user="root", password="", database="flask")
            self.conn.autocommit = True
            self.cur = self.conn.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("Error while connecting...")
            
    def book_getall_model(self, book_id):
        #Query execution code
        if book_id == "all":
           self.cur.execute(f"SELECT * FROM books")
        else:
            self.cur.execute(f"SELECT * FROM books WHERE bookid LIKE '{book_id}'")
        result = self.cur.fetchall()
        if len(result) > 0:         
            return result   
            # return json.dumps(result)
        else:
            return "No Data Found"
        
    def book_add_model(self, bookid, data):
        #Query execution code
        self.cur.execute(f"INSERT INTO books(bookid, title, doi) VALUES('{bookid}','{data['title']}','{data['doi']}')")
        return "Book Successfully Added"
    
    def book_update_model(self, book_id, data):
        #Query execution code
        self.cur.execute(f"UPDATE books SET title='{data['title']}', doi='{data['doi']}' WHERE bookid LIKE '{book_id}'")
        if self.cur.rowcount > 0:
            return "Book Successfully Updated"
        else:
            return "Nothing to Update"
    
    def book_delete_model(self, book_id):
        #Query execution code
        self.cur.execute(f"DELETE FROM books WHERE bookid LIKE '{book_id}'")
        if self.cur.rowcount > 0:
            return "Book Deleted Successfully"
        else:
            return "Nothing to Update"
    
