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


@app.route("/")
def index():
    print(app.config['SECRET_KEY'])
    return "hello world"


# if __name__ == '__main__':
#     # Run the debugging server provided by flask
#     # app.run()
#     app.run(host="0.0.0.0", port=5000, debug=True)

# flask run <===> python -m flask run