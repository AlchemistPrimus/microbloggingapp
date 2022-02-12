from flask import Blueprint

auth=Blueprint('auth',__name__,template_folder='templates')
main=Blueprint('main',__name__,template_folder='templates')

import sys
sys.path.insert(0,'/home/ado/Desktop/microblog')


 
from app.main import views,errors
from app.models import Permission

#Adding a context processor to make variable available to all templates during rendering
@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)