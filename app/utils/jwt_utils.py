
import jwt,time
def create_token(tenant_id,tier,secret):
    return jwt.encode(
      {'tenant_id':tenant_id,'tier':tier,'exp':time.time()+86400},
      secret,algorithm='HS256')
