from pymongo import MongoClient
from src.config.settings import settings
from src.utils.logger import logger

def get_mongo_client():
    try:
        client = MongoClient(settings.mongo_uri)
        logger.info("Connected to MongoDB.")
        return client
    except Exception as e:
        logger.error("Error connecting to MongoDB: %s", e)
        raise e

def get_raw_db():
    client = get_mongo_client()
    return client[settings.mongo_db]

# Usage:
# db = get_raw_db()
# collection = db["products"]
