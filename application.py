from flask import Flask, render_template
app=Flask(__name__)
def index():
names=["Mohamed","Driss","Rachida","Fatima","Ismail",]
return render_template("index.html",names=names)
