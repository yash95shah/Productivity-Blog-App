from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1 style=font-famidddddddly: times;>This is the first commit!</h1> <p> You have only three lives. If you wish to continue, you need to form good habits! <br> <ul><li> Go strong </li> <li> Be bold </li>  <li> Take your chances </li></ul> "


@app.route("/about")
def about():
    return "< h3 style = font- family : helvetica ; > This is just gonna have to work < /h3 >"


@app.route("/documentation")
def documentation():
    return "This is a sample documentation page"
if __name__ == '__main__':
    app.run(debug=True)
