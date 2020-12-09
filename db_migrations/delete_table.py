from config import logger
from utils.db_client import DbConnectionClient


def retrive_data(table_name: str, custom_db_connection: DbConnectionClient) -> None:
    try:
        custom_db_connection.db_cursor.execute(f"DROP TABLE {table_name};")
        custom_db_connection.db_connection.commit()

    except Exception as exception:
        logger.debug(exception)


if __name__ == "__main__":
    db_connection = DbConnectionClient()
    retrive_data("articles_history_production", db_connection)
