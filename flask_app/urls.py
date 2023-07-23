from flask import render_template, session, url_for, redirect
from flask_login import login_required
import models
from functools import wraps

#custom decorator for admin privaledges such that it prevents unauthorized users.
def admin_required(func):
    @wraps(func)
    #define positional arguments and keyword arguments
    def decorated_function(*args, **kwargs):
        print(session.get('usertype'))
        if session.get('usertype') == 'admin':
            return func(*args, **kwargs)

        return redirect(url_for('login'))
    return decorated_function\

#custom decorator for admin privaledges such that it prevents unauthorized users.
def user_required(func):
    @wraps(func)
    #define positional arguments and keyword arguments
    def decorated_function(*args, **kwargs):
        print(session.get('usertype'))
        if session.get('usertype') == 'user':
            return func(*args, **kwargs)

        return redirect(url_for('login'))
    return decorated_function


def other_routes(app):

    @app.route("/userdashboard", methods=["GET"])
    @login_required
    def userdashboard():
        username = session.get('username')
        return render_template('userdashboard.html', username=username)