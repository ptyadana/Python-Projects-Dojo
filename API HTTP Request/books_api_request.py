import json
import urllib3

http = urllib3.PoolManager()
request = http.request('GET','https://booksbyptyadana.herokuapp.com/books')
data = request.data

print(request.status)

if len(data) > 0:
    book_dict = dict()
    books = json.loads(data.decode('utf-8'))
    for book in books:
        book_dict[book['book_name']]= book['author_name']
    print(book_dict)
else:
    print('no data received.')