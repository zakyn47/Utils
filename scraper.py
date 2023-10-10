from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import re
import argparse
from webdriver_manager.chrome import ChromeDriverManager

class WebCrawler:
    def __init__(self, starting_url):
        self.starting_url = starting_url
        self.driver = webdriver.Chrome()
        self.visited_urls = []

    def gather_urls_and_emails(self, url):
        self.visited_urls.append(url)
        self.driver.get(url)
        urls = self.extract_urls()
        emails = self.extract_emails()
        print(f"Visited URL: {url}")
        print(f"Found URLs: {urls}")
        print(f"Found Emails: {(set(emails))}")
        print("-----------------------------------------------------")
        if url == self.starting_url:
            print("Stopping script as the next page is the same as the starting URL")
            return

        for new_url in urls:
            if new_url not in self.visited_urls:
                self.gather_urls_and_emails(new_url)

    def extract_urls(self):
        links = self.driver.find_elements(By.TAG_NAME, "a")
        urls = []
        for link in links:
            url = link.get_attribute("href")
            if url and url.startswith("http"):
                urls.append(url)
        print(f"Extracted URLs: {urls}")
        return urls

    def extract_emails(self):
        page_source = requests.get(self.driver.current_url).text
        emails = re.findall(r"[\w\.-]+@[\w\.-]+", page_source)
        print(f"Extracted Emails: {emails}")
        return list(set(emails))

    def close(self):
        self.driver.quit()

parser = argparse.ArgumentParser(description="Web Crawler")
parser.add_argument("starting_url", type=str, help="The starting URL for web crawling")
args = parser.parse_args()

crawler = WebCrawler(args.starting_url)
crawler.gather_urls_and_emails(args.starting_url)
crawler.close()
