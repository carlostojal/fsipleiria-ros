import os

class Config:

    redis_host = "localhost"
    redis_port = 6379
    redis_db = 0

    def __init__(self):
        redis_host = os.environ['ROS_REDIS_HOST'];
        redis_port = os.environ['ROS_REDIS_PORT'];
        redis_db = os.environ['ROS_REDIS_DB'];
