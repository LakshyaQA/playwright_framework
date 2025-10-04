# import time
#
# from playwright.sync_api import Page, expect, Playwright
#
# import pytest
# from PageObject.LoginPage import LoginPage
# from Utilities.logger import get_logger
#
# logger = get_logger()
#
#
# def test_serach_iphone(browser_page):
#     browser_page.goto("https://www.amazon.in/")
#     browser_page.fill("input#twotabsearchtextbox", "iphone")
#     browser_page.click("input#nav-search-submit-button")
#     page = browser_page
#
#     # Grab all titles using a stable attribute (replace with correct one if needed)
#     # titles = page.locator('[data-cy="title-recipe"]')  # If this attribute exists
#     time.sleep(2)
#     expect(page.locator('[data-cy="title-recipe"]').filter(has_text="Apple iPhone 15 (128 GB) - Blue")).to_be_visible()

# locator_one = page.locator('[data-cy="title-recipe"]').filter(has_text="Apple iPhone 15 (128 GB) - Blue")
# locator_one.get_by_role("link").click()

from playwright.sync_api import expect

# .get_by_role


def test_search_iphone(browser_page):
    # Step 1: Go to Amazon.in
    # browser_page.goto("https://www.amazon.in/")
    page = browser_page
    page.goto("https://www.amazon.in/")
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("iphone")
    page.get_by_role("searchbox", name="Search Amazon.in").press("Enter")

    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Sponsored Ad - Apple iPhone").click()
    page1 = page1_info.value
    page1.goto(
        "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY/ref=sr_1_1_sspa?crid=103AHP4GZE3PY&dib=eyJ2IjoiMSJ9.LAOeCfRf5hGlewzXDbccdg4hvE3MJpITvlRCn0rN4dFhDPQn-fIYfKJxxKAv6p4vygRYLBLonVDqJigRsV0rwVfiGehRx2PqLF625RHp61DAjesu0CCiURGkpUWKrwkc5MDwxs8YNE1pp2ZSdJg9WNj9H7bimqcA96ENy8R8gWYJQ0HrCPtqD_566GP9QjlUqXbCmMPQYByG66l0_ZZ2FPu0OnVr7wZ-HEfLKNFKslw.jyvotl654Kg7x2Y7zvTis0YOuBjMAPPas2iWcc3pW98&dib_tag=se&keywords=iphone&qid=1759517055&sprefix=iphone%2Caps%2C235&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
    page1.get_by_role("button", name="Without Exchange    47,999.00").click()
    page1.get_by_role("button", name="Buy Now").click()
    page1.get_by_role("textbox", name="Enter your mobile number or").click()
#
#     # Step 2: Search for 'iPhone'
#     browser_page.fill_text("input#twotabsearchtextbox", "iphone")
#     browser_page.click("input#nav-search-submit-button")
#
#     # Step 3: Wait for search results to load
#     browser_page.wait_for_selector('[data-cy="title-recipe"]', timeout=10000)
#
#     # Step 4: Locate all product titles
#     titles = browser_page.locator('[data-cy="title-recipe"]')
#     count = titles.count()
#     print(f"\n Total iPhone search results found: {count}")
#
#     # Step 5: Print all found titles
#     for i in range(count):
#         print(f"{i + 1}. {titles.nth(i).inner_text()}")
#
#     # Step 6: Assert some results were found
#     assert count > 0, " No search results found for 'iphone'"
#
#     # Step 7: Filter to find the specific iPhone model
#     target = titles.filter(has_text="Apple iPhone 15 (128 GB) - Blue")
#     expect(target).to_be_visible(timeout=5000)
#     assert target.count() > 0, " 'Apple iPhone 15 (128 GB) - Blue' not found in results"
#
#     print("\n Found the target iPhone model!")
#
# '''🧪 Test Scenario: Search and Verify iPhone on Amazon
#
# Title: Search for iPhone and verify a specific model is listed
#
# Steps:
#
# Open Amazon India: Navigate to https://www.amazon.in
#
# Search: Enter "iphone" in the search bar and submit.
#
# Wait for Results: Ensure product listings have loaded.
#
# Get Titles: Collect all product titles from the results.
#
# Print All Titles: Log them for visibility.
#
# Verify Presence: Check if "Apple iPhone 15 (128 GB) - Blue" is among the results.
#
# Assertion:
#
# ✅ At least one search result is shown.
#
# ✅ Target iPhone model exists in the results.'''
