from apscheduler.schedulers.blocking import BlockingScheduler

from config import DELAY_IN_MINUTES
from utils.gis_bot import Bot
from utils.db_client import DbConnectionClient


bot_scheduler = BlockingScheduler()
db_connection = DbConnectionClient()
bot = Bot()


@bot_scheduler.scheduled_job("interval", minutes=DELAY_IN_MINUTES)
def check_articles():
    bot.check_articles(db_connection)


bot_scheduler.start()
