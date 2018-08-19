# Flask In Depth

## Set Up Virtual Environment (recommended)

```sh
pip install virtualenv
virtualenv venv
cd venv/bin
source venv/bin/activate(.fish|.zsh|.py) # will name (venv) if active
# `deactivate` # To leave
```

## Installation

```sh
pip install -r requirements.txt # install all requirments
pip freeze > reqiurements.txt # save dependencies
python; import flask; exit() # if no error, installed correctly
pip list --local # List installed packages in current virtual environment
python run.py
```

## Project Structure

```sh
.
├── flaskblog
│   ├── forms.py # WTForm definitions
│   ├── __init__.py # Init app, init ORM, import routes
│   ├── models.py # SQLAlchemy models
│   ├── routes.py # Route definitions, import models
│   ├── static/ # Static CSS, JS, images
│   └── templates/ # Jinja2 templates
├── requirements.txt # Manifest of dependencies
├── run.py # Flask entry point
└── venv/ # virtualenv dir (optional)
```

## Flask Snippets

```py
# ALL ##########################################################
# BASE: hw | route | routegp | routep |
# APP: fapp | froute | furl | fmeth | frt | ftreq | fup | fsup | frc | fsc | feh | flog
# TEMPLATING: fexp | ffilter | fcomment | fblock | fextends | fself | fsuper | ffor | fif | fife | felif | fmacro | ffb | fset | finclude | fimport | fautoescape | furl
```

## SQLAlchemy Commands

```py
# import ORM instance from module
>>> from flaskblog import db
# Create tables as defined by ORM instance
>>> db.create_all()
>>> from flaskblog import User, Post
# Create ORM row instance
>>> user_1 = User(username='test', email='test@test.test', password='test')
# Create ORM row instance
>>> post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
# Stage changes in memory
>>> db.session.add(user_1)
>>> db.session.add(post_1)
# Write changes to database
>>> db.session.commit()
# Discard uncommited changes from session (error handling)
>>> db.session.rollback()
# SELECT * FROM user
>>> User.query.all()
# SELECT * FROM user WHERE * username = 'test'
>>> User.query.filter_by(username='test').all()
# SELECT * FROM user LIMIT 1
>>> User.query.first()
# SELECT * FROM user WHERE * username = 'test' LIMIT 1
>>> user = User.query.filter_by(username='test').first()
# 1
>>> user.id
# Shows hashed password
>>> user.password
# query by id
>>> user = User.query.get(1)
# Collection of Post instances (db rows)
# Loop through rows and print all (note posts mapped with user.id:post.user_id)
>>> for post in user.posts:
# uses backref="author" from User class
# Note post table has no column 'author', while post.user_id is the foreign key used to get the 'author' row
...     print(post.author, post.user_id)
# Delete a row/rows stored from query
>>> db.session.delete(user)
>>> db.session.commit()
# flush the database
>>> db.drop_all()
# create tables again in empty state
>>> db.create_all()
```

## Password Hashing With BCrypt

```py
>>> from flask import Bcrypt
>>> bcrypt = Bcrypt()
# Generates a different hash every time, preventing hash table attacks
>>> hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
>>> bcrypt.check_password_hash(hashed_pw, 'password') # False
>>> bcrypt.check_password_hash(hashed_pw, 'testing') # True
```

## SQLite3 Basics

### Basic Operation Config

```sh
sqlite3 #open the cli tool
.exit # exit the cli tool
.open <filename.db> #open local database
.show # print all SQLite config options
.mode column # Pretty print stdout as columns
.headers (on|off) # In col view, toggle column headers
```

### Recon

```sh
.database #list the current database
.databases #list all databases (in the current directory?)
.schema #print out the db schema
.schema <tablename> # print the schema for a single table
.indexes # print all indexes in the current database
.indexes <tablename> # print all indexes in a single table
.tables #list all tables
.table <tablename> #check for the existence of table
```

### Queries

```sh
.output post.txt
SELECT \* FROM post LIMIT 10; #output query results to file.
'SELECT \* FROM post LIMIT 10;' > commands.txt; sqlite3;
.open <filename.db>
.read commands.txt # Read SQL statements from a file.
```
