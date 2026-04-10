from utilities.web_driver_helper import WebDriverHelper
from uistore.first_product_page_locator import FirstProductPageLocator
from time import sleep

class FirstProductPage:
    def __init__(self, driver, logger):
        """
        Author Name: ROBIN MAHANTA
        Method Name: __init__
        Description: Initializes the FirstProductPage with WebDriver and Logger instances, and sets up WebDriverHelper.
        Return Type: None
        Parameters: driver, logger
        """
        self.logger = logger
        self.driver = driver
        self.helper = WebDriverHelper(self.driver, self.logger)

    def verify_text_Consume_Type(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_text_Consume_Type
        Description: Verifies that the 'Consume Type' text is present on the product page.
        Return Type: None
        Parameters: None
        """
        self.helper.verify_text_presence(FirstProductPageLocator.consume_type, "Consume Type")

    def click_on_join_circle(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_on_join_circle
        Description: Clicks on the 'Join Circle' button on the product page.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(FirstProductPageLocator.join_circle, "Join_Circle")

    def click_on_twelve_month(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_on_twelve_month
        Description: Selects the 12-month subscription option.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(FirstProductPageLocator.twelve_months, "For_12_months")

    def close_join_circle_popup(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: close_join_circle_popup
        Description: Closes the 'Join Circle' popup window.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(FirstProductPageLocator.close_icon, "Close_icon")

    def click_on_number_of_strips(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_on_number_of_strips
        Description: Opens the dropdown to select the number of strips.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(FirstProductPageLocator.strip_select, "Strip_DropDown")

    def click_on_two(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_on_two
        Description: Selects the option for two strips from the dropdown.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(FirstProductPageLocator.two_strips, "Two_Strips")

    def click_view_cart(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_view_cart
        Description: Clicks on the 'View Cart' button to proceed to the cart.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(FirstProductPageLocator.view_cart, "View_Cart")

    def add_crocin(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: add_crocin
        Description: Executes the full flow to add Crocin to the cart including subscription selection and quantity.
        Return Type: None
        Parameters: None
        """
        self.verify_text_Consume_Type()
        self.click_on_join_circle()
        self.click_on_twelve_month()
        self.close_join_circle_popup()
        sleep(2)
        self.click_on_number_of_strips()
        sleep(2)
        self.click_on_two()
        sleep(2)
        self.click_view_cart()
