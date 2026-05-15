# Playwright Enterprise Framework

A scalable, enterprise-grade UI automation framework built using **Playwright + Python + Pytest** following modern QA architecture patterns.

This framework is designed for:

* Enterprise UI automation
* Cross-browser testing
* Scalable test execution
* CI/CD integration
* API + UI combined automation strategy
* Parallel execution
* Reporting and logging
* Maintainable Page Object Model architecture

---

# Tech Stack

* **Language:** Python
* **Automation Tool:** Playwright
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM)
* **API Support:** Requests
* **Reporting:** Allure / HTML Reports
* **CI/CD:** GitHub Actions / Jenkins
* **Logging:** Python Logging
* **Configuration:** JSON / ENV based

---

# Framework Architecture

```text
playwright-enterprise-framework/
│
├── src/
│   ├── pages/                # Page Object classes
│   ├── tests/                # UI & API test cases
│   ├── utils/                # Utilities and helpers
│   ├── api/                  # API clients and services
│   ├── config/               # Environment configurations
│   ├── data/                 # Test data files
│   └── fixtures/             # Pytest fixtures
│
├── reports/                  # Test execution reports
├── logs/                     # Framework logs
├── screenshots/              # Failure screenshots
├── requirements.txt
├── pytest.ini
├── README.md
└── .github/workflows/        # CI pipelines
```

---

# Key Features

## UI Automation

* Cross-browser execution
* Headless and headed execution
* Parallel execution support
* Smart waits and retry mechanisms
* Screenshot capture on failure
* Video recording support
* Trace viewer support

## API Automation

* Reusable API client architecture
* BaseClient implementation
* Request and response validation
* API chaining support
* Token/session management

## Enterprise Capabilities

* Modular architecture
* Scalable folder structure
* Environment-based execution
* CI/CD ready
* Logging and reporting integration
* Data-driven testing
* Reusable utilities
* Configurable execution

---

# BaseClient Architecture

The framework uses a reusable `BaseClient` for API interactions.

```python
import requests

class BaseClient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://reqres.in/api"

    def get(self, url, params=None):
        return self.session.get(f"{self.base_url}/{url}", params=params)

    def post(self, url, payload=None):
        return self.session.post(f"{self.base_url}/{url}", json=payload)
```

## Why BaseClient?

* Centralized API handling
* Reusable session management
* Cleaner service layer implementation
* Easy authentication handling
* Better scalability and maintainability
* Reduced code duplication

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd playwright-enterprise-framework
```

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Playwright Browsers

```bash
playwright install
```

---

# Running Tests

## Run All Tests

```bash
pytest
```

## Run Specific Test

```bash
pytest src/tests/ui/test_homepage.py
```

## Run in Headed Mode

```bash
pytest --headed
```

## Run in Parallel

```bash
pytest -n auto
```

## Generate Allure Report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

# Environment Configuration

Configurations can be managed using:

* JSON configuration files
* Environment variables
* Command-line parameters

Example:

```json
{
  "base_url": "https://example.com",
  "browser": "chromium",
  "headless": true
}
```

---

# Reporting

The framework supports:

* Allure Reports
* HTML Reports
* Screenshots on failure
* Video recordings
* Execution logs
* Playwright traces

---

# CI/CD Integration

The framework can be integrated with:

* GitHub Actions
* Jenkins
* Azure DevOps
* GitLab CI

Example GitHub Actions workflow:

```yaml
name: Playwright Tests

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt
          playwright install

      - name: Execute Tests
        run: pytest
```

---

# Best Practices Followed

* Page Object Model (POM)
* Single Responsibility Principle
* Reusable utilities and fixtures
* Centralized configuration management
* Explicit assertions
* Scalable test organization
* Enterprise logging strategy
* Clean code principles

---

# Future Enhancements

* Docker support
* Kubernetes execution
* AI-powered self-healing locators
* Slack/Teams notifications
* Database validation layer
* Contract testing support
* Performance testing integration

---

# Author

Developed by Satnam Malhotra

QA Automation Architect | Playwright | API Automation | Enterprise Test Frameworks

---

# License

This project is licensed under the MIT License.
