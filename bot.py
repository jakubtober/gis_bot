import asyncio

import config


class Bot():
    async def check_articles(self):
        print("Articles checked, haven't found new content...")

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
