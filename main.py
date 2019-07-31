from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
   { 'author' : 'Yash Shah', 'Designation' : 'Software Engineer' } ,
    {
        'author' : 'Amy Bernard',
    'Designation':'Software Engineer' },
     {
         'author' : 'Kieran Killian',
    'Designation':'Software Engineer' } ,
    {
        'author' : 'Mark Davis',
    'Designation':'Software Engineer' }
]

@app.route("/")
def home():
    return render_template('home.html',posts=posts )


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/documentation")
def documentation():
    return "This is a sample documentation page"
if __name__ == '__main__':
    app.run(debug=True)
