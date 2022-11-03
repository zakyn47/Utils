from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
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
                    with open("links.txt", "a") as f:
                        f.write(link.get_attribute("href"))
                        f.write("\n")
        except:
            pass


    def mail_regex(self):
        return re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")


    def cz_phone_regex(self):
        return re.compile(r"(\+420)? ?[1-9][0-9]{2} ?[0-9]{3} ?[0-9]{3}")


    def go_to_next_url(self):
        if len(self.urls) > 0:
            self.driver.get(self.urls[0])
            self.urls.pop(0)
    

    def close(self):
        self.driver.close()
        

if __name__ == "__main__":
    UrlGrabber = UrlGrabber("https://www.reddit.com/")
    start_time = time.time()

    UrlGrabber.get_links()
    UrlGrabber.go_to_next_url()

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
    print(UrlGrabber.get_email_regex())