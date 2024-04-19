import requests

def hitfirebase(cate):
    cate = cate.title()
    db= "https://filmyapp-e1005.firebaseio.com/short/itemdata/" + cate +".json"
    response = requests.get(db)
    itemdata = response.json()
    #print(db)
    itemdata = itemdata["items"]
    return itemdata