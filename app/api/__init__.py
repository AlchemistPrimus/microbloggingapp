from flask import Blueprint


api=Blueprint('api',__name__)


import sys
sys.path.insert(0,'/home/ado/Desktop/microblog')
from app.api import authentication, comments, decorators, errors, posts, users