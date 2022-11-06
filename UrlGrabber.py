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
import random

class UrlGrabber:

    email_regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    phone_regex = re.compile(r"(^\+?[\d\s?]{10,15})")

    urls = []
     

    def __init__(self, url: str):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(3)
        self.driver.get(url)


    def get_urls(self):
        print("collecting urls at page: " + self.driver.current_url)
        url_links = self.driver.find_element(By.XPATH, "/html/body").find_elements(By.TAG_NAME, "a")
        try:
            for link in url_links:
                if link.get_attribute("href").startswith("http"):
                    self.urls.append(link.get_attribute("href"))
                    #print(link.get_attribute("href"))
                    with open("links.txt", "a") as f:
                        f.write(link.get_attribute("href"))
                        f.write("\n")
        except:
            pass


    def all_page_elements(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body")))
        return self.driver.find_elements(By.XPATH, "/html/body/*")
    

    def get_emails(self):
        print("collecting emails at page: " + self.driver.current_url)
        for element in self.all_page_elements():
            emails = self.email_regex.findall(element.text)
            if emails:
                print(emails)


    def get_phones(self):
        print("collecting phones at page: " + self.driver.current_url)
        for element in self.all_page_elements():
            phones = self.phone_regex.findall(element.text)
            if phones:
                print(phones)


    def go_to_next_url(self):
        if len(self.urls) > 1:
            self.driver.get(self.urls[0])
            self.urls.pop(0)
    

    def close(self):
        self.driver.close()
        

if __name__ == "__main__":
    UrlGrabber = UrlGrabber("https://www.korycany.cz/")
    start_time = time.time()


    next_pages = 5
    while next_pages > 0:
        next_pages -= 1
        UrlGrabber.get_urls()
        UrlGrabber.get_emails()
        UrlGrabber.get_phones()
        UrlGrabber.go_to_next_url()


    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
    UrlGrabber.close()