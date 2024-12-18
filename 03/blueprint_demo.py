import json

from flask import Flask, Blueprint

app = Flask(__name__)

# Creating Blueprint Objects
user_bp = Blueprint('user', __name__)


@user_bp.route('/profile')
def get_profile():
    return "user profile"


# Registration Blueprint
# app.register_blueprint(user_bp)
app.register_blueprint(user_bp, url_prefix='/user')

from goods import goods_bp
app.register_blueprint(goods_bp)

if __name__ == '__main__':
    app.run()
