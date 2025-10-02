from Utilities.logger import get_logger
import allure

logger = get_logger()

@allure.feature("CarDekho Search")
@allure.story("Search Thar Vehicle")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_thar(browser_page):
    page = browser_page
    logger.info("Opening CarDekho website...")


    allure.attach(body="Opening CarDekho...", name="Step Log", attachment_type=allure.attachment_type.TEXT)

    page.goto("https://www.cardekho.com/")
    page.wait_for_selector("text=Thar")

    logger.info("Searching for 'Thar'...")
    page.fill("input#cardekhosearchtext", "Thar")
    page.keyboard.press("Enter")

    logger.info("Waiting for results...")
    page.wait_for_selector("text=Thar")

    assert "Thar" in page.inner_text("body"), "Thar not found in search results!"
    allure.attach(body="Thar found successfully!", name="Validation", attachment_type=allure.attachment_type.TEXT)

    logger.info("Thar vehicle found successfully!")
