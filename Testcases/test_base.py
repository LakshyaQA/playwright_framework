from playwright.sync_api import Page
from Utilities.logger import get_logger

logger = get_logger()


def test_run_one(browser_page):
    page = browser_page

    page.goto("https://dev.aeye.pro/itc/login")
    logger.info("Opening Aeye Portal")

    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("lakshyasharmaqa@proton.me")
    logger.info("Username filled")

    page.locator('#password').click()  # Using the input's id attribute directly
    page.locator('#password').fill("Tester@1234")
    logger.info("Password filled")

    page.locator('button[tabindex="2"]').click()
    logger.info("Login Button clicked successfully!")

    logger.info("Test completed successfully!")
