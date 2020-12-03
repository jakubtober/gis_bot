import asyncio

import config
from beautiful_soup_browser import BeautifulSoupBrowser
import logging
import sys


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

class Bot:
    def __init__(self):
        self.beautiful_soup_browser = BeautifulSoupBrowser()

    async def check_articles(self):
        last_article = self.beautiful_soup_browser.get_last_article()
        if last_article:
            logger.debug(f"Last article: \n{last_article.article_title}\n")
        else:
            # add logger event
            logger.debug("Couldn't find any article on the GIS homepage...")


async def main():
    bot = Bot()

    while True:
        try:
            await bot.check_articles()
            sys.stdout.flush()
        except Exception as e:
            await asyncio.sleep(config.RETRY_IN_SECONDS)
            # add logger event
        finally:
            # add logger event
            await asyncio.sleep(config.DELAY_IN_SECONDS)


asyncio.run(main())
