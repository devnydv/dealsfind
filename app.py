from flask import Flask, render_template, request
import os
import json
from bs4 import BeautifulSoup
import requests
from hitapi import hitfirebase, getdeals
from getdetails import getfirebase


f = open("data.json", "r")
menudata= f.read()
menudata = json.loads(menudata)
menudata = menudata["id1"]
app = Flask(__name__)

@app.route("/")
def hello_world():
    
    cate = request.args.get("category")
    if cate == None:
        cate = "electronics"
        
        itemdata = hitfirebase(cate)
        itemdata.reverse()
    else:
        cate = cate.replace("-", " ")
        #print(cate)
        itemdata = hitfirebase(cate)
        itemdata.reverse()
    return render_template("home.html", cate = cate, data= menudata, itemdata = itemdata)
    

@app.route("/details")
def detail():
    id = request.args.get("id")
    cate = request.args.get("category")
    cate = cate.replace("-", " ")
    
    itemdata = getfirebase(cate, id)
    #print(itemdata)
    return render_template("details.html", data = menudata, id=id, cate= cate, itemdata = itemdata)

@app.route("/deals")
def deals():

    url = "https://inrdeals.com/ajax/deals/engine?page=1&user=bit422097711"
    #url = "https://www.flipkart.com/realme-c53-champion-black-128-gb/p/itm5df90168ecd05?pid=MOBGTEVGGM7CTGXU"
    head = ({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language":"en-US , en;q=0.5"
})
    data = requests.get(url, headers=head)
    soup = BeautifulSoup(data.content, "html.parser")
    return render_template("deals.html", deals= soup)


#if __name__ == "__main__":
    #app.run(debug=True)
