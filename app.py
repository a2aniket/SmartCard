from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
import pandas as pd    

@app.route("/")
def home():
   #with open('data.p', 'rb') as handle:
        #data = pickle.load(handle)
    df=pd.read_csv("bill.csv")
    total=df["total_price"].sum()
    unit_total=df["unit"].sum()
    Name=df["Name"]
    length=len(Name)
    description=df["description"]
    price=df["price"]
    unit=df["unit"]
    total_price=df["total_price"]
    image="Colgate.jpg"
    return render_template("home.html",image=image,length=length,Name=Name,description=description,price=price,unit=unit,total_price=total_price,total=total,unit_total=unit_total)
if __name__=="__main__":
    app.run(debug=True)