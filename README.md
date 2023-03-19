# Simple Flask API

# Database
Database - MySQL
<br>DB Structure:
<br>
![image](https://user-images.githubusercontent.com/54971497/226119862-e97f040f-063b-4226-9ef4-d5b685db0bc6.png)
<br>
# Endpoints
Reading Data:<br>
/all/ - Shows all available data<br>
/book1/ - Shows book1 detail<br>

Creating:<br>
/create/book3/<br>

Updating:<br>
/update/book3/<br>

Deleting:<br>
/delete/book3/<br>

# Inserting, Updating, and Deleting using CURL:
Create:<br>
curl http://127.0.0.1:5000/create/book3 -d "title=Web 3.0" -d "doi=2021" -X POST<br>

Delete:<br>
curl http://127.0.0.1:5000/delete/book3 -X DELETE<br>

Update:<br>
curl http://127.0.0.1:5000/update/book3 -d "title=New Title" -d "doi=New Date of Issue" -X PUT
