import pytest
import allure
from Utilities.screenshot import capture_screenshot
from Base.playwright_factory import PlaywrightFactory
from Utilities.logger import get_logger


# ------------------ Pytest CLI Options ------------------
def pytest_addoption(parser):
    parser.addoption("--mybrowser", action="store", default="chromium",
                     help="Browser: chromium, firefox, webkit")
    parser.addoption("--headless", action="store_true",
                     help="Run tests in headless mode")
    parser.addoption("--fullscreen", action="store_true",
                     help="Launch browser in fullscreen mode")


# ------------------ Browser Fixture ------------------
@pytest.fixture(scope="function")
def browser_page(request, logger):
    browser_name = request.config.getoption("--mybrowser")
    headless = request.config.getoption("--headless")
    fullscreen = request.config.getoption("--fullscreen")

    args = ["--start-fullscreen"] if fullscreen else []
    factory = PlaywrightFactory(browser_name=browser_name, headless=headless, args=args)

    logger.info(f"Launching {browser_name} browser (headless={headless}).")

    page = factory.start_browser()
    yield page
    factory.stop_browser()
    logger.info("Browser session stopped.")


# ------------------ Screenshot & Allure Hook ------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("browser_page", None)
        if page:
            # Save screenshot locally
            path = capture_screenshot(page, item.name)
            logger.error(f"Test failed! Screenshot saved at {path}")

            # Attach screenshot in Allure
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"{item.name}_Failure_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Attach log reference in Allure
            allure.attach(
                body=f"Check logs at {path}",
                name="Log Info",
                attachment_type=allure.attachment_type.TEXT
            )
            logger.info("Screenshot and log info attached to Allure report.")


# Define the logger fixture
@pytest.fixture(scope="session")
def logger():
    return get_logger()
