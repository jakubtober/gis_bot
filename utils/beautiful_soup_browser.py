import requests
from bs4 import BeautifulSoup
from typing import Union


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

    def _get_articles_urls(self) -> list:
        articles_urls = []
        try:
            response = requests.get(self.GIS_WARNINGS_URL)
            soup = BeautifulSoup(response.text, "html.parser")
            articles_div = soup.find_all("div", class_="art-prev art-prev--near-menu")
            list_of_articles = articles_div[0].ul.find_all("li") if articles_div else []

            for list_element in list_of_articles:
                url = list_element.a["href"]
                articles_urls.append(url)

            return articles_urls
        except Exception as e:
            # add logger event
            raise

    def _get_last_article_url(self) -> Union[str, None]:
        article_urls = self._get_articles_urls()
        last_article_on_the_list_url = (
            self.BASE_GIS_URL + article_urls[0] if article_urls else None
        )
        return last_article_on_the_list_url

    def get_last_article(self) -> Union[Article, None]:
        last_article_url = self._get_last_article_url()

        if last_article_url:
            response = requests.get(last_article_url)
            soup = BeautifulSoup(response.text, "html.parser")
            article_title = soup.find_all("title")[0].get_text()
            article_date = ""
            article_content = ""
            return Article(article_title, article_content, article_date)
        else:
            # add logger event
            return None
