from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '8e54af86ebd2a0e82932'
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


@app.route("/registration")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title= 'Login', form=form)




if __name__ == '__main__':
    app.run(debug=True)
