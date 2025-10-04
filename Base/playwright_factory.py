from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import new_context


# from pytest_playwright.pytest_playwright import playwright


class PlaywrightFactory:
    def __init__(self, browser_name="chromium", headless=False, args=None):
        self.browser_name = browser_name
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self.args = args or ["--start-fullscreen"]

    def start_browser(self):
        self.playwright = sync_playwright().start()
        # playwright.chromium.launch()
        if self.browser_name == "chromium":
            self.browser = self.playwright.chromium.launch(headless=self.headless, args=self.args)
        elif self.browser_name == "firefox":
            self.browser = self.playwright.firefox.launch(headless=self.headless, args=self.args)
        elif self.browser_name == "webkit":
            self.browser = self.playwright.webkit.launch(headless=self.headless, args=self.args)
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

        self.context = self.browser.new_context(viewport=None)
        self.page = self.context.new_page()
        return self.page

    def stop_browser(self):
        try:
            if self.page:
                self.page.close()
            if self.context:
                self.context.close()
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()
        except Exception as e:
            print(f"Error closing browser: {e}")
