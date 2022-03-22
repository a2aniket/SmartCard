from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
import pandas as pd    

@app.route("/")
def home():
    with open('bill.pkl', 'rb') as handle:
        b = pickle.load(handle)
    total=0
    units=0
    for i in b:
        total=total+b[i]['totalPrice']
        units=units+b[i]['unit']
    
    
    return render_template("home.html",bill=b,units=units,total=total)
if __name__=="__main__":
    app.run(debug=True, host= '192.168.15.167')
