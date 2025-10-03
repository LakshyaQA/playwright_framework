# File: PageObject/LoginPage.py

from playwright.sync_api import Page
from Base.base_page import BasePage
from Utilities.logger import get_logger

logger = get_logger()


class LoginPageLocators:
    """Locators for Login Page elements"""
    USERNAME_LABEL = "Username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = 'button[tabindex="2"]'
    DASHBOARD_HEADING = 'h2:has-text("Dashboard")'  # post-login element to verify success


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.logger = logger

    def navigate_to_login(self, url: str = "https://dev.aeye.pro/itc/login"):
        """Navigate to the login page"""
        self.navigate_to(url)
        self.logger.info(f"Navigated to: {url}")

    def fill_username(self, username: str):
        self.page.get_by_label(LoginPageLocators.USERNAME_LABEL).fill(username)
        self.logger.info("Username filled")

    def fill_password(self, password: str):
        self.page.locator(LoginPageLocators.PASSWORD_INPUT).fill(password)
        self.logger.info("Password filled")

    def click_login_button(self):
        self.page.locator(LoginPageLocators.LOGIN_BUTTON).click()
        self.logger.info("Login button clicked")

    def login_with_credentials(self, username: str, password: str):
        """Perform full login sequence"""
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()
        self.logger.info(f"Login attempted with username: {username}")
        try:
            self.page.wait_for_selector(LoginPageLocators.DASHBOARD_HEADING, timeout=5000)
            self.logger.info("Login successful — Dashboard loaded.")
        except Exception as e:
            self.page.screenshot(path="login_failed.png")
            self.logger.error(f"Login failed or dashboard not visible: {e}")
            raise

    def is_logged_in(self) -> bool:
        """Verify login success by checking visibility of a post-login element"""
        try:
            return self.page.locator(LoginPageLocators.DASHBOARD_HEADING).is_visible()
        except Exception as e:
            self.logger.error(f"Login verification failed: {e}")
            return False
