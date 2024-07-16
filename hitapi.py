import requests

def hitfirebase(cate):
    cate = cate.title()
    db= "https://filmyapp-e1005.firebaseio.com/short/itemdata/" + cate +".json"
    response = requests.get(db)
    itemdata = response.json()
    #print(db)
    itemdata = itemdata["items"]
    return itemdata

def getdeals():
    res= requests.get("https://inrdeals.com/ajax/deals/engine?page=1&user=bit422097711&token=")
    data  = res.text
    return data
