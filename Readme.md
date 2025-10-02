# 🧪 Playwright Automation Framework (Pytest + Allure)

This framework uses **Playwright with Pytest** for end-to-end testing and **Allure** for advanced reporting.

-------------------------------------------------------------------------------------------------------------------

## 📦 Prerequisites

Before running tests, ensure you have the following installed:

- Python 3.8+
- pytest
- pytest-playwright
- allure-pytest
- Allure command-line (for report generation)
- Playwright browsers (install via: `playwright install`)

-------------------------------------------------------------------------------------------------------------------

## 🛠️ Setup Instructions

Create Virtual Environment
python -m venv .venv
Activate Virtual Environment
Windows:
bash.venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Install Playwright Browsers
playwright install

-------------------------------------------------------------------------------------------------------------------

## 🚀 Running Tests

You can run tests with different browsers and modes (headed/headless) using command-line options.

### ✅ Run on **Any Browser** (Headed/Headless Mode) :

✅ Run Tests on Chrome (Headed Mode)
pytest -s -v Testcases/test_base.py --mybrowser=firefox --alluredir=reports/allure-results
✅ Run Tests on Chrome (Headless Mode)
pytest -s -v Testcases/test_base.py --mybrowser=chromium --alluredir=reports/allure-results

-------------------------------------------------------------------------------------------------------------------

📊 Generating Reports
Generate and Open Allure Report
allure serve reports/allure-results

------------------------------------------------------------------------------------------------------------
🔧 Configuration
Browser Options

--mybrowser: Choose browser (chrome, firefox, webkit)
--headed: Run in headed mode (true/false)
Example Configuration in pytest.ini
ini[pytest]
addopts = -v -s --alluredir=reports/allure-results
testpaths = Testcases

-----------------------------------------------------------------------------------------------------------

📁 Project Structure
playwright_framework/
│
├── .venv/ # Virtual environment
├── Base/ # Base configurations
│ ├── __init__.py
│ ├── base_page.py
│ └── playwright_factory.py
├── Logs/ # Test execution logs
│ └── test_log.log
├── PageObject/ # Page Object Models
│ └── __init__.py
├── reports/ # Test reports
│ ├── allure-results/ # Raw allure data
│ └── allure-report/ # Generated HTML reports
├── screenshots/ # Test screenshots
├── Testcases/ # Test files
│ ├── __init__.py
│ ├── test_base.py
│ └── test_search_thar.py
├── Utilities/ # Utility functions
│ ├── __init__.py
│ ├── logger.py
│ └── screenshot.py
├── commands.txt # Useful commands
├── conftest.py # Pytest fixtures
├── pytest.ini # Pytest configuration
├── Readme.md # Project documentation
├── requirements.txt # Python dependencies
└── scratch.txt # Notes

