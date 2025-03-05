from minio import Minio
from src.config.settings import settings
from src.utils.logger import logger

def get_minio_client():
    try:
        client = Minio(
            endpoint=settings.minio_endpoint.replace("http://", "").replace("https://", ""),
            access_key=settings.minio_access_key,
            secret_key=settings.minio_secret_key,
            secure=settings.minio_endpoint.startswith("https://")
        )
        # Ensure bucket exists
        if not client.bucket_exists(settings.minio_bucket):
            client.make_bucket(settings.minio_bucket)
            logger.info("Created bucket: %s", settings.minio_bucket)
        logger.info("Connected to MinIO.")
        return client
    except Exception as e:
        logger.error("Error connecting to MinIO: %s", e)
        raise e

# Usage:
# minio_client = get_minio_client()
