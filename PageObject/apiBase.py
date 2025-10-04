from playwright.sync_api import APIRequestContext, Playwright
from Utilities.logger import get_logger

# Logger initialization
logger = get_logger()

# Login payload and headers
login_payload = {
    "email": "lakshyasharmaqa@proton.me",  # Ensure the email format is correct
    "password": "Tester@1234"  # Ensure the password format is correct
}

login_headers = {
    "Content-Type": "application/json; charset=utf-8",  # Ensure this is correct
    "Accept": "application/json"  # Some APIs also expect the Accept header
}


class apiBase:
    def __init__(self, playwright: Playwright, logger=None):
        self.playwright = playwright
        self.logger = logger if logger else get_logger()

    def api(self):
        # Create a new isolated API request context
        request_context: APIRequestContext = self.playwright.request.new_context(
            base_url="https://dev.aeye.pro"
        )

        # Send login request
        response = request_context.post(
            "/apps/itc/user_manager/api/v1/login",
            data=login_payload,
            headers=login_headers
        )

        # Log the response status and details
        if response.ok:
            self.logger.info("API login successful")
        else:
            self.logger.error(f"API login failed - Status: {response.status}")
            self.logger.error(f"Response: {response.text()}")

        # Log the full response JSON for debugging
        try:
            json_data = response.json()
            self.logger.debug(f"Login Response JSON: {json_data}")
        except Exception as e:
            self.logger.error(f"Failed to parse login response as JSON: {str(e)}")

        return response

    def user_list(self):
        # Call the api() method to get the token
        token_response = self.api()

        # Make sure the response is successful
        if not token_response.ok:
            self.logger.error(f"Failed to retrieve token: {token_response.status} {token_response.status_text}")
            return None

        # Extract JSON from the response to get the token
        try:
            token_data = token_response.json()  # Convert the response body to a dictionary
        except Exception as e:
            self.logger.error(f"Failed to parse token response: {str(e)}")
            return None

        # Log the response JSON to debug token extraction
        self.logger.debug(f"Token Response JSON: {token_data}")

        # Check if the token is present in the response data
        if 'data' not in token_data or 'token' not in token_data['data'] or 'access' not in token_data['data']['token']:
            self.logger.error("Token not found in the API response.")
            return None

        token = token_data['data']['token']['access']  # Correctly access the token
        self.logger.debug(f"Token retrieved: {token}")  # Debugging log to ensure token is correct

        # Set up the headers for the user list request
        user_headers = {
            "Content-Type": "application/json",  # Correct Content-Type header
            "Accept": "application/json, text/plain, */*",  # Correct Accept header
            "Authorization": f"Bearer {token}"  # Correct Authorization header with token
        }

        # Log the Authorization header for debugging
        self.logger.debug(f"Authorization Header: {user_headers['Authorization']}")  # Debugging log

        # Create a new isolated API request context
        request_context: APIRequestContext = self.playwright.request.new_context(
            base_url="https://dev.aeye.pro"
        )

        # Send the GET request to fetch the user list
        response = request_context.get(
            "apps/itc/reports/api/v1/candidates?limit=5&offset=1&search=&ordering=-starts_at",
            headers=user_headers
        )

        # Log and return the response for debugging
        if response.ok:
            self.logger.info("User list fetched successfully")
        else:
            self.logger.error(f"Failed to fetch user list - Status: {response.status}")
            self.logger.error(f"Response: {response.text()}")

        return response
