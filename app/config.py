
import os
class Config:
    SECRET_KEY=os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI=os.getenv("MYSQL_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    REDIS_HOST=os.getenv("REDIS_HOST","localhost")
    REDIS_PORT=int(os.getenv("REDIS_PORT",6379))
