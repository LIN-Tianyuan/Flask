from flask import Flask, render_template, make_response, request, session

app = Flask(__name__)


class DefaultConfig(object):
    SECRET_KEY = 'fih9fh9eh9gh2'


app.config.from_object(DefaultConfig)


@app.route('/')
def home():
    m_int = 123
    m_str = 'alex'

    data = dict (
        my_int=123,
        my_str='alex'
    )
    # return render_template('index.html', my_str=m_str, my_int=m_int)
    return render_template('index.html', **data)


@app.route('/demo')
def demo():
    return 'Status code is 666', 666, {'Name': 'Alex'}


@app.route('/cookie')
def set_cookie():
    resp = make_response('set cookie ok')
    resp.set_cookie('username', 'alex')
    return resp


@app.route('/get_cookie')
def get_cookie():
    resp = request.cookies.get('username')
    return resp


@app.route('/set_session')
def set_session():
    session['username'] = 'alex'
    return 'Set session ok'


@app.route('/get_session')
def get_session():
    username = session.get('username')
    return 'Get session username {}'.format(username)


if __name__ == '__main__':
    app.run()