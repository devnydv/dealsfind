from flask import Flask, render_template, request
import os
import json
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
   
    return render_template("deals.html")

@app.route("/dealdata", methods = ["GET", "POST"])
def deal():
     if request.method == "POST":
        dealsdata = getdeals()
        return dealsdata


#if __name__ == "__main__":
    #app.run(debug=True)
