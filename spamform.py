import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    for _ in range(10000):
        page.goto("https://docs.google.com/forms/d/e/xxxxxxxx/viewform")
        page.get_by_label("Jméno a příjmení").click()
        page.get_by_label("Jméno a příjmení").fill("xxxxx")
        page.get_by_label("Submit").click()
        page.get_by_role("link", name="Odeslat další odpověď").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
