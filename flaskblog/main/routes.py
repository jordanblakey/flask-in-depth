from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

# MAIN ########################################################################


@main.route('/')
@main.route('/home')  # Second route decorator for multiple redirects
def home():
  # pass data into the template with a second argument
  page = request.args.get('page', 1, type=int)
 # Get newest posts first, paginate w/ page size of 5 and page # via URL param
  posts = Post.query.order_by(
      Post.date_posted.desc()).paginate(page=page, per_page=5)
  return render_template('home.html', posts=posts)


@main.route('/about')
def about():
  return render_template('about.html', title='About')


# ERRORS ######################################################################

@main.errorhandler(404)
def page_not_found(e):
  return render_template('errors/404.html'), 404


@main.errorhandler(403)
def page_not_found(e):
  return render_template('errors/403.html'), 403
