
import redis,time
class RateLimiter:
    def __init__(self,h,p):
        self.r=redis.Redis(host=h,port=p,decode_responses=True)
    def check(self,key,limit=100,window=60):
        bucket=f'{key}:{int(time.time())//window}'
        count=self.r.incr(bucket)
        if count==1:self.r.expire(bucket,window)
        return count<=limit
