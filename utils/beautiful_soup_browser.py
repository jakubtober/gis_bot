import requests
from bs4 import BeautifulSoup


class Article:
    def __init__(self, article_title: str, article_text: str, article_date: str):
        self.article_title = article_title
        self.article_text = article_text
        self.article_date = article_date


class BeautifulSoupBrowser:
    MAIN_GIS_URL = r"https://gis.gov.pl/kategoria/zywnosc-i-woda/normy-i-prawo/ostrzezenia-publiczne-dot-zywnosci/"

    def __init__(self):
        pass

    def _get_articles_urls(self):
        articles_list = []
        response = requests.get(self.MAIN_GIS_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles_list_elements = soup.find_all("div", class_="category-list__item")

        for article in articles_list_elements:
            url = article.a["href"]
            articles_list.append(url)

        return articles_list

    def _get_last_article_url(self):
        try:
            return self._get_articles_urls()[0]
        except Exception:
            return None

    def get_last_article(self):
        response = requests.get(self._get_last_article_url())
        soup = BeautifulSoup(response.text, 'html.parser')
        article_title = soup.find_all("title")[0].get_text()
        article_date = soup.find_all("div", class_="single-post__date")[0].get_text().replace(" ", "").replace("\n", "")
        article_content = soup.find_all("div", class_="single-post__content")[0].get_text()

        return Article(article_title, article_content, article_date)
