
import jwt
from flask import request,current_app
def get_payload():
    token=request.headers.get('Authorization','').replace('Bearer ','')
    return jwt.decode(token,current_app.config['SECRET_KEY'],algorithms=['HS256'])
