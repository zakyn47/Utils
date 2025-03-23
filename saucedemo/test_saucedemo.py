import pytest
import allure
from playwright.sync_api import sync_playwright, Page


BASE_URL = "https://www.saucedemo.com/"
VALID_USER = "standard_user"
ALL_USERS = ["standard_user", "locked_out_user", "problem_user",
             "performance_glitch_user", "error_user", "visual_user"]
VALID_PASS = "secret_sauce"
INVALID_USER = "invalid_user"
INVALID_PASS = "wrong_pass"

############################################## fixtures###############################################


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            slow_mo=100)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()


################################################# pages#################################################

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("navigate to {url}")
    def navigate(self, url: str):
        self.page.goto(url)

    @allure.step("get text content of selector {selector}")
    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector)

    @allure.step("check if selector {selector} is visible")
    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = ".error-message-container"

    @allure.step("navigate to login page")
    def navigate(self):
        super().navigate(BASE_URL)

    @allure.step("login with username {username} and password {password}")
    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    @allure.step("get text of error message")
    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)


class InventoryPage(BasePage):
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    FIRST_ITEM_ADD_BUTTON = ".inventory_item:first-child .btn_inventory"
    SHOPPING_CART_BADGE = ".shopping_cart_badge"
    SHOPPING_CART_LINK = ".shopping_cart_link"
    PRODUCT_SORT_DROPDOWN = ".product_sort_container"
    INVENTORY_ITEMS = ".inventory_item"
    INVENTORY_ITEM_NAME = ".inventory_item_name"
    INVENTORY_ITEM_PRICE = ".inventory_item_price"
    INVENTORY_ITEM_IMAGE = ".inventory_item_img"

    @allure.step("check if inventory page is loaded")
    def is_loaded(self) -> bool:
        return self.page.url == self.INVENTORY_URL

    @allure.step("add first item to cart")
    def add_first_item_to_cart(self):
        self.page.click(self.FIRST_ITEM_ADD_BUTTON)

    @allure.step("get count of items in cart")
    def get_cart_count(self) -> str:
        return self.get_text(self.SHOPPING_CART_BADGE)

    @allure.step("go to cart")
    def go_to_cart(self):
        self.page.click(self.SHOPPING_CART_LINK)


class CartPage(BasePage):
    CHECKOUT_BUTTON = "#checkout"

    @allure.step("go to checkout")
    def checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)


class CheckoutInfoPage(BasePage):
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"

    @allure.step("fill information with first name {first_name}, last name {last_name} and postal code {postal_code}")
    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)
        self.page.click(self.CONTINUE_BUTTON)


class CheckoutOverviewPage(BasePage):
    FINISH_BUTTON = "#finish"

    @allure.step("finish checkout")
    def finish_checkout(self):
        self.page.click(self.FINISH_BUTTON)


class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = ".complete-header"

    @allure.step("get confirmation message")
    def get_confirmation_message(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)


############################### tests ##############################
@allure.feature("always fail tests")
def test_always_fail():
    assert False


@allure.feature("login")
@pytest.mark.parametrize("user", [user for user in ALL_USERS if user != "locked_out_user"])
def test_valid_login(page, user):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login(user, VALID_PASS)

    assert inventory_page.is_loaded()


@allure.feature("login")
@pytest.mark.parametrize("user", [user for user in ALL_USERS if user != VALID_USER])
def test_invalid_login(page, user):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(INVALID_USER, INVALID_PASS)

    assert "Epic sadface" in login_page.get_error_message()


@allure.feature("inventory")
def test_images_are_visible(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login(VALID_USER, VALID_PASS)

    assert inventory_page.is_loaded()
    for item in inventory_page.page.locator(InventoryPage.INVENTORY_ITEMS).all():
        assert item.is_visible()
        assert item.locator(InventoryPage.INVENTORY_ITEM_NAME).first.is_visible()
        assert item.locator(InventoryPage.INVENTORY_ITEM_PRICE).first.is_visible()
        assert item.locator(InventoryPage.INVENTORY_ITEM_IMAGE).first.is_visible()


@allure.feature("inventory")
def test_add_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login(VALID_USER, VALID_PASS)
    inventory_page.add_first_item_to_cart()

    assert "1" in inventory_page.get_cart_count()


@allure.feature("inventory")
def test_checkout(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_info_page = CheckoutInfoPage(page)
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_complete_page = CheckoutCompletePage(page)

    login_page.navigate()
    login_page.login(VALID_USER, VALID_PASS)
    inventory_page.add_first_item_to_cart()

    inventory_page.go_to_cart()
    cart_page.checkout()

    checkout_info_page.fill_information("jan", "novak", "12345")
    checkout_overview_page.finish_checkout()
    assert "Thank you for your order!" in checkout_complete_page.get_confirmation_message()
