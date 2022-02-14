from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Wagner"

if __name__ == '__main__':
    app.run()