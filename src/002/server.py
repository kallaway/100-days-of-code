# __dunder__ this is called a dunder
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. 
# Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home   ():
    return render_template("index.html")

@app.route("/404")
def error   ():
    return render_template("error.html")