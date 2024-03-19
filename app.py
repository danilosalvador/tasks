from flask import Flask

#__name__ = "__main__" > quando executado de forma manual e  não está sendo importado por outro arquivo
app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello world!!!"

@app.route("/about")
def about():
    return "Sobre"

if __name__ == "__main__":
    app.run(debug=True)
