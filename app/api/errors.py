#Adding error handler with http content negotiation
from flask import request, render_template, jsonify
import sys
sys.path.insert(0,'/home/ado/Desktop/microblog/app')
import main

#@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetype.accept_json and request.accept_mimetype.accept_html:
        response=jsonify({'error':'not found'})
        response.status_code=404
    return render_template('404.html'),404


def forbidden(message):
    response=jsonify({'error':'forbidden','message':message})
    response.status_code=403
    return response