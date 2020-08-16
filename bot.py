from utils.beautiful_soup_browser import BeautifulSoupBrowser
from utils.facebook_client import FacebookClient
from utils.db_client import DbConnectionClient


if __name__ == "__main__":
    beautiful_soup__browser = BeautifulSoupBrowser()
    facebook_client = FacebookClient()
    db_client = DbConnectionClient()

    all_db_posts = db_client.get_all_db_posts()

    article_urls = beautiful_soup__browser._get_articles_urls()
    last_article_url = beautiful_soup__browser._get_last_article_url()
    last_article = beautiful_soup__browser.get_last_article()

    message = facebook_client.generate_message_content(
        last_article.article_title, last_article.article_text,
    )

    # We will keep part where bot posts message until we have running database
    # to check history of pubnlished posts first

    # facebook_client.publish_post(message, last_article_url)
