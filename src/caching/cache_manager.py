import redis
from src.config.settings import settings
from src.utils.logger import logger

def get_redis_client():
    try:
        client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            password=settings.redis_password,
        )
        # Test the connection
        client.ping()
        logger.info("Connected to Redis.")
        return client
    except Exception as e:
        logger.error("Error connecting to Redis: %s", e)
        raise e

# Usage:
# redis_client = get_redis_client()
