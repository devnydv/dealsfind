import requests

def getfirebase(cate, id):
    cate = cate.title()
    db = "https://filmyapp-e1005.firebaseio.com/shopsy/itemdata/" +cate +"/items.json"
    #db= "https://filmyapp-e1005.firebaseio.com/short/itemdata/" + cate +".json"
    response = requests.get(db)
    itemdata = response.json()
    #print(db)
    titarray = []
    for file, val in itemdata.items():
        titarray.append(file)
    #titarray.reverse()
    id = int(id)
    title = titarray[id]
    itemdata = itemdata[title]
    return itemdata
