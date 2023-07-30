from flask import Flask, render_template, request, session, redirect, url_for
import csi5302 as cfg
import os
from models import db
import models
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from urls import other_routes
from datetime import timedelta


# Replace the following placeholders with your database details
DB_HOST = cfg.mysql['location']  # Or the appropriate driver for your database
DB_USER = cfg.mysql['user']
DB_PASSWORD=  cfg.mysql['password']
DB_NAME = cfg.mysql['database']


#startapp and configure settings
app = Flask(__name__)
app.secret_key = os.urandom(253) #secret keys are helpful to encrpty and protect data
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
app.config['SESSION_PROTECTION'] = 'strong'
#added more security I think. Cookies for sessions should be seen by client.
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return models.users.query.get(int(user_id))

def is_logged_in():
    return 'username' in session

#include the other routes such that this page doesnt get cluttered.
other_routes(app, db)

#start with the login page
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = str(request.form.get("username"))
        password = str(request.form.get("password"))
        
    
        user = models.users.query.filter_by(username=username).first()
        #if the username is in my database
        if user:
            # check the password
            correct_pass = check_password_hash(user.password, password)
            session['username'] = user.username
            session['usertype'] = user.usertype
            if correct_pass:
                #route to the dashboard and login
                login_user(user)
                if user.usertype == 'admin':
                    return redirect(url_for('admindashboard'))
                
                return redirect(url_for("userdashboard"))
            else:
                return render_template("login.html", message="Incorrect Password")
        else:
            return render_template("login.html", message="User not found")

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)