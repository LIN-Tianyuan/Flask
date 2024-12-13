# Flask
## Introduction to Flask
### Flask
Flask was born in 2010, is Armin ronacher (human name) in Python language based on the Werkzeug toolkit written lightweight web development framework.

Flask itself is equivalent to a kernel , almost all other features have to use extensions ( mail extension Flask-Mail, user authentication Flask-Login, database Flask-SQLAlchemy), all need to use third-party extensions to achieve . For example, we can use Flask extensions to add ORM, form validation tools, file uploads, authentication, etc. Flask does not have a default database to use, we can choose MySQL, we can also use NoSQL.

Its WSGI toolkit using Werkzeug (routing module), the template engine uses Jinja2. These two are also the core of the Flask framework.

### Framework Comparison
#### Lightness of the framework
Heavyweight framework: to facilitate the development of business programs, provides a wealth of tools, components, such as Django

lightweight framework: only provide the core functions of the Web framework , free, flexible, highly customizable , such as Flask, Tornado

#### Comparison with Django
django provides:

 - django-admin to quickly create a project works directory

 - manage.py to manage project works

 - orm model (database abstraction layer)

 - admin backend to manage the site

 - Caching mechanism

 - File storage system

 - user authentication system

All of these, flask do not have, need to extend the package to provide.

### Common Expansion Packs
List of extensions: http://flask.pocoo.org/extensions/
 - Flask-SQLalchemy: manipulating databases;
 - Flask-script: inserting scripts;
 - Flask-migrate: managing migrated databases;
 - Flask-Session: session storage method specification;
 - Flask-WTF: forms;
 - Flask-Mail: mail;
 - Flask-Bable: provide internationalization and localization support, translation;
 - Flask-Login: authenticate user status;
 - Flask-OpenID: authentication;
 - Flask-RESTful: tools for developing REST APIs;
 - Flask-Bootstrap: integration of front-end Twitter Bootstrap framework;
 - Flask-Moment: localized date and time;
 - Flask-Admin: a simple and extensible framework for managing interfaces

## project management
### Environment Installation
#### Virtual environments and the pip command
```bash
# Virtual environments
mkvirtualenv # Create virtual environment
rmvirtualenv # delete virtual environments
workon # enter virtual environment, view all virtual environments
deactivate # exit a virtual environment

# pip
pip install # Install dependent packages
pip uninstall # Uninstall dependencies
pip list # View installed dependencies
pip freeze # Freeze dependencies for the current environment.

# Create a Virtual Environment
python3 -m venv flask-env
source flask-env/bin/activate
# Install Flask
pip3 install flask
```
### Flask Programming
 - Create the helloworld.py file
```python
# Importing Flask Classes
from flask import Flask

# The Flask class takes one parameter, __name__.
app = Flask(__name__)


# Define the view
# The role of the decorator is to map routes to the view function index
@app.route('/')
def index():
    return 'hello world'


# The run method of a Flask application instance starts the WEB server.
if __name__ == '__main__':
    app.run()
```
 - run
```bash
python3 helloworld.py
 ```

### Parameter description
#### Flask object initialization parameters
When a Flask program instance is created, it needs to be passed the package (module) specified by the current Flask program by default.

 - import_name
   - The package (module) that the Flask program is in. Pass `__name__` and you're done.
   - This determines the path Flask looks for when accessing static files.
 - static_url_path
   - static_url_path, can be passed without, the default is: `/ + static_folder`
 - static_folder
   - The folder where static files are stored, can be left out, default is `static`.
 - template_folder
   - The folder where template files are stored, can not be passed, default is `templates`.
#### Application Configuration Parameters
Unlike Django, which puts all configuration information in the settings.py file.

Flask saves the configuration information into the `app.config` property, which can be manipulated by dictionary type.

Read

 - `app.config.get(name)`

 - `app.config[name]`

Set up
1. Load from Configuration Object
`app.config.from_object(configuration object)`
```python
class DefaultConfig(object):
    SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'

app = Flask(__name__)

app.config.from_object(DefaultConfig)

@app.route("/")
def index():
    print(app.config['SECRET_KEY'])
    return "hello world"
```
 - Application Scenario: 
   - Written as a default configuration in program code
 - Benefits: Inheritance, reuse
 - Cons: Exposure of sensitive data
2. Load from configuration file
`app.config.from_pyfile(config file)`
```python
# setting.py
SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'

# flaskprogram.py
app = Flask(__name__)

app.config.from_pyfile('setting.py')

@app.route("/")
def index():
    print(app.config['SECRET_KEY'])
    return "hello world"
```
 - Application Scenario:
    - Use a fixed configuration file in the project
 - Benefits: Separate files Protect sensitive data
 - Cons: Fixed file paths Inflexible
3. Load from environment variables
`app.config.from_envvar('environment variable name')`
   
The essence of Flask's use of environment variables to load configurations is to find the configuration file through the environment variable values and then read the configuration file's information.
```bash
# The value of the environment variable is the absolute path to the configuration file
export PROJECT_SETTING='~/setting.py'
```
```python
app = Flask(__name__)

app.config.from_envvar('PROJECT_SETTING', silent=True)

@app.route("/")
def index():
    print(app.config['SECRET_KEY'])
    return "hello world"
```
- Application Scenario:
    -  The address of the configuration file is not fixed;
    - Don't want to expose the real configuration file address in the code, and only have information about the real configuration file on the server running the code.
- Benefits: Separate files Protection of sensitive data Variable file paths Flexibility
- Cons: inconvenient Remember to set environment variables
A note about silent:

Indicates whether to throw an exception if the corresponding value is not set in the system environment variable
 - False means no silent processing, no value error notification, the default is False.
 - True means silent processing, even if there is no value, let Flask run normally.

Setting and reading environment variables on a Linux system is done as follows:
```bash
export variable name = variable value # set
echo $variable name # read

# For example
export language=python
echo $language
```
#### Common approaches in projects
Creating a Flask app using the factory pattern and loading configuration using a combination of configuration objects and environment variables
 - Use configuration objects to load the default configuration
 - Use environment variables to load sensitive configuration information that you don't want to see in your code.
```python
from flask import Flask


def create_flask_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.config.from_envvar("PROJECT_SETTING", silent=True)
    return app


class DefaultConfig(object):
    SECRET_KEY = 'alex'


class DevelopmentConfig(DefaultConfig):
    DEBUG=True

    
app = create_flask_app(DevelopmentConfig)

@app.route("/")
def index():
    print(app.config['SECRET_KEY'])
    return "hello world"
```
#### app.run parameter
`app.run(host="0.0.0.0", port=5000, debug=True)`

About DEBUG debugging mode:
 - The server can be restarted automatically after the program code is modified.
 - When the server error occurs, we can directly return the error information to the front-end for display.

### Development server startup method
#### Terminal Launch
```bash
$ export FLASK_APP=helloworld
$ flask run
 * Running on http://127.0.0.1:5000/
```
Description

 - The FLASK_APP environment variable specifies the instance where flask is started.
 - flask run -h 0.0.0.0 -p 8000 bind address port
 - flask run --help Get help.
 - Control of production and development modes
 - Indicated by the FLASK_ENV environment variable
   - export FLASK_ENV=production 
     - Runs in production mode, or defaults to that mode if not specified.
   - export FLASK_ENV=development 
     - Runs in development mode.

Extensions
```bash
$ export FLASK_APP=helloworld
$ python -m flask run
  * Running on http://127.0.0.1:5000/
```
#### Pycharm Launch
![set_up_env](image_md/env.png)
![set_up_env2](image_md/env2.png)