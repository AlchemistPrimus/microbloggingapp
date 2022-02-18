from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
import sys
sys.path.insert(0,'/home/ado/Desktop/microblog')
from app.models import User, Role

    
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('Keep me logged in')
    submit=SubmitField('Log in')
    
class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    username=StringField('Username',validators=[DataRequired(),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Usernames must have only letters, numbers, dots or underscores')])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('password2',message='passwords must match')])
    password2=PasswordField('Confirm password',validators=[DataRequired()])
    submit=SubmitField('submit')
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')
        
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username exists.')
        
class EditProfileForm(FlaskForm):
    name=StringField('Real name',validators=[Length(0,64)])
    location=StringField('Location',validators=[Length(0,64)])
    about_me=TextAreaField('About me')
    submit=SubmitField('Submit')
    
class EditProfileAdminForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    username=StringField('Username',validators=[DataRequired(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Usernames can only have alphabets, fullstops and underscores')])
    confirmed=BooleanField('Confirmed')
    role=SelectField('Role',coerce=int)#will provide a dropdown list implemented by <select> in html coerce set to int to store id inform of int instead of default which is strings since ids in the db are int
    name=StringField('Real name',validators=[DataRequired(),Length(1,64)])
    location=StringField('Location',validators=[DataRequired(),Length(1,64)])
    about_me=TextAreaField('About me')
    submit=SubmitField('Submit')
    
    def __int__(self,user,*args,**kwargs):
        super(EditProfileAdminForm,self).__init__(*args,**kwargs)
        self.role.choices=[(role.id,role.name) for role in Role.query.order_by(Role.name).all()]#provide choices for role field that implements <select> element and must be given as a list of tuples of two values(id and text to show)
        self.user=user
        
    def validate_email(self,field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered!')
        
        
    def validate_username(self,field):
        if field.data != self.user.email and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use!')
        
class PostForm(FlaskForm):
    #Enabling markdown post form
    body=PageDownField('What is on your mind?',validators=[DataRequired()])
    submit=SubmitField('Submit')
    
#Comment input form
class CommentForm(FlaskForm):
    body=StringField('',validators=[DataRequired()])
    submit=SubmitField('Submit')