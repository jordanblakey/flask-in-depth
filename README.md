# Flask in depth

## Setting up Python Virtual Environment

```sh
pip install virtualenv
virtualenv venv
cd venv/bin
source activate # Should show name (venv) before prompt
# `devactivate` # To leave
cd ../../
pip install flask
python; import flask; # if no error, installed correctly
flask run
```

Most basic flask app:

```py
from flask import Flask
app = Flask(__name__)

@app.route("/") # Route decorator.
# Calls the below function on the defined route.
def hello():
  return "Hello World."
```

Set the FLASK_APP environment variable:

```sh
export FLASK_APP=flaskblog.py
export FLASK_DEBUG=1
```