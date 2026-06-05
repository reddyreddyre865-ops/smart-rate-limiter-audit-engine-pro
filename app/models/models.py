
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Tenant(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    tenant_name=db.Column(db.String(100))
    tier=db.Column(db.String(20))
class AuditLog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    tenant_id=db.Column(db.Integer,index=True)
    endpoint=db.Column(db.String(200))
