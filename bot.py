from utils.selenium_browser import SeleniumBrowser
from utils.beautiful_soup_browser import BeautifulSoupBrowser


MAIN_GIS_URL = r"https://gis.gov.pl/kategoria/zywnosc-i-woda/normy-i-prawo/ostrzezenia-publiczne-dot-zywnosci/"


if __name__ == "__main__":
    selenium_browser = SeleniumBrowser()
    beautiful_soup__browser = BeautifulSoupBrowser()
    # article_urls = selenium_browser.get_articles_urls(MAIN_GIS_URL)
    article_urls = beautiful_soup__browser.get_articles_urls(MAIN_GIS_URL)


    print("Browser initialized.")