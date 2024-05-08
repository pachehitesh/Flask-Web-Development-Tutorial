from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hitesh")
def harry():
    return "Hello hitesh bhai4!"
app.run(debug=True)
