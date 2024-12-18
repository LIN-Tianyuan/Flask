# Importing Flask Classes
from flask import Flask

# The Flask class takes one parameter, __name__.
app = Flask(__name__)   # Flask (module name string type)
# app = Flask(__name__, static_url_path='/s', static_folder='static_files')

# Define the view
# The role of the decorator is to map routes to the view function index
@app.route('/')
def index():
    return 'hello world'


# The run method of a Flask application instance starts the WEB server.
if __name__ == '__main__':
    app.run()