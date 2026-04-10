"""
Author Name: ROBIN MAHANTA
Module: reporter.py
Purpose: Provides Allure reporting integration for test results.
Description: This module contains pytest hooks for capturing screenshots on test failures
             and attaching them to Allure reports for better diagnostic information.
"""

import pytest
import allure

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Author Name: ROBIN MAHANTA
    Function: pytest_runtest_makereport
    Purpose: Pytest hook to capture screenshots on test failures.
    Description: Intercepts test execution and captures a screenshot whenever a test fails,
                 then attaches it to the Allure report for better diagnostics.
    Parameters:
        - item: Pytest test item
        - call: Pytest call object
    Return Type: None
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            try:
                png = driver.get_screenshot_as_png()
                allure.attach(png, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Could not capture screenshot: {e}")