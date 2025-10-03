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

from playwright.sync_api import expect


def test_search_iphone(browser_page):
    # Step 1: Go to Amazon.in
    browser_page.goto("https://www.amazon.in/")

    # Step 2: Search for 'iPhone'
    browser_page.fill("input#twotabsearchtextbox", "iphone")
    browser_page.click("input#nav-search-submit-button")

    # Step 3: Wait for search results to load
    browser_page.wait_for_selector('[data-cy="title-recipe"]', timeout=10000)

    # Step 4: Locate all product titles
    titles = browser_page.locator('[data-cy="title-recipe"]')
    count = titles.count()
    print(f"\n Total iPhone search results found: {count}")

    # Step 5: Print all found titles
    for i in range(count):
        print(f"{i + 1}. {titles.nth(i).inner_text()}")

    # Step 6: Assert some results were found
    assert count > 0, " No search results found for 'iphone'"

    # Step 7: Filter to find the specific iPhone model
    target = titles.filter(has_text="Apple iPhone 15 (128 GB) - Blue")
    expect(target).to_be_visible(timeout=5000)
    assert target.count() > 0, " 'Apple iPhone 15 (128 GB) - Blue' not found in results"

    print("\n Found the target iPhone model!")

'''🧪 Test Scenario: Search and Verify iPhone on Amazon

Title: Search for iPhone and verify a specific model is listed

Steps:

Open Amazon India: Navigate to https://www.amazon.in

Search: Enter "iphone" in the search bar and submit.

Wait for Results: Ensure product listings have loaded.

Get Titles: Collect all product titles from the results.

Print All Titles: Log them for visibility.

Verify Presence: Check if "Apple iPhone 15 (128 GB) - Blue" is among the results.

Assertion:

✅ At least one search result is shown.

✅ Target iPhone model exists in the results.'''
