from config import logger
from utils.db_client import DbConnectionClient


def check_if_article_in_db(db_connection: DbConnectionClient, date: str, title: str):
    try:
        db_connection.db_cursor.execute(
            f"""
                SELECT * FROM articles_history_staging
                WHERE date = '{date}'
                AND title = '{title}';
            """
        )

        items = [entity for entity in db_connection.db_cursor.fetchall()]

        if items:
            logger.debug(f"Found artcile in the db, date: {date} title: {title}")
            return items[0]
        else:
            return None

    except Exception as exception:
        logger.debug(exception)


def add_article_to_db(db_connection: DbConnectionClient, date: str, title: str):
    try:
        db_connection.db_cursor.execute(
            f"""
                INSERT INTO articles_history_staging (date, title)
                VALUES ('{date}', '{title}');
            """
        )
        db_connection.db_connection.commit()

    except Exception as exception:
        logger.debug(exception)
