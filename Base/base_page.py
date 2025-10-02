class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator: str):
        self.page.locator(locator).click()

    def type_text(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str):
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator: str):
        return self.page.locator(locator).is_visible()