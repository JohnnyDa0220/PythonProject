from utilities.web_driver_helper import WebDriverHelper
from uistore.crocin_results_page_locator import CrocinResultsPageLocator

class CrocinResultPage:
    def __init__(self, driver, logger):
        """
        Author Name: Sagnick Routh
        Method Name: __init__
        Description: Initializes the CrocinResultPage with WebDriver and Logger instances, and sets up WebDriverHelper.
        Return Type: None
        Parameters: driver, logger
        """
        self.logger = logger
        self.driver = driver
        self.helper = WebDriverHelper(self.driver, self.logger)

    def click_on_first_item(self):
        """
        Author Name: Sagnick Routh
        Method Name: click_on_first_item
        Description: Clicks on the first Crocin product listed in the search results.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(CrocinResultsPageLocator.crocin_first_product, "First_Crocin_Product")