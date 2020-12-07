from apscheduler.schedulers.blocking import BlockingScheduler

from utils.gis_bot import Bot


bot_scheduler = BlockingScheduler()
bot = Bot()


@bot_scheduler.scheduled_job("interval", minutes=60)
def check_articles():
    bot.check_articles()


bot_scheduler.start()
