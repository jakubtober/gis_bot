import logging
import os

DB_CONNECTION_URL = os.getenv("DATABASE_URL", "xxxxxxxx")

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
)
logger = logging.getLogger()

RETRY_IN_SECONDS = 30
DELAY_IN_SECONDS = 30
