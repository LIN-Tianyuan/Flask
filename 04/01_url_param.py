from flask import Flask, request, abort
from werkzeug.routing import BaseConverter

app = Flask(__name__)

app.config['name'] = 'python'


@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):
    return 'The divisor cannot be 0'


# /users/123
@app.route('/users/<user_id>')
def get_users_data(user_id):
    print(type(user_id))
    return 'get users {}'.format(user_id)


class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


app.url_map.converters['mobile'] = MobileConverter


@app.route('/sms_codes/<mobile:mob_num>')
def send_sms_code(mob_num):
    print(type(mob_num))
    return 'get users {}'.format(mob_num)


# /articles/?channel_id=123
@app.route('/articles')
def get_articles():
    channel_id = request.args.get('channel_id')

    if channel_id is None:
        abort(400)
    return 'You wanna get articles of channel {}'.format(channel_id)


@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['pic']
    # with open('./demo.png', 'wb') as new_file:
    #     new_file.write(f.read())
    f.save('./demo.png')
    return 'ok'


if __name__ == '__main__':
    app.run()