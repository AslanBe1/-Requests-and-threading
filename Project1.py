import threading
import requests
import json

url = 'https://dummyjson.com/products'
r = requests.get(url)
request = r.json()

def save_to_json(url):
    try:
        with open('products.json', 'w') as f:
            json.dump(request, f, indent=4)
            print('Successfully saved data to json file')

    except Exception as e:
        print(e)

def thread_function():
    save_to_json(url)

thread = threading.Thread(target=thread_function)
thread.start()
thread.join()