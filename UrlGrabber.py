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

class UrlGrabber:

    urls = []
    
    def __init__(self, url: str):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(3)
        self.driver.get(url)


    def get_links(self):
        body = self.driver.find_element(By.XPATH, "/html/body").find_elements(By.TAG_NAME, "a")
        try:
            for link in body:
                if link.get_attribute("href").startswith("http"):
                    self.urls.append(link.get_attribute("href"))
                    print(link.get_attribute("href"))
        except AttributeError:
            pass


    def go_to_next_url(self):
        if len(self.urls) > 0:
            self.driver.get(self.urls[0])
            self.urls.pop(0)
    

    def close(self):
        self.driver.close()
        

if __name__ == "__main__":
    UrlGrabber = UrlGrabber("https://www.reddit.com")
    UrlGrabber.get_links()

