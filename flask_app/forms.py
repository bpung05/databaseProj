from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
class AddUserForm(FlaskForm):
    username = StringField('UserName:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    accounttype = SelectField('Account Type:', choices=[('user', 'User'), ('admin', 'Admin')], validators=[DataRequired()])
    submit = SubmitField('Add New User')

class SelectTeamYear(FlaskForm):
    team = SelectField('Account Type:', validators=[DataRequired()])
    year = SelectField('Account Type:', validators=[DataRequired()])