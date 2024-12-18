from flask import Flask


# Configuration object method of loading configuration information
# class DefaultConfig(object):
#     """Default configuration"""
#     SECRET_KEY = 'chjosjospolpldplsdowjodwjodkwopkp2k4'


app = Flask(__name__)   # Flask (module name string type)
# set up
# app.config.from_object(DefaultConfig)
app.config.from_pyfile('setting.py')


@app.route('/')
def index():
    # Read configuration information
    print(app.config['SECRET_KEY'])
    return 'hello world'


if __name__ == '__main__':
    app.run()