import requests
from bs4 import BeautifulSoup


class Article:
    def __init__(self, article_title: str, article_text: str, article_date: str):
        self.article_title = article_title
        self.article_text = article_text
        self.article_date = article_date


class BeautifulSoupBrowser:
    BASE_GIS_URL = r"https://www.gov.pl"
    GIS_WARNINGS_URL = r"https://www.gov.pl/web/gis/ostrzezenia"

    def __init__(self):
        pass

    def _get_articles_urls(self):
        articles_urls = []
        response = requests.get(self.GIS_WARNINGS_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        list_of_articles_list = soup.find_all("div", class_="art-prev art-prev--near-menu")[0].ul.find_all("li")

        for list_element in list_of_articles_list:
            url = list_element.a["href"]
            articles_urls.append(url)

        return articles_urls

    def _get_last_article_url(self):
        try:
            return self.BASE_GIS_URL + self._get_articles_urls()[0]
        except Exception:
            return None

    def get_last_article(self):
        response = requests.get(self._get_last_article_url())
        soup = BeautifulSoup(response.text, "html.parser")
        article_title = soup.find_all("title")[0].get_text()
        article_date = ""
        article_content = ""

        return Article(article_title, article_content, article_date)
