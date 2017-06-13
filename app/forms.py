from flask_wtf import Form
from wtforms improt StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BolleanField('remember_me', default=False)
