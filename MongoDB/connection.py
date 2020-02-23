from pymongo import MongoClient

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
    for record in list(records):
        result.append({"_id":record["_id"],"image":record["image"]})
    return result

def search(title):
    client = MongoClient("mongodb+srv://HackCU:girlpower@book-barter-erinp.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("BookBarter_Overall") #Database
    records = db.book_info #Collections
    print(list(records.find({"title": "Sapiens"})))
    return records.find({"title": "Sapiens"})
