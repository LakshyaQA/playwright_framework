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

##✅ Run Tests on Chrome (Headed Mode)
pytest -s -v Testcases/test_base.py --mybrowser=firefox --alluredir=reports/allure-results

#✅ Run Tests on Chrome (Headless Mode)
pytest -s -v Testcases/test_base.py --mybrowser=chromium --alluredir=reports/allure-results

-------------------------------------------------------------------------------------------------------------------

##📊 Generating Reports
Generate and Open Allure Report
allure serve reports/allure-results

------------------------------------------------------------------------------------------------------------
##🔧 Configuration
Browser Options

--mybrowser: Choose browser (chrome, firefox, webkit)
--headed: Run in headed mode (true/false)
Example Configuration in pytest.ini
ini[pytest]
addopts = -v -s --alluredir=reports/allure-results
testpaths = Testcases

-----------------------------------------------------------------------------------------------------------

## 📁 playwright_framework

```Python
playwright_framework/
│
├── .venv/
├── base/
│   ├── __init__.py
│   ├── base_page.py
│   └── playwright_factory.py
├── logs/
│   └── test_log.log
├── page_objects/
│   └── __init__.py
├── reports/
│   ├── allure-results/
│   └── allure-report/
├── screenshots/
├── tests/
│   ├── __init__.py
│   ├── test_base.py
│   └── test_search_thar.py
├── utilities/
│   ├── __init__.py
│   ├── logger.py
│   └── screenshot.py
│
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt 
