from .beautiful_soup_browser import BeautifulSoupBrowser

from config import logger


class Bot:
    def __init__(self):
        self.beautiful_soup_browser = BeautifulSoupBrowser()

    def check_articles(self):
        last_article = self.beautiful_soup_browser.get_last_article()
        if last_article:
            logger.debug(f"Last article: \n{last_article.article_title}\n")
        else:
            # add logger event
            logger.debug("Couldn't find any article on the GIS homepage...")