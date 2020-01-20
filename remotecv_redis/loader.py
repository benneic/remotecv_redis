# coding: utf-8

from redis import Redis
from remotecv.utils import logger, config

def load_sync(path):
    """
    Loads image from Redis
    :param string path: Path to load
    """
    host = os.environ.get('REMOTECV_REDIS_HOST', config.redis_host)
    port = os.environ.get('REMOTECV_REDIS_PORT', config.redis_port)
    db = os.environ.get('REMOTECV_REDIS_DATABASE', config.redis_database)
    password = os.environ.get('REMOTECV_REDIS_PASSWORD', config.redis_password)
    logger.debug("remotecv_redis.loader: Connecting to Redis(host=%s, port=%s, db=%s, password=%s)", host, port, db, password)
    redis = Redis(host=host, port=port, db=db, password=password)
    image = redis.get(path)

    if not image:
        raise Exception("remotecv_redis.loader: Image not found at %s" % path)

    logger.debug("remotecv_redis.loader: Loaded %s" % path)
    return image

