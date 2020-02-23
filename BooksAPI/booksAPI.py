#Returns a dictionary with book details
def get_book_details(book_name):
    from BooksAPI import googlebooks
    api = googlebooks.Api()
    api_result = api.list('intitle:'+book_name)
    if 'items' not in api_result.keys():
        return None
    required_fields=['title','description','publisher','averageRating']
    result={}
    for field in required_fields:
        if field in api_result['items'][0]['volumeInfo'].keys():
            result[field]=api_result['items'][0]['volumeInfo'][field]
    result['authors']=str(','.join(api_result['items'][0]['volumeInfo']['authors']))
    result['image']=api_result['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    return result

books=['Sapiens','The gone girl','Little women','Harry Potter and the chamber of secrets','Life of pi']
for book in books:
    print(get_book_details(book))