from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email

class LoginForm(Form):
	email = StringField('email',validators=[Required(),Email(),Length(1,64)])
	password = PasswordField('Password',validators=[Required()])
	rememper_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')
	