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
    Pytest fixture for LOCAL Chrome execution with automatic driver management
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
