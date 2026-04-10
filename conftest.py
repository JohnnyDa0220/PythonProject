"""
Author Name: ROBIN MAHANTA
Module: conftest.py
Purpose: Pytest configuration and fixture definitions.
Description: This module contains pytest fixtures used throughout the test suite,
             including the driver fixture which provides automated WebDriver instances
             for browser automation testing.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utilities.eventhandler import EventHandler
from utilities.config_reader import get_properties


@pytest.fixture(scope="function")
def driver():
    """
    Author Name: ROBIN MAHANTA
    Fixture: driver
    Purpose: Provides a Selenium WebDriver instance for test execution.
    Description: Creates a Chrome WebDriver with EventFiringWebDriver wrapper for event logging.
                 Automatically manages ChromeDriver version and applies test configuration.
                 Fixture scope is function level, providing a fresh driver for each test.
    Return Type: selenium.webdriver.remote.webdriver.WebDriver (EventFiringWebDriver wrapped)
    Configuration:
        - Headless mode: Read from config [BROWSER] headless setting
        - Auto-download: ChromeDriver automatically downloaded via webdriver-manager
        - Options: Maximized window, notifications disabled, sandboxing options
    Yields:
        EventFiringWebDriver instance for test execution
    Teardown:
        Quits the driver after test completion to cleanup resources
    """

    event_handler = EventHandler()

    options = webdriver.ChromeOptions()
    
    # Read headless setting from config
    headless = get_properties("BROWSER", "headless").lower() == "true"
    if headless:
        options.add_argument("--headless")
    
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Automatically download and manage ChromeDriver
    service = Service(ChromeDriverManager().install())

    base_driver = webdriver.Chrome(
        service=service,
        options=options
    )

    event_driver = EventFiringWebDriver(base_driver, event_handler)

    yield event_driver

    # Teardown
    event_driver.quit()
