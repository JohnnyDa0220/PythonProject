# Apollo Pharmacy UI Test Automation Framework

This project is a comprehensive Selenium-based automated testing framework for the Apollo Pharmacy website (https://www.apollopharmacy.in/). It implements the Page Object Model (POM) design pattern to ensure maintainable and scalable test automation.

## Features

- **Page Object Model**: Clean separation of test logic and UI interactions
- **Comprehensive Logging**: Detailed logging for all actions with timestamps
- **Screenshot Capture**: Automatic screenshots on failures and key actions
- **Excel Data-Driven Testing**: Test data management using Excel files
- **Cross-Browser Support**: Configured for Chrome (easily extensible)
- **Test Reporting**: Integration with Allure for detailed HTML reports
- **Event Listening**: Selenium event firing for enhanced traceability

## Project Structure

```
PythonProject/
├── config/
│   └── configproperties.ini    # Configuration settings
├── pages/                      # Page Object classes
├── uistore/                    # UI element locators
├── utilities/                  # Helper utilities
│   ├── web_driver_helper.py    # Selenium wrapper
│   ├── config_reader.py        # Configuration reader
│   ├── excel_reader.py         # Excel data reader
│   ├── logger.py               # Logging utility
│   ├── screenshot.py           # Screenshot utility
│   └── reporter.py             # Allure reporting
├── testdata/
│   └── apollo.xlsx             # Test data
├── tests/
│   └── test_execution_file.py  # Test cases
├── logs/                       # Generated log files
├── screenshot/                 # Generated screenshots
├── conftest.py                 # Pytest fixtures
└── pytest.ini                  # Pytest configuration
```

## Prerequisites

- Python 3.8+
- Chrome browser (Selenium will auto-download the driver)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JohnnyDa0220/PythonProject.git
   cd PythonProject
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux/Mac:
   source .venv/bin/activate
   ```

3. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

No manual configuration needed! The framework uses:
- **Relative paths** that work across all platforms
- **Environment variable support** for overriding config values
- **Auto-managed ChromeDriver** - automatically downloaded and managed

Optional: Update `config/configproperties.ini` for custom settings:

```ini
[URL]
website_url=https://www.apollopharmacy.in/

[PATH]
logger_path=logs
screenshot_path=screenshot
excel_path=testdata/apollo.xlsx
reporter_path=Report

[BROWSER]
headless=true              # Set to false to see browser during execution
wait_timeout=10           # Timeout for element waits in seconds

[LOG]
level=INFO
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

**Override via Environment Variables:**
```bash
# Example: Override base URL via environment variable
export URL_website_url=https://www.apollopharmacy.in/

# Or on Windows PowerShell:
$env:URL_website_url = "https://www.apollopharmacy.in/"
```

## Running Tests

### Run all tests:
```bash
pytest tests/ -v
```

### Run specific test:
```bash
pytest tests/test_execution_file.py::Test_Page::test_method_add_crocin_to_cart -v
```

### Run smoke tests:
```bash
pytest -m smoke tests/ -v
```

### Run with visible browser (non-headless):
```bash
# Edit config/configproperties.ini and set: headless=false
# OR set environment variable:
export BROWSER_headless=false
pytest tests/ -v
```

### Generate Allure report:
```bash
pytest --alluredir=Report tests/ -v
allure serve Report/
```

### Run tests in parallel (requires pytest-xdist):
```bash
pip install pytest-xdist
pytest tests/ -v -n auto
```

## Test Cases

### Active Tests
- **Add Crocin to Cart**: Complete e-commerce flow from search to cart

### Commented Tests (can be enabled)
- Honey product flow
- Baby care products
- Health devices
- Footer link verification
- Personal care products

## Key Components

### WebDriverHelper
Enhanced Selenium wrapper providing:
- Element highlighting before interaction
- Automatic screenshot capture
- Flexible locator support
- Comprehensive logging

### Page Objects
Each page has a corresponding class with methods for user interactions:
- `HomePage`: Homepage interactions
- `SearchMedicinePage`: Medicine search
- `CrocinResultPage`: Search results
- `FirstProductPage`: Product details
- `CartPage`: Cart operations

### Utilities
- **Config Reader**: Reads INI configuration files
- *Troubleshooting

### ChromeDriver Issues

**Error: "chromedriver not found"**
- Solution: The framework uses `webdriver-manager` to auto-download drivers. Ensure you installed dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- If still failing, clear cache:
  ```bash
  rm -rf ~/.wdm/  # On Linux/Mac
  rmdir %USERPROFILE%\.wdm\  # On Windows
  ```

### File Path Issues

**Error: "No such file or directory" for logs/screenshot/excel files**
- Solution: Paths in `configproperties.ini` are now relative (e.g., `logs` instead of `C:\Users\...`)
- The framework automatically creates required directories
- Ensure you're running tests from the project root directory

### Import Errors

**Error: "ModuleNotFoundError: No module named 'selenium'"**
- Solution: Reinstall dependencies:
  ```bash
  pip install -r requirements.txt --force-reinstall
  ```

**Error: ImportError in conftest.py**
- Solution: Ensure Python path includes the project root:
  ```bash
  cd /path/to/PythonProject
  pytest tests/
  ```

### Element Not Found Errors

**Error: "NoSuchElementException" or "TimeoutException"**
- Possible causes:
  1. Apollo Pharmacy website UI has changed (XPath/CSS selectors outdated)
  2. Element takes longer to load - increase timeout in `configproperties.ini`:
     ```ini
     [BROWSER]
     wait_timeout=20
     ```
  3. Page not fully loaded - verify in non-headless mode:
     ```ini
     [BROWSER]
     headless=false
     ```

### Test Failures in CI/CD

**Tests pass locally but fail in GitHub Actions**
- Solution: CI runs in headless mode by default (recommended)
- Check artifact uploads for screenshots/logs to debug:
  ```bash
  pip install allure-pytest
  allure serve Report/
  ```

### Configuration Not Being Read

**Changes to configproperties.ini not taking effect**
- Solution: Clear Python cache:
  ```bash
  find . -name "__pycache__" -type d -exec rm -rf {} +  # Linux/Mac
  Get-ChildItem -Path . -Directory -Name "__pycache__" | Remove-Item -Recurse  # Windows
  ```
- Restart your Python process/IDE

### Headless Mode Issues

**Error: "Chrome is not reachable" in headless mode**
- Solution: Add sandbox disabling in headless mode (already in conftest.py):
  ```python
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  ```

### Virtual Environment Issues

**Error: "source: not found" or activation fails**
- On Windows, use:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- If execution policy error, run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

### Test Data Issues

**Error: "File not found" for excel_path in apollo.xlsx**
- Ensure `testdata/apollo.xlsx` exists
- Verify the path in `configproperties.ini` is correct (relative to project root)
- Check sheet name and cell references in test code match the Excel file

### Logging Issues

**Logs not being generated**
- Ensure `logs/` directory has write permissions
- Check `logger_path` in `configproperties.ini` is readable
- Verify `[LOG]` section exists in `configproperties.ini`

### Common Questions

**Q: Can I run tests on other browsers?**
A: Currently configured for Chrome. To add Firefox/Edge, extend `conftest.py` with additional browser fixtures and update configuration.

**Q: How to run tests in batch/schedule them?**
A: Use GitHub Actions (`.github/workflows/ci.yml` included) or schedule locally with cron/Task Scheduler.

**Q: How to integrate with CI/CD?**
A: Framework is pre-configured for GitHub Actions. For other CI tools (Jenkins, GitLab CI), follow similar patterns in `.github/workflows/ci.yml`.

**Q: How to add new tests?**
A: 
1. Create new page object in `pages/` with methods for user interactions
2. Create corresponding locators in `uistore/`
3. Add test method in `tests/test_execution_file.py`
4. Use pytest markers (`@pytest.mark.smoke`, etc.) for categorizationb Actions or similar
5. **Browser Compatibility**: Currently Chrome-only
6. **Test Data Management**: Improve parameterization

## Contributing

1. Follow Page Object Model principles
2. Add comprehensive logging
3. Include screenshots for debugging
4. Update locators in `uistore/` when UI changes
5. Add test data to `testdata/apollo.xlsx`

## License

Private project - All rights reserved.
