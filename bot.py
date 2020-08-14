from utils.selenium_browser import SeleniumBrowser
from utils.beautiful_soup_browser import BeautifulSoupBrowser



if __name__ == "__main__":
    selenium_browser = SeleniumBrowser()
    beautiful_soup__browser = BeautifulSoupBrowser()

    article_urls = beautiful_soup__browser._get_articles_urls()
    last_article_url = beautiful_soup__browser._get_last_article_url()

    last_artcile = beautiful_soup__browser.get_last_article()

    print(last_artcile.article_date)
    print(last_artcile.article_text)