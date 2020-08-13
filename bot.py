from selenium_browser import initialize_selenium


MAIN_GIS_URL = r"https://gis.gov.pl/kategoria/zywnosc-i-woda/normy-i-prawo/ostrzezenia-publiczne-dot-zywnosci/"


if __name__ == "__main__":
    articles_urls_list = []

    browser = initialize_selenium(MAIN_GIS_URL, 2)
    articles_list = browser.find_element_by_class_name("category-list__content").find_elements_by_class_name("category-list__item")

    for article in articles_list:
        articles_urls_list.append(article.find_element_by_css_selector("a").get_attribute("href"))

    print("Browser initialized.")