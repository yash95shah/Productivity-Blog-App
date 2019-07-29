from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style=font-family: times;>This is the first commit!</h1>"

@app.route("/about")
def about():
    return "This is just gonna have to work"


@app.route("/documentation")
def documentation():
    return "This is a sample documentation page"
if __name__ == '__main__':
    app.run(debug=True)
