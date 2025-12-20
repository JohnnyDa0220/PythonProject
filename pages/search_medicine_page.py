from utilities.web_driver_helper import WebDriverHelper
from uistore.search_medicines_page_locator import SearchMedicineLocator
from utilities.excel_reader import read_excel
from utilities.config_reader import get_properties
from utilities.screenshot import Screenshot
from time import sleep
class SearchMedicinePage:
    """
Author Name: Debjani Kundu
Class Name: SearchMedicinePage
Description: This class contains methods to interact with the search medicine functionality of the application.
             It uses WebDriverHelper for element interactions and provides methods to search for medicines,
             enter medicine names, and view search results.
Constructor Parameters:
    - driver (WebDriver): Selenium WebDriver instance used to interact with the browser.
    - logger (Logger): Logger instance used for logging actions and events.
"""

    def __init__(self,driver,logger):
        self.driver=driver
        self.logger=logger
        self.helper=WebDriverHelper(self.driver,self.logger)

    def click_and_enter_medicine_name(self,medicine_name):
        """
    Author Name: Debjani Kundu
    Method Name: click_and_enter_medicine_name
    Description: Clicks on the search input field and enters the provided medicine name.
    Return Type: None
    Parameters:
        - medicine_name (str): Name of the medicine to be searched.
    """
        self.helper.click_on_element(SearchMedicineLocator.search_medicine_input,"search_medicine_input")
        self.helper.send_keys_to_element(SearchMedicineLocator.search_medicine_input,"search_medicine_input",medicine_name)
        sleep(5)
       
    def click_and_enter_medicine_name_and_press_enter(self, medicine_name):
        """
        Author Name: Sagnick Routh
        Method Name: click_and_enter_medicine_name_and_press_enter
        Description: Clicks on the medicine search input field, enters the provided medicine name, and presses Enter.
        Return Type: None
        Parameters: medicine_name (str)
        """
        self.helper.click_on_element(SearchMedicineLocator.search_medicine_input, "search_medicine_input")
        self.helper.input_text_then_enter(SearchMedicineLocator.search_medicine_input, medicine_name, "search_medicine_input")


    def click_view_all_results_button(self):
        
        """
    Author Name: Debjani Kundu
    Method Name: click_view_all_results_button
    Description: Clicks on the 'View All Results' button to display all search results.
    Return Type: None
    Parameters: None
    """
        # element=self.driver.find_element(*SearchMedicineLocator.view_all_results_button)
        # Screenshot.capture_screenshot_of_particular_element(element,'view all result')
        self.helper.click_on_element(SearchMedicineLocator.view_all_results_button,"view_all_results_button")
        sleep(5)
   
    def search_and_open_medicine_results(self,medicine_name):
        
        """
    Author Name: Debjani Kundu
    Method Name: search_and_open_medicine_results
    Description: Searches for a medicine and opens the full list of results.
    Return Type: None
    Parameters:
        - medicine_name (str): Name of the medicine to be searched.
    """
        self.click_and_enter_medicine_name(medicine_name)
        self.click_view_all_results_button()