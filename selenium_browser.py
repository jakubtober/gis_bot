import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROMEDRIVER_PATH = r"C:\gis_bot\gis_bot\chromedriver.exe"


def initialize_selenium(url, time_to_wait):
    try:
        options = Options()
        options.headless = True
        browser = webdriver.Chrome(
            options=options, executable_path=CHROMEDRIVER_PATH)
        test_request = requests.get(url)
        browser.get(url)
        time.sleep(time_to_wait)
        print("Selenium successfully initialized.")
        return browser
    except Exception as error:
        print("Couldn't initizlize Selenium...")