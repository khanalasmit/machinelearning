from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Amazon_bot:
    def __init__(self, url, search_item):
        self.driver = webdriver.Chrome()
        self.htmls = []
        self.url = url
        self.search_item = search_item

    def send_to_search(self):
        try:
            search_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox'))
            )
            search_element.clear()
            search_element.send_keys(self.search_item)
            search_element.send_keys(Keys.RETURN)
        except:
            print('Error occurred during search')

    def send_next_key(self):
        try:
            next_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.s-pagination-next'))
            )
            next_element.click()
            time.sleep(3)
            return True
        except:
            print("Error occurred during sending2 next key")
            return False

    def get_items(self):
        try:
            html = self.driver.page_source
            return html
        except:
            print("Error in getting items")
            return None

    def amazon_bot(self):
        self.driver.get(self.url)
        time.sleep(20)
        self.send_to_search()
        html = self.get_items()
        self.htmls.append(html)
        while self.send_next_key():
            html = self.get_items()
            self.htmls.append(html)
        self.driver.quit()

    def get_html(self):
        self.amazon_bot()
        return self.htmls