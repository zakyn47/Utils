from selenium.webdriver.common.by import By


class Locators():
    """Locators for alza.cz"""
    COOKIES = (By.XPATH, "//*[@id=\"rootHtml\"]/body/alza-component-head/div[7]/div/div/div[2]/a[1]")
    PRICES = (By.CLASS_NAME, "price-box__price")
    DALSICH_24 = (By.XPATH, "//*[@id=\"loadmoreInner\"]/a[1]")
    SEARCH = (By.ID, "edtSearch")
    ITEMS = (By.ID, "boxes")
    NAME = (By.CLASS_NAME, "name")