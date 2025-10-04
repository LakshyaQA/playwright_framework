# File: Tests/test_login.py
import json
import os
import pytest
from PageObject.LoginPage import LoginPage
from Utilities.logger import get_logger

logger = get_logger()

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root)

# Define the relative path to the config file
config_file_path = os.path.join(project_root, 'Base', 'configuration', 'config.json')
# Load the config file
with open(config_file_path) as f:
    config = json.load(f)
    dev_cred_list = config['dev_creds']


@pytest.fixture
def login_page(browser_page):
    """Fixture to initialize LoginPage with a browser page"""
    return LoginPage(browser_page)


@pytest.mark.parametrize("dev_creds", dev_cred_list)
def test_successful_login(login_page, dev_creds):
    """Test valid login flow"""

    # Step 1: Navigate to login page
    login_page.navigate_to_login()
    login_page.login_with_credentials(
        username=dev_creds['username'],
        password=dev_creds['password']
    )
    # Step 3: Assert login was successful
    assert login_page.is_logged_in(), "Login failed: Settings icon not visible"

    logger.info("Test completed successfully.")
