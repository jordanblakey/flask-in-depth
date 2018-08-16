from flask import (
    Flask,
    render_template,
    url_for,
    flash,
    redirect
)

from forms import(
    RegistrationForm,
    LoginForm
)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5d3fca38e18881324d5efe79c2e1373'

posts = [
    {
        'author': 'Jordan Blakey',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jordan Blakey',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },

]


@app.route('/')
@app.route('/home')  # Second route decorator for multiple redirects
def home():
  # pass data into the template with a second argument
  return render_template('home.html', posts=posts)


@app.route('/about')
def about():
  return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'test@test.com' and form.password.data == 'test':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form)


@app.errorhandler(404)
def page_not_found(e):
  return render_template('errors/404.html'), 404


if __name__ == '__main__':
  app.run(debug=True)
