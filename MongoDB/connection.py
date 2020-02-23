from pymongo import MongoClient
from BooksAPI import booksAPI

def insert_user(user_details):
    client = MongoClient("mongodb+srv://HackCU:girlpower@book-barter-erinp.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("BookBarter_Overall")  # Database
    records = db.accounts  # Collections
    records.insert(user_details)

def get_books():
    client = MongoClient("mongodb+srv://HackCU:girlpower@book-barter-erinp.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("BookBarter_Overall")  # Database
    records = db.book_info  # Collections
    result=[]
    for record in list(records.find()):
        result.append({"title":record["title"],"image":record["image"],"authors":["authors"]})
    print(result)
    return result

def add_book(book):
    client = MongoClient("mongodb+srv://HackCU:girlpower@book-barter-erinp.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("BookBarter_Overall")  # Database
    records = db.book_info  # Collections
    records.insert(booksAPI.get_book_details(book))

def search(book):
    client = MongoClient("mongodb+srv://HackCU:girlpower@book-barter-erinp.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("BookBarter_Overall") #Database
    records = db.book_info #Collections
    return records.find({"title": book})
