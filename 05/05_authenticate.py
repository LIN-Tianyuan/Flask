from flask import Flask, request, abort, current_app, g


app = Flask(__name__)


# Request hook (tries to determine the identity of the user, does not process for non-logged-in users, releases them)
# Use g object to save user identity information
@app.before_request
def authentication():
    """
    Use the before_request request hook to try to determine the user's identity before entering all views
    :return:
    """
    # This uses authentication mechanisms (e.g., cookie, session, jwt, etc.) to identify the user's identity information
    # if logged in user, user has identity information
    # g.user_id = 123
    # else If not logged in, user has no identity information.
    g.user_id = None


# Forced Login Decorator
def login_required(func):
    def wrapper(*args, **kwargs):
        # Determine whether a user is logged in or not
        if g.user_id is None:
            abort(401)
        else:
            # logged in
            return func(*args, **kwargs)

    return wrapper


@app.route('/')
def index():
    return 'home page user_id={}'.format(g.user_id)


@app.route('/profile')
@login_required
def get_user_profile():
    return 'user profile page user_id={}'.format(g.user_id)


if __name__ == '__main__':
    app.run()