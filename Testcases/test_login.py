# File: Tests/test_login.py

import pytest
from PageObject.LoginPage import LoginPage
from Utilities.logger import get_logger

logger = get_logger()


@pytest.fixture
def login_page(browser_page):
    """Fixture to initialize LoginPage with a browser page"""
    return LoginPage(browser_page)


def test_successful_login(login_page):
    """Test valid login flow"""

    # Step 1: Navigate to login page
    login_page.navigate_to_login()

    # Step 2: Perform login
    login_page.login_with_credentials(
        username="lakshyasharmaqa@proton.me",
        password="Tester@1234"
    )
    # Step 3: Assert login was successful
    assert login_page.is_logged_in(), "Login failed: Settings icon not visible"

    logger.info("Test completed successfully.")
