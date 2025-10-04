import pytest
from playwright.sync_api import sync_playwright
from PageObject.apiBase import apiBase


@pytest.fixture
def api_setup():
    # Set up Playwright instance for the test
    with sync_playwright() as playwright:
        # Initialize the API base class with playwright and logger
        api = apiBase(playwright)
        yield api
        # Cleanup or close any resources if necessary (if you have any close/cleanup logic)


def test_api_login(api_setup):
    # Test API login functionality
    response = api_setup.api()  # Call the API method to get the login response
    assert response.ok, f"API login failed with status {response.status}"


def test_api_user(api_setup):
    # Test fetching user list
    response = api_setup.user_list()  # Call the user_list method to fetch user data
    assert response, "Response was None, user list could not be fetched."
    assert response.ok, f"Failed to fetch user list. Status: {response.status}"
    assert response.status == 200, f"Expected status 200 but got {response.status}"

# def test_api_example(api_setup):
#     lp = api_setup.login_page
#     lp.nav_login()
#     lp.login_with_credentials(
#         username="lakshyasharmaqa@proton.me",
#         password="Tester@1234"
#     )
