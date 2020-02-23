from pymongo import MongoClient

def search(title):
    client = MongoClient("mongodb+srv://HackCU:girlpower@book-barter-erinp.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("BookBarter_Overall") #Database
    records = db.book_info #Collections
    print(list(records.find({"title": "Sapiens"})))
    return records.find({"title": "Sapiens"})