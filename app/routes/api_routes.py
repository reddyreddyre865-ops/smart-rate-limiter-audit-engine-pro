
from flask import Blueprint,jsonify
from app.middleware.auth import get_payload
bp=Blueprint('api',__name__)
@bp.route('/data')
def data():
    p=get_payload()
    return jsonify({'tenant':p['tenant_id'],'status':'success'})
