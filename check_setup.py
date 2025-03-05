from src.data_storage.mongodb import get_raw_db
from src.data_storage.postgres import get_postgres_connection
from src.caching.cache_manager import get_redis_client
from src.caching.minio_client import get_minio_client
from src.utils.logger import logger

def run_data_pipeline():
    # Connect to databases and caching systems
    raw_db = get_raw_db()
    pg_conn = get_postgres_connection()
    redis_client = get_redis_client()
    minio_client = get_minio_client()
    
    # Your data collection and cleaning logic here...
    logger.info("Running data pipeline...")
    
    # Example usage: log a sample product fetch
    sample_product = {"name": "Sample Product", "price": 100}
    logger.debug("Fetched product: %s", sample_product)
    
if __name__ == "__main__":
    run_data_pipeline()
