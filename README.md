# Flask In Depth

## Set Up Virtual Environment (recommended)

```sh
pip install virtualenv
virtualenv venv
cd venv/bin
source venv/bin/activate(.fish|.zsh|.py) # will name (venv) if active
# `devactivate` # To leave
```

## Installation

```sh
pip freeze > reqiurements.txt # save dependencies
python; import flask; exit() # if no error, installed correctly
pip install -r requirements.txt # install all requirments
pip list --local # List installed packages in current virtual environment
sh start.sh # contents below
  # export FLASK_APP=flaskblog.py
  # export FLASK_DEBUG=1
  # flask run
```

## Project Structure

```sh
.
├── flaskblog.py # Flask entry point
├── requirements.txt # Manifest of dependencies
├── start.sh # Sets env vars and starts the app
├── static # Static CSS, JS, images
├── templates # Jinja2 templates
│   └── **/*.html
└── venv
    └── # virtualenv dir (optional)
```