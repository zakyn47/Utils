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

class Alza:
    """bot which checks (idk yet) on alza.cz"""
    
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(1)
        self.driver.get("https://www.alza.cz/")
        self.driver.find_element(*Locators.COOKIES).click() # click on cookies button to avoid ElementNotInteractableException while clicking on DALSICH_24


    def search(self, item="GEFORCE 4090"):
        search = self.driver.find_element(*Locators.SEARCH)
        search.send_keys(item)
        search.send_keys(Keys.RETURN)

    def show_more_products(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*Locators.DALSICH_24).click()

    def get_prices(self):
        prices = self.driver.find_elements(*Locators.PRICES)
        for price in prices:
            print(price.text)


    def get_names(self):
        names = self.driver.find_elements(*Locators.NAME)
        for name in names:
            print(name.text)
        

if __name__ == "__main__":
    alza = Alza()
    alza.search()
    alza.get_prices()
    alza.get_names()
    alza.show_more_products()
    time.sleep(5)
    alza.show_more_products()
    alza.get_names()
    #alza.driver.close()