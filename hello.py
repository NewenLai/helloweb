from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hola():
    return "Hola, Mundo!"

@app.route("/bye")
def Adios():
    return "Adios, Mundo cruel"