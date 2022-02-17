from flask_httpauth import HTTPBasicAuth
from flask import jsonify
import sys
sys.path.insert(0,'/home/ado/Desktop/microblog')
from app import db
from app.exceptions import ValidationError
from app.api import api
from app.models import User, Post
from app.api.errors import unauthorized, forbidden

#This will be initialized in the blueprints package and not in the application package
auth=HTTPBasicAuth()

#protecting all the routes hence login_required decorator will be added before request handler for the blueprint
@api.before_request
@auth.login_required
def before_request():
    if not g.current_user.is_anonymous and not g.current_user.confirmed:
        return forbidden('Unconfirmed account.')

#accepting tokens and regular credentials
@auth.verify_password
def verify_password(email_or_token,password):
    if email_or_token=='':
        return False
    if password == '':
        g.current_user=User.verify_auth_token(email_or_token)
        g.token_user=True
        return g.current_user is not None
    user=User.query.filter_by(email=email_or_token).first()
    if not user:
        return False
    g.current_user=user
    g.token_used=False
    return user.verify_password(password)

@auth.error_handler
def auth_error():
    return unauthorized('Invalid Credentials')

#generating authentication token
@api.route('/tokens/',methods=['POST'])
def get_token():
    if g.current_user.is_anonymous or g.token_used:
        return unauthorized('Invalid credentials')
    return jsonify({'token':g.current_user.generate_auth_token(expiration=3600),'expiration':3600})