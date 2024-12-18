# Project management
## 1. Environment Installation
### Virtual environments and the pip command
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
## 2. Flask Programming
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

## 3. Parameter description
### 3.1 Flask object initialization parameters
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

**Default parameter case**
```python
app = Flask(__name__)
```
File catalog
```bash
----
  |---static
  |     |--- 1.png
  |---helloworld.py
```
Visit `127.0.0.1:5000/static/1.png` to access the image

**Parameter modification case**
```python
app = Flask(__name__, static_url_path='/url_path_param', static_folder='folder_param')
```
File catalog
```bash
----
  |---folder_param     # Catalog name changes here
  |     |--- 1.png
  |---helloworld.py
```
Visit `127.0.0.1:5000/url_path_param/1.png` in order to access the image

### 3.2 Application Configuration Parameters
**Role**

Centralized management of all configuration information for the project

**Usage**

Unlike Django, which puts all configuration information in the settings.py file.

Flask saves the configuration information into the `app.config` property, which can be manipulated by dictionary type.

**Read**

- `app.config.get(name)`

- `app.config[name]`

**Set up**
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
- Advantages: Inheritance, reuse
- Disadvantages: Exposure of sensitive data
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
- Advantages: Separate files Protect sensitive data
- Disadvantages: Fixed file paths Inflexible
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
- Advantages: Separate files Protection of sensitive data Variable file paths Flexibility
- Disadvantages: Inconvenient. Remember to set environment variables
  
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
### 3.3 Common approaches in projects
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
### 3.4 app.run parameter
Can specify the IP address of the running host, port, and whether to enable debug mode.

`app.run(host="0.0.0.0", port=5000, debug=True)`

About DEBUG debugging mode:
- The server can be restarted automatically after the program code is modified.
- When the server error occurs, we can directly return the error information to the front-end for display.

## 4. Development server startup method
Flask has adjusted the startup of the development server from the code writing `app.run()` statement to the command `flask run` startup.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

# There is no need to write app.run() in the program
```
### 4.1 Terminal Launch
```bash
$ export FLASK_APP=helloworld
$ flask run
 * Running on http://127.0.0.1:5000/
```
**Description**

- The FLASK_APP environment variable specifies the instance where flask is started.
- `flask run -h 0.0.0.0 -p 8000` Bind address port
- `flask run --help` Get help
- Control of production and development modes
- Indicated by the `FLASK_ENV` environment variable
    - `export FLASK_ENV=production`
        - Runs in production mode, or defaults to that mode if not specified.
    - `export FLASK_ENV=development`
        - Runs in development mode.

**Extensions**
```bash
$ export FLASK_APP=helloworld
$ python -m flask run
  * Running on http://127.0.0.1:5000/
```
### 4.2 Pycharm Launch
![set_up_env](../image_md/env.png)
![set_up_env2](../image_md/env2.png)