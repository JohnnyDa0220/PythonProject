from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from utilities.screenshot import Screenshot
from selenium.webdriver.remote.webdriver import WebDriver
from logging import Logger

class WebDriverHelper:
    """
    Author: Robin Mahanta
    Class: WebDriverHelper
    Purpose:
        A utility wrapper around Selenium WebDriver operations providing common actions
        like locating elements, clicking, sending keys, scrolling, window switching,
        presence verification, and hover interactions. Each action includes structured
        logging and optional full-page screenshots for traceability.
    Attributes:
        driver (selenium.webdriver): The active Selenium WebDriver instance.
        logger (logging.Logger): Logger used for structured info/warning/error messages.
    """
    def __init__(self, driver: WebDriver, logger: Logger):
        """
        Author: Robin Mahanta
        Initialize the WebDriverHelper.
        Parameters:
            driver (selenium.webdriver): The Selenium WebDriver instance to operate with.
            logger (logging.Logger): Logger for emitting action-level diagnostics.
        Returns:
            None
        """
        self.driver = driver
        self.logger = logger

    def find_an_element(self, locator, elements, timeout=10):
        """
        Author: Robin Mahanta
        Locate a single element using an explicit wait until presence is detected.
        Parameters:
            locator (tuple): A locator tuple (By, value), e.g., (By.ID, "username").
            elements (str): A human-readable name/label for logging (e.g., "Username field").
            timeout (int, optional): Max seconds to wait for presence. Defaults to 10.
        Returns:
            selenium.webdriver.remote.webelement.WebElement | None:
                The located element if found within the timeout; otherwise None.
        Notes:
            - Uses `presence_of_element_located`, which does not guarantee visibility.
            - Emits info logs on success and error logs on failure.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
            self.logger.info(f"{elements} found with locator {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Error finding {elements} with locator {locator}: {e}")
            return None

    def click_on_element(self, locator, button_to_be_clicked):
        """
        Author: Robin Mahanta
        Click a located element and capture a screenshot for traceability.
        Parameters:
            locator (tuple): A locator tuple (By, value) to identify the element.
            elements (str): A label used for logs and screenshot naming.
            self.logger.info(f"Click on {button_to_be_clicked}")
        Returns:
            None
        Behavior:
            - Highlights the element in yellow before clicking, then resets style.
            - Captures a full-page screenshot after clicking.
            - On failure, captures an error screenshot and logs the exception.
        """
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
            Screenshot.capture_full_screenshot(self.driver, button_to_be_clicked)
            self.driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)
            self.driver.execute_script("arguments[0].style.border=''", element)
            element.click()
            # self.driver.execute_script("arguments[0].setAttribute('onclick', 'this.style.backgroundColor=\"red\";');", element)
            try:
                self.driver.execute_script("arguments[0].style.backgroundColor = '';", element)
            except:
                pass
            self.logger.info(f"Clicked on {button_to_be_clicked}")
            Screenshot.capture_full_screenshot(self.driver, f"{button_to_be_clicked}")
            self.logger.info(f"taken screenshot of element {button_to_be_clicked}")
        except Exception as e:
            self.logger.error(f"Error occured while clicking on {button_to_be_clicked}: {e}")
            Screenshot.capture_full_screenshot(self.driver, f"{button_to_be_clicked}_error")
            raise Exception("Error in " + str(e))

    def input_text_then_enter(self, locator, text, elements):
        """
        Author: Robin Mahanta
        Clear an input, type the provided text, press ENTER, and capture a screenshot.
        Parameters:
            locator (tuple): Locator to find the input element.
            text (str): The text to send to the element.
            elements (str): A label used for logs and screenshot naming.
        Returns:
            None
        Behavior:
            - Clears the input, highlights it, sends text and ENTER, then un-highlights.
            - Captures a full-page screenshot and logs success.
            - Logs and screenshots on failure.
        """
        try:
            element = self.find_an_element(locator, elements)
            if element:
                element.clear()
                self.driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)
                # self.driver.execute_script("arguments[0].style.border='3px solid green'", element)
                element.send_keys(text, Keys.RETURN)
                self.driver.execute_script("arguments[0].style.backgroundColor = '';", element)
                # self.driver.execute_script("arguments[0].style.border=''", element)
                Screenshot.capture_full_screenshot(self.driver, f"{elements}")
                self.logger.info(f"Sent text '{text}' and ENTER to {elements}")
            else:
                raise Exception(f"{elements} not found")
        except Exception as e:
            self.logger.error(f"Error sending text to {elements} with locator {locator}: {e}")
            Screenshot.capture_full_screenshot(self.driver, f"{elements}")

    def send_keys_to_element(self, locator, elements, keys):
        """
        Author: Robin Mahanta
        Send keyboard input to a located element and log the action.
        Parameters:
            locator (tuple): Locator to find the target element.
            elements (str): A descriptive label for logging.
            keys (str | list | selenium.webdriver.common.keys.Keys):
                Keys or text to send. Can be a string or Selenium Keys.
        Returns:
            None
        Behavior:
            - Temporarily highlights the element during key send.
            - Logs success or failure and captures a screenshot on error.
        """
        try:
            element = self.find_an_element(locator, elements)
            if element:
                self.driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)
                self.driver.execute_script("arguments[0].style.border='3px solid green'", element)
                element.clear()
                element.send_keys(keys)
                self.driver.execute_script("arguments[0].style.backgroundColor = '';", element)
                self.driver.execute_script("arguments[0].style.border=''", element)
                self.logger.info(f"Sent keys {keys} to {elements}")
                self.logger.info(f"Sent keys to {elements} with locator {locator}")
            else:
                raise Exception(f"{elements} not found")
        except Exception as e:
            self.logger.error(f"Error sending keys to {elements} with locator {locator}: {e}")
            Screenshot.capture_full_screenshot(self.driver, f"{elements}")

    def scroll_to_element(self, locator, elements, timeout=10):
        """
        Author: Robin Mahanta
        Scroll the page until the target element is in view and log the action.
        Parameters:
            locator (tuple): Locator to find the target element.
            elements (str): A descriptive label used for logging.
            timeout (int, optional): Max seconds to wait for element visibility. Defaults to 10.
        Returns:
            None
        Behavior:
            - Waits for `visibility_of_element_located`.
            - Executes `scrollIntoView()` and captures a full-page screenshot.
            - Logs success or error.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            Screenshot.capture_full_screenshot(self.driver, f"{elements}")
            self.logger.info(f"Scrolled to {elements} successfully")
        except Exception as e:
            self.logger.error(f"An Error occurred while scrolling to {elements}: {e}")
            Screenshot.capture_full_screenshot(self.driver, f"{elements}")

    def switch_to_new_window(self):
        """
        Author: Robin Mahanta
        Switch the driver's context to the most recently opened window if available.
        Parameters:
            None
        Returns:
            bool:
                True if a new window was found and switched to; False otherwise.
        Behavior:
            - Checks `driver.window_handles` and switches to the last handle when multiple exist.
            - Logs the outcome or any error encountered.
        """
        try:
            window_handles = self.driver.window_handles
            if len(window_handles) > 1:
                self.driver.switch_to.window(window_handles[-1])
                self.logger.info("Switched to new window")
                return True
            else:
                self.logger.warning("No new window found to switch to")
                return False
        except Exception as e:
            self.logger.error(f"Error switching to new window: {e}")
            return False

    def verify_presence(self, locator, elements, timeout=10):
        """
        Author: Robin Mahanta
        Assert that an element is present in the DOM and log the verification.
        Parameters:
            locator (tuple): Locator to find the target element.
            elements (str): A descriptive label for logging and screenshots.
            timeout (int, optional): Max seconds to wait for presence. Defaults to 10.
        Returns:
            bool:
                True if presence assertion passes; False if assertion fails or an error occurs.
        Behavior:
            - Uses `find_an_element` to retrieve the element.
            - Highlights the element briefly when present.
            - Captures screenshots and logs pass/fail details.
        """
        try:
            element = self.find_an_element(locator, elements, timeout)
            assert element is not None, f"{elements} with locator {locator} should be present."
            self.driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)
            self.logger.info(f"Assertion Pass: {elements} with locator {locator} is present.")
            self.driver.execute_script("arguments[0].style.backgroundColor = '';", element)
            Screenshot.capture_full_screenshot(self.driver, f"{elements}")
            return True
        except AssertionError as ae:
            self.logger.warning(f"Assertion Fail: {ae}")
            Screenshot.capture_full_screenshot(self.driver, f"{elements}")
            return False
        except Exception as e:
            self.logger.error(f"Error during presence verification of {elements} with locator {locator}: {e}")
            Screenshot.capture_full_screenshot(self.driver, f"{elements}")
            return False

    def verify_text_presence(self, locator, expected_text):
        """
        Author: Robin Mahanta
        Verify that a specific text is present in the current URL.
        Parameters:
            expected_text (str): The text expected to be found in the URL.
        Returns:
            None
        Behavior:
            - Retrieves the current URL from the browser.
            - Checks if the expected text is part of the URL.
            - Logs a PASS if the expected text is found; otherwise logs a FAIL.
            - Logs any exceptions encountered during the process.
        """

        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(ec.visibility_of_element_located(locator))
            actual_text = element.text.strip()
            try:
                assert expected_text in actual_text
                self.logger.info(f"Assertion PASS: {expected_text} is found on the page")
            except AssertionError as ae:
                self.logger.info(f"Assertion FAIL: {ae}")
        except Exception as e:
            self.logger.error(f"Error verifying text presence: {e}")

    def hover_on_single_element(self, locator, elements, timeout=10):
        """
        Author: Robin Mahanta
        Hover the mouse over a single located element using ActionChains.
        Parameters:
            locator (tuple): Locator to find the target element.
            elements (str): A descriptive label for logging and screenshots.
            timeout (int, optional): Max seconds to wait for presence. Defaults to 10.
        Returns:
            bool:
                True if hover action succeeds; False if element not found or an error occurs.
        Behavior:
            - Highlights the element, performs a hover, then resets styling.
            - Captures a full-page screenshot and logs results.
        """
        try:
            element = self.find_an_element(locator, elements, timeout)
            if element:
                self.driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)
                self.driver.execute_script("arguments[0].style.border='3px solid green'", element)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                self.driver.execute_script("arguments[0].style.backgroundColor = '';", element)
                self.driver.execute_script("arguments[0].style.border=''", element)
                self.logger.info(f"Hovered over {elements} with locator {locator}")
                Screenshot.capture_full_screenshot(self.driver, f"{elements}")
                return True
            else:
                Screenshot.capture_full_screenshot(self.driver, f"{elements}")
                raise Exception(f"{elements} not found")
        except Exception as e:
            self.logger.error(f"Error hovering over {elements} with locator {locator}: {e}")
            Screenshot.capture_full_screenshot(self.driver, f"{elements}")
            return False

    def replace_string_and_verify_url(self, text, url_text, timeout=10):

        '''
        Author Name: Anushka Verma
        Method Name: replace_string_and_verify_url
        Description: This method dynamically replaces a placeholder in an XPath string with the provided text,
                    clicks on the corresponding element, switches to the new window, verifies the URL,
                    and then closes the new window and returns to the original one.
        Return Type: None
        Parameter:
            text (string to replace in the XPath)
            url_text (expected substring in the new window's URL)
        '''
        try:
            locator_text = '//a[text()="text_to_be_replaced"]'.replace('text_to_be_replaced', text)
            locator = (By.XPATH, locator_text)
            self.click_on_element(locator, text)
            self.switch_to_new_window()
            self.verify_url(url_text)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as e:
            self.logger.error(f"Error replacing text for locator")

    def verify_url(self, expected_text):

        '''
        Author Name: Anushka Verma
        Method Name: verify_url
        Description: This method checks if the expected text is present in the current URL and logs the result.
        Return Type: None
        Parameter:
            expected_text (substring expected to be found in the current URL)
        '''
        try:
            url = self.driver.current_url
            assert expected_text in url
            self.logger.info(f"Assertion PASS: {expected_text} is found in the url")
        except AssertionError as ae:
            self.logger.info(f"Assertion FAIL: {ae}")
        except Exception as e:
            self.logger.error(f"Error verifying text in url presence: {e}")
