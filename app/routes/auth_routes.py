
from flask import Blueprint,request,jsonify,current_app
from app.utils.jwt_utils import create_token
bp=Blueprint('auth',__name__)
@bp.route('/login',methods=['POST'])
def login():
    data=request.json
    token=create_token(data['tenant_id'],data['tier'],current_app.config['SECRET_KEY'])
    return jsonify({'token':token})
