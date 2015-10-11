from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
	email = StringField('email',validators=[Required(),Email(),Length(1,64)])
	password = PasswordField('Password',validators=[Required()])
	rememper_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')
	
class ChangePasswordForm(Form):
	
	old_password = PasswordField('Current Password ',validators=[Required()])
	password = PasswordField('New Password',validators=[
		Required(),EqualTo('password2',message='Password must match.')])
	password2 = PasswordField('Confirm Password',validators=[Required()])
	
	submit = SubmitField('Password Change ')

	
class RegistrationForm(Form):
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	username = StringField('Username',validators=[
		Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
										'Username must have only letters,'
										'numpers , dots or underscores')])
	password = PasswordField('Password',validators=[
		Required(),EqualTo('password2',message='Password must match.')])
	password2 = PasswordField('Confirm password ',validators=[Required()])
	submit = SubmitField('Register')
	
	def validate_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registred.')
	
	def validate_username(self,field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('username  already in use .')
			
class PasswordResetRequestForm(Form):
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	submit = SubmitField('Reset Password')
	
class PasswordResetForm(Form):
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	password = PasswordField('Password',validators=[
		Required(),EqualTo('password2',message='Password must match.')])
	password2 = PasswordField('Confirm password ',validators=[Required()])
	submit = SubmitField('Reset Password')

class ChangeEmailForm(Form):
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	password = PasswordField('Password',validators=[Required()])
	submit = SubmitField('Update Email Address')
	
	def validate_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registred. ')
