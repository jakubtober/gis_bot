import logging
import os

DB_CONNECTION_URL = os.getenv("DATABASE_URL", "xxxxxxxx")

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
)
logger = logging.getLogger()

DELAY_IN_SECONDS = 10
DELAY_IN_MINUTES = 60
