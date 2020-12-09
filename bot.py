from apscheduler.schedulers.blocking import BlockingScheduler

from utils.gis_bot import Bot
from utils.db_client import DbConnectionClient


bot_scheduler = BlockingScheduler()
db_connection = DbConnectionClient()
bot = Bot()


@bot_scheduler.scheduled_job("interval", minutes=60)
def check_articles():
    bot.check_articles()


bot_scheduler.start()
