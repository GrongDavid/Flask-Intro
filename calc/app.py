# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/')
def home():
    return "start"

@app.route('/<modifier>')
def calculate(modifier):
    if modifier == "add":
        return str(operations.add(int(request.args["a"]), int(request.args["b"])))
    if modifier == "sub":
        return str(operations.sub(int(request.args["a"]), int(request.args["b"])))
    if modifier == "mult":
        return str(operations.mult(int(request.args["a"]), int(request.args["b"])))
    if modifier == "div":
        return str(operations.div(int(request.args["a"]), int(request.args["b"])))
