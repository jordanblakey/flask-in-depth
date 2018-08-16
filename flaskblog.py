from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
  app.run(debug=True)
