
from flask import Flask,jsonify,request
from app.config import Config
from app.models.models import db
from app.routes.auth_routes import bp as auth_bp
from app.routes.api_routes import bp as api_bp
from app.services.rate_limit_service import RateLimiter
import jwt
def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    limiter=RateLimiter(app.config['REDIS_HOST'],app.config['REDIS_PORT'])
    @app.before_request
    def protect():
      if request.path=='/login': return
      try:
        token=request.headers.get('Authorization','').replace('Bearer ','')
        payload=jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])
        if not limiter.check(str(payload['tenant_id'])):
          return jsonify({'error':'Too Many Requests'}),429
      except Exception:
        return jsonify({'error':'Unauthorized'}),401
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    with app.app_context():
      db.create_all()
    return app
