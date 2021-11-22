import redis
import json
from Config import Config

class DataAcquisition:

    # Engine speed
    def getEngineRPM(self):

        r = redis.Redis(host=Config.redis_host, port=Config.redis_port, db=Config.redis_db)

        frame = r.hget("can_messages", str(0x60))
        frame = json.loads(frame)
        data = frame['data']

        r.close()

        # shift B1 8 bits (1 byte) left and concatenate with B0
        return data[6] << 8 | data[7]

    def listenEngineRPM(self, callback):

        # TODO
        # think of a performant and elegant way to do this
        # this is just a placeholder

        callback(self.getEngineRPM())

    # Speed
    def getSpeed(self):

        r = redis.Redis(host=Config.redis_host, port=Config.redis_port, db=Config.redis_db)

        frame = r.hget("can_messages", str(0x61))
        frame = json.loads(frame)
        data = frame['data']

        r.close()

        # ground speed (B1 and B0)
        return data[6] << 8 | data[7]

    def listenSpeed(self, callback):

        callback(self.getSpeed())
    

