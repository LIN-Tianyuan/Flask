from flask import Flask, request, abort, current_app, g


app = Flask(__name__)

# redis-cli
app.redis_cli = 'redis client'


# /articles/?channel_id=123
@app.route('/articles')
def get_articles():
    channel_id = request.args.get('channel_id')
    print(app.redis_cli)
    if channel_id is None:
        abort(400)
    return 'You wanna get articles of channel {}'.format(channel_id)


from passport import bp
app.register_blueprint(bp)


def db_query():
    user_id = g.user_id
    user_name = g.user_name
    print('user_id={} user_name={}'.format(user_id, user_name))


@app.route('/')
def get_user_profile():
    g.user_id = 123
    g.user_name = 'alex'
    db_query()
    return 'hello world'

"""
app1 = Flask(__name__)
app2 = Flask(__name__)

# redis-cli
app1.redis_cli = 'redis client 1'
app2.redis_cli = 'redis client 2'


# /articles/?channel_id=123
@app1.route('/app1')
def get_articles():
    return '{}'.format(current_app.redis_cli)


@app2.route('/app2')
def get_articles():
    return '{}'.format(current_app.redis_cli)

"""
if __name__ == '__main__':
    app.run()