#Adding error handler with http content negotiation
from xml.dom import ValidationErr
from flask import request, render_template, jsonify

import sys

from app.exceptions import ValidationError
sys.path.insert(0,'/home/ado/Desktop/microblog/')
from app.api import api


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response

def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response

def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response

@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])

def page_not_found(e):
    if request.accept_mimetype.accept_json and request.accept_mimetype.accept_html:
        response=jsonify({'error':'not found'})
        response.status_code=404
    return render_template('404.html'),404