import os
# from PIL import Image, ImageDraw
from datetime import datetime
from utilities.config_reader import get_properties


class Screenshot:
    # full screenshot
    @staticmethod
    def capture_full_screenshot(driver, filename):
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

