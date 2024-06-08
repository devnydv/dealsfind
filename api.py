import requests 
import json
def hit():
    arr = {"ad":"newdtest"}
    url = "https://getpantry.cloud/apiv1/pantry/afb58d33-1d0b-409c-beaa-f5f88ef0d91d/basket/newb"
    res = requests.post(url, json=arr)
