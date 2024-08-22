import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    for _ in range(1000):
        page.goto("https://docs.google.com/forms/d/e/1FAIpQLSdaAp8s841r1itsmXd7OaBs7mKzSz4iVlEgdbgXJUTrnhQsjw/viewform")
        page.get_by_label("Jméno a příjmení").click()
        page.get_by_label("Jméno a příjmení").fill("yo mama")
        page.get_by_label("Submit").click()
        page.get_by_role("link", name="Odeslat další odpověď").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
