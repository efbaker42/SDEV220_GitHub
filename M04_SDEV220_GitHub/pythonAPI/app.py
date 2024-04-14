"""Elizabeth Baker
13APR2024
SDEV 220 35N
Watch: https://www.youtube.com/watch?v=qbLc5a9jdXo&ab_channel=CalebCurry
Create a CRUD API for a BOOK.
Use these parameters:
-id
-book_name
-author
-publisher"""

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer,primary_key = True) #in an ideal world, this would instead be an ISBN
    book_name = db.Column(db.String(120),nullable = False) #some books may have the same names
    author = db.Column(db.String(120),nullable = False) #anonymous if no author
    publisher = db.Column(db.String(120),nullable = False) #books with no publisher marked as self-published

    def __repr__(self):
        return f"{self.book_name} by {self.author}, published by {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name':book.book_name, 'author':book.author,'publisher':book.publisher} #remember book refers to the variable book that queries are passed to, not the Books class
        output.append(book_data)

    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'name':book.book_name, 'author':book.author,'publisher':book.publisher}

@app.route('/books',methods=['POST'])
def add_book():
    book=Book(book_name=request.json['name'],author=request.json['author'],publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id':book.id} #I'm keeping this so I can get the id number and verify that the book was entered correctly after a successful POST

@app.route('/books/<id>',methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return{"error": "Not found."}
    db.session.delete(book)
    db.session.commit()
    return{"message":"Entry deleted."}