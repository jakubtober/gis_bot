import os

try:
    import psycopg2
except ImportError as import_exception:
    print("This script needs psycopg2.\n" f"Exception: {import_exception}")
except Exception as exception:
    print(exception)


DB_CONNECTION_STRING = "postgres://{}:{}@{}/{}?port={}".format(
    os.getenv("DB_USER", "xxxxxxxx"),
    os.getenv("DB_PASSWORD", "xxxxxxxx"),
    os.getenv("DB_HOST", "xx.xxx.xxx.xxx"),
    os.getenv("DB_NAME", "xxxxxxx"),
    os.getenv("DB_PORT", 1234),
)


class DbConnectionClient:
    def __init__(self):
        # We will leave it commented until we have db set up and running
        # if DB_CONNECTION_STRING is None:
        #     raise AttributeError(
        #         "Connection string to database is not defined."
        #     )
        #
        # self.db_connection = psycopg2.connect(DB_CONNECTION_STRING)
        # self.cursor = db_connection.cursor()
        self.cursor = None

    def get_all_db_posts(self):
        # Until we have running database we will use mocked data
        return [
            (
                "Wycofanie produktu pn. Rizi, Olej z ryżu - aktualizacja z 12 sierpnia 2020 r. - GIS",
                "13.08.2020",
            ),
        ]
