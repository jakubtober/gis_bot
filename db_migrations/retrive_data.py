from config import logger
from utils.db_client import DbConnectionClient


def retrive_data(table_name: str, custom_db_connection: DbConnectionClient) -> None:
    try:
        custom_db_connection.db_cursor.execute(f"SELECT * FROM {table_name};")
        items = [entity for entity in custom_db_connection.db_cursor.fetchall()]
        logger.debug(f"Data from {table_name} table sucessfully retrived.")

    except Exception as exception:
        logger.debug(exception)


if __name__ == "__main__":
    db_connection = DbConnectionClient()
    retrive_data("articles_history_staging", db_connection)
