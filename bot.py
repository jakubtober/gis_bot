import time
import datetime

from utils.beautiful_soup_browser import BeautifulSoupBrowser
from utils.facebook_client import FacebookClient
from utils.db_client import DbConnectionClient


BOT_REFRESH_RATE_IN_SECONDS = 10
NEW_POST = (
    "Wycofanie produktu pn. Rizi, Olej z ryżu - aktualizacja z 12 sierpnia 2020 r. - GIS",
    "13.08.2020",
)

try:
    beautiful_soup__browser = BeautifulSoupBrowser()
    facebook_client = FacebookClient()
    db_client = DbConnectionClient()
except Exception as exception:
    print(f"Couldn't initialize bot clients: {exception}")


def refresh_bot():
    all_db_posts = db_client.get_all_db_posts()

    last_article_url = beautiful_soup__browser._get_last_article_url()
    last_article = beautiful_soup__browser.get_last_article()

    message = facebook_client.generate_message_content(
        last_article.article_title, last_article.article_text,
    )

    if all_db_posts:
        for post in all_db_posts:
            if all(
                [
                    (last_article.article_title not in post),
                    (last_article.article_date not in post),
                ]
            ):
                facebook_client.publish_post(message, last_article_url)
                db_client.all_posts.append(NEW_POST)
    else:
        facebook_client.publish_post(message, last_article_url)
        db_client.all_posts.append(NEW_POST)


while True:
    time.sleep(BOT_REFRESH_RATE_IN_SECONDS)
    refresh_bot()
    print(f"Bot refreshed at: {datetime.datetime.now()}")
