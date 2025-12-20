import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.chrome.service import Service
from utilities.eventhandler import EventHandler


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture for LOCAL Chrome execution
    """

    event_handler = EventHandler()

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    # If chromedriver is in PATH, Service() is enough
    service = Service()

    base_driver = webdriver.Chrome(
        service=service,
        options=options
    )

    event_driver = EventFiringWebDriver(base_driver, event_handler)

    yield event_driver

    # Teardown
    event_driver.quit()
