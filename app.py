from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "hello world"


@app.route("/about")
def about():
    return "<h1>this is about page</h1>"

if __name__ == "__main__":
    app.run(debug=True)

