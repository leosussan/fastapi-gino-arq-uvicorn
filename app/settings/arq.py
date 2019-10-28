from arq.connections import RedisSettings

from .globals import REDIS_IP, REDIS_PORT

settings = RedisSettings(host=REDIS_IP, port=REDIS_PORT)
