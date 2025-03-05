import psycopg2
from psycopg2.extras import RealDictCursor
from src.config.settings import settings
from src.utils.logger import logger

def get_postgres_connection():
    try:
        conn = psycopg2.connect(settings.postgres_uri, cursor_factory=RealDictCursor)
        logger.info("Connected to PostgreSQL.")
        return conn
    except Exception as e:
        logger.error("Error connecting to PostgreSQL: %s", e)
        raise e

# Usage:
# conn = get_postgres_connection()
# with conn.cursor() as cursor:
#     cursor.execute("SELECT * FROM products")
