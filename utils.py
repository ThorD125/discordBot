import requests
import random
import string

def randomPass(amount):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=int(amount)))

def util_cat():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    response_json = response.json()
    return response_json[0].get("url")
