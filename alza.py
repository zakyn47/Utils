from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from locators import Locators
import time
import re

class Alza:
    """bot which checks (idk yet) on alza.cz"""

    urls = []
    
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.alza.cz/")
        self.driver.find_element(*Locators.COOKIES).click()


    def search(self, item="GEFORCE 4090"):
        search = self.driver.find_element(*Locators.SEARCH)
        search.send_keys(item)
        search.send_keys(Keys.RETURN)

    def show_more_products(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*Locators.DALSICH_24).click()


    def get_product_names(self):
        names = self.driver.find_elements(*Locators.NAME)
        for name in names:
            print(name.text)


    def get_links(self):
        body = self.driver.find_element(By.ID, "rootHtml").find_elements(By.TAG_NAME, "a")
        for link in body:
            if link.get_attribute("href").startswith("http"):
                self.urls.append(link.get_attribute("href"))
                print(link.get_attribute("href"))


    def go_to_next_url(self):
        if len(self.urls) > 0:
            self.driver.get(self.urls[0])
            self.urls.pop(0)
    

    def close(self):
        self.driver.close()
        

if __name__ == "__main__":
    alza = Alza()
    alza.search()
    alza.get_product_names()
    alza.get_links()

