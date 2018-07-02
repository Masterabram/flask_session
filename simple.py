from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login")
def login():
    return "Priss priss login here!"


if __name__ == '__main__':
    app.run(debug=True, port=5052)
