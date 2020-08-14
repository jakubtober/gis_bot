import requests
from bs4 import BeautifulSoup



class BeautifulSoupBrowser:
    def __init__(self):
        pass

    def get_articles_urls(self, url):
        articles_list = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles_list_elements = soup.find_all("div", class_="category-list__item")

        for article in articles_list_elements:
            url = article.a["href"]
            articles_list.append(url)

        return articles_list
