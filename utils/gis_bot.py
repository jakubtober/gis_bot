from .beautiful_soup_browser import BeautifulSoupBrowser
from .db_operations import check_if_article_in_db, add_article_to_db

from config import logger


class Bot:
    def __init__(self):
        self.beautiful_soup_browser = BeautifulSoupBrowser()

    def check_articles(self, db_connection):
        last_web_article = self.beautiful_soup_browser.get_last_article()

        if last_web_article:
            article_in_db = check_if_article_in_db(
                db_connection, last_web_article.date, last_web_article.title,
            )

            if article_in_db:
                logger.debug(
                    f"Article already in db, date: {last_web_article.date}, title: {last_web_article.title}"
                )
            else:
                logger.debug(
                    f"New article on GIS webiste, couldn't find it in the db, date: {last_web_article.date}, title: {last_web_article.title}"
                )
                logger.debug(
                    f"Adding new article to the db, date: {last_web_article.date}, title: {last_web_article.title}"
                )
                add_article_to_db(db_connection, last_web_article.date, last_web_article.title)

               # TODO:
                # add post_article() method here as a next step
        else:
            logger.debug("Couldn't find any articles on GIS webiste...")
