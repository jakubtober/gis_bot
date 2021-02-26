from config import logger
from utils.db_client import DbConnectionClient


def create_articles_history_table(
    name: str, custom_db_connection: DbConnectionClient
) -> None:
    try:
        custom_db_connection.db_cursor.execute(
            f"""CREATE TABLE {name}(
            id SERIAL PRIMARY KEY NOT NULL,
            date VARCHAR (50) NOT NULL,
            title VARCHAR (250) NOT NULL
        );
        """
        )
        custom_db_connection.db_connection.commit()
        logger.debug(f"{name} table sucessfully created.")

    except Exception as exception:
        logger.debug(exception)


if __name__ == "__main__":
    db_connection = DbConnectionClient()
    create_articles_history_table("articles_history_production", db_connection)
