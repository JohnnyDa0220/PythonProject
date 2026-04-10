"""
Author Name: ROBIN MAHANTA
Module: screenshot.py
Purpose: Provides screenshot capture utilities for test evidence and debugging.
Description: This module contains the Screenshot class which manages screenshot capture
             for full page views and specific elements during test execution.
"""

import os
# from PIL import Image, ImageDraw
from datetime import datetime
from utilities.config_reader import get_properties


class Screenshot:
    """
    Author Name: ROBIN MAHANTA
    Class: Screenshot
    Purpose: Manages screenshot capture for test debugging and evidence.
    Description: Provides static methods to capture full-page screenshots and element-specific screenshots
                 with timestamp-based file naming.
    """
    
    # full screenshot
    @staticmethod
    def capture_full_screenshot(driver, filename):
        """
        Author Name: ROBIN MAHANTA
        Method: capture_full_screenshot
        Purpose: Captures a full-page screenshot of the current browser window.
        Description: Saves a full-page screenshot with timestamp in the configured screenshot directory.
        Parameters:
            - driver (WebDriver): Selenium WebDriver instance
            - filename (str): Base filename for the screenshot (without extension)
        Return Type: None
        """
        folder = get_properties('PATH', 'screenshot_path')
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%H%M%S_%d-%m-%Y")
        screenshot_name = f"{timestamp}_{filename}.png"
        path = os.path.join(folder, screenshot_name)
        driver.save_screenshot(path)

    @staticmethod
    def capture_screenshot_of_particular_element(element, filename):
        folder = get_properties('PATH', 'screenshot_path')
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%H%M%S_%d-%m-%Y")
        screenshot_name = f"{timestamp}_{filename}_{element}.png"
        path = os.path.join(folder, screenshot_name)
        element.screenshot(path)

