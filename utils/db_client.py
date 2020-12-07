from config import DB_CONNECTION_URL
from config import logger


try:
    import psycopg2
except ImportError as import_exception:
    logger.debug("This script needs psycopg2.\n" f"Exception: {import_exception}")
except Exception as exception:
    logger.debug(exception)


class DbConnectionClient:
    def __init__(self):
        if DB_CONNECTION_URL is None:
            raise AttributeError("Connection string to database is not defined.")

        try:
            self.db_connection = psycopg2.connect(DB_CONNECTION_URL)
            self.db_cursor = self.db_connection.cursor()
            logger.debug("Connected to the db.")
        except Exception as exception:
            logger.debug(exception)
