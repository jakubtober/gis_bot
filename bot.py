import asyncio

import config
from beautiful_soup_browser import BeautifulSoupBrowser


class Bot():
    def __init__(self):
        self.beautiful_soup_browser = BeautifulSoupBrowser()

    async def check_articles(self):
        last_article = self.beautiful_soup_browser.get_last_article()
        print(f"Last article: \n{last_article.article_title}\n")


async def main():

    bot = Bot()

    while True:
        try:
            await bot.check_articles()
        except Exception as e:
            await asyncio.sleep(config.RETRY_IN_SECONDS)
        finally:
            await asyncio.sleep(config.DELAY_IN_SECONDS)

asyncio.run(main())
