import json

from flask import Flask


def create_flask_app(config):
    """
    Factory Functions for Building Flask Objects
    :param config: Configuration objects
    :return: Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config)

    # Configuration information read from a configuration file pointed to by an environment variable overrides parameters of the same name loaded from a configuration object
    app.config.from_envvar("PROJECT_SETTING", silent=True)
    return app


class DefaultConfig(object):
    """Default config"""
    SECRET_KEY = 'alex'


class DevelopmentConfig(DefaultConfig):
    DEBUG=True


# app = create_flask_app(DefaultConfig)
app = create_flask_app(DevelopmentConfig)


# @app.route("/")
# def index():
#     print(app.config['SECRET_KEY'])
#     return "hello world"

# print(app.url_map)    # -> Map object
# Requirement: need to traverse url_map, take out specific information and return it in a specific interface
# for rule in app.url_map.iter_rules():
#     print('name={} path={}'.format(rule.endpoint, rule.rule)) # name=static path=/static/<path:filename>

@app.route('/')
def route_map():
    rules_iterator = app.url_map.iter_rules()
    # {"static": "/static/", "route_map": "/"}
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})
# if __name__ == '__main__':
#     # Run the debugging server provided by flask
#     app.run()
#     app.run(host="0.0.0.0", port=5000, debug=True)

# flask run <===> python -m flask run