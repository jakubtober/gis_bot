import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROMEDRIVER_PATH = r"C:\gis_bot\gis_bot\chromedriver.exe"


class SeleniumBrowser:
    def __init__(self):
        self.browser = self._initialize_selenium()

    def _initialize_selenium(self):
        try:
            options = Options()
            options.headless = True
            browser = webdriver.Chrome(
                options=options, executable_path=CHROMEDRIVER_PATH
            )
            time.sleep(2)
            print("Selenium successfully initialized.")
            return browser
        except Exception as error:
            print("Couldn't initizlize Selenium...")

    def get_articles_urls(self, url):
        articles_list = []
        articles_list_elements = self.browser.find_element_by_class_name(
            "category-list__content"
        ).find_elements_by_class_name("category-list__item")

        for article in articles_list_elements:
            articles_list.append(
                article.find_element_by_css_selector("a").get_attribute("href")
            )

        return articles_list
