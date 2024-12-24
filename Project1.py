import threading
from telnetlib import theNULL

import requests
import json

def save_to_json(url):
    r = requests.get(url)
    request = r.json()

    try:
        with open('products.json', 'w') as f:
            json.dump(request, f, indent=4)
        print('Successfully saved data to json file')

    except Exception as e:
        print(e)

def thread_function(url):
    r = requests.get(url)
    request = r.json()

    try:
        with open('posts.json', 'w') as f:
            json.dump(request, f, indent=4)
        print('Successfully saved data to json file')

    except Exception as e:
        print(e)

urls = [
    'https://dummyjson.com/products',
    'https://jsonplaceholder.typicode.com/posts'
]

thread = threading.Thread(target=save_to_json, args=(urls[0], ))
thread2 = threading.Thread(target=thread_function, args=(urls[1], ))

thread.start()
thread2.start()
thread2.join()
thread.join()