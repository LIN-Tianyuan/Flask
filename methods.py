import json

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    return "hello world"


if __name__ == '__main__':
    app.run()