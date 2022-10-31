import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from browserstack_caps import all_devices
from locators import GamesLocators as locators


class BrowserstackScreenshotter():
    def __init__(self, url):
        self.token = "https://<username>:<access_key>@hub-cloud.browserstack.com/wd/hub"
        self.url = url


    def test_passed(self):
        self.driver.execute_script("browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": {\"status\":\"passed\", \"reason\": \"Test Passed\"}}")


    def screen_devices(self, desired_cap):
        self.driver = webdriver.Remote(
            command_executor=self.token,
            desired_capabilities=desired_cap,
            keep_alive=True)

        file_name = desired_cap['bstack:options']['deviceName'] + "_" + desired_cap['bstack:options']['deviceOrientation'] + '.png'

        self.driver.get(self.url)
        # wait for the page to load
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((locators.WHATEVER))).click()


        self.driver.get_screenshot_as_file(file_name)
        print(f'{file_name} saved')
        self.test_passed()
        self.driver.quit()
        
        if not os.path.exists(f'screenshots_{self.url}_{datetime.now().strftime("%Y-%m-%d")}'):
            os.makedirs(f'screenshots_{self.url}_{datetime.now().strftime("%Y-%m-%d")}')
        for f in os.listdir(os.getcwd()):
            if f.endswith(".png"):
                shutil.move(f, f'screenshots_{self.url}_{datetime.now().strftime("%Y-%m-%d")}')

    def run(self):
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.screen_devices, all_devices)
