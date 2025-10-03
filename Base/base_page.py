# base_page.py
from playwright.sync_api import Page
from Utilities.logger import get_logger

logger = get_logger()

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

    def navigate_to(self, url: str):
        """Navigate to a URL"""
        self.page.goto(url)
        self.logger.info(f"Navigated to: {url}")

    def click_element(self, selector: str):
        """Click on an element"""
        self.page.locator(selector).click()
        self.logger.info(f"Clicked element: {selector}")

    def fill_text(self, selector: str, text: str):
        """Fill text in an input field"""
        self.page.locator(selector).fill(text)
        self.logger.info(f"Filled text in: {selector}")

    def type_text(self, selector: str, text: str):
        """Type text with keyboard simulation"""
        self.page.locator(selector).type(text)
        self.logger.info(f"Typed text in: {selector}")

    def press_keys(self, selector: str, keys: str):
        """Press keyboard keys on an element"""
        self.page.locator(selector).press(keys)
        self.logger.info(f"Pressed '{keys}' on: {selector}")

    def get_text(self, selector: str) -> str:
        """Get text from an element"""
        text = self.page.locator(selector).inner_text()
        self.logger.info(f"Got text from {selector}: {text}")
        return text

    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        visible = self.page.locator(selector).is_visible()
        self.logger.info(f"Element {selector} visible: {visible}")
        return visible

    def wait_until_visible(self, selector: str, timeout: int = 5000):
        """Wait for element to be visible"""
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)
        self.logger.info(f"Element {selector} is now visible")

    def wait_until_attached(self, selector: str, timeout: int = 5000):
        """Wait for element to be attached"""
        self.page.locator(selector).wait_for(state="attached", timeout=timeout)
        self.logger.info(f"Element {selector} is now attached")

    def get_by_label_and_click(self, label: str):
        """Get element by label and click"""
        self.page.get_by_label(label).click()
        self.logger.info(f"Clicked element with label: {label}")

    def get_by_label_and_fill(self, label: str, text: str):
        """Get element by label and fill text"""
        self.page.get_by_label(label).fill(text)
        self.logger.info(f"Filled text in label: {label}")

    def clear_input(self, selector: str):
        """Clear an input field"""
        self.page.locator(selector).clear()
        self.logger.info(f"Cleared input: {selector}")

    def click(self, selector: str):
        self.page.locator(selector).click()

