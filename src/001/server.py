from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World - From Flask"
@app.route("/goodbye")
def goodbye():
    print("Debugging this.")
    return "Goodbye World - From Flask"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='3000')

