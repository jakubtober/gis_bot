from apscheduler.schedulers.blocking import BlockingScheduler

from config import DELAY_IN_MINUTES
from utils.db_client import DbConnectionClient
from utils.facebook_client import FacebookClient
from utils.gis_bot import Bot


bot_scheduler = BlockingScheduler()
db_connection = DbConnectionClient()
fb_client = FacebookClient()
bot = Bot()


@bot_scheduler.scheduled_job("interval", minutes=DELAY_IN_MINUTES)
def check_articles():
    bot.check_articles(db_connection, fb_client)


bot_scheduler.start()
