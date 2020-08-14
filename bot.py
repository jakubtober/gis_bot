from utils.beautiful_soup_browser import BeautifulSoupBrowser
from utils.facebook_client import FacebookClient



if __name__ == "__main__":
    beautiful_soup__browser = BeautifulSoupBrowser()
    facebook_client = FacebookClient()

    article_urls = beautiful_soup__browser._get_articles_urls()
    last_article_url = beautiful_soup__browser._get_last_article_url()

    last_artcile = beautiful_soup__browser.get_last_article()

    print(last_artcile.article_date)
    print(last_artcile.article_text)

    facebook_client.get_all_posts()

    print(facebook_client.all_posts)