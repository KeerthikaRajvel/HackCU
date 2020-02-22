#Returns a dictionary with book details
import googlebooks
api = googlebooks.Api()
api_result = api.list('intitle:Harry Potter and the chamber of secrets')
required_fields=['title','description','publisher','averageRating']
result={}
for field in required_fields:
    result[field]=str(api_result['items'][0]['volumeInfo'][field])
result['authors']=str(','.join(api_result['items'][0]['volumeInfo']['authors']))
result['image']=api_result['items'][0]['volumeInfo']['imageLinks']['thumbnail']
print(result)