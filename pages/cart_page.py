from uistore.cart_page_locators import CartPageLocators
from time import sleep
from utilities.web_driver_helper import WebDriverHelper
from utilities.excel_reader import read_excel
from utilities.config_reader import get_properties

class CartPage:
    def __init__(self, driver, logger):
        """
        Author Name: ROBIN MAHANTA
        Method Name: __init__
        Description: Initializes the CartPage object with WebDriver and Logger instances, and sets up WebDriverHelper.
        Return Type: None
        Parameters: driver, logger
        """
        self.logger = logger
        self.driver = driver
        self.helper = WebDriverHelper(self.driver, self.logger)

    def my_cart_is_present(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: my_cart_is_present
        Description: Verifies that the 'Your Cart' text is present on the cart page.
        Return Type: None
        Parameters: None
        """
        self.helper.verify_text_presence(CartPageLocators.my_cart_text, "your cart")

    def click_on_proceed(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_on_proceed
        Description: Clicks on the 'Proceed' button on the cart page.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(CartPageLocators.proceed, "Proceed")

    def enter_on_mobile_number(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: enter_on_mobile_number
        Description: Enters the mobile number into the input field using data from Excel.
        Return Type: None
        Parameters: None
        """
        self.helper.send_keys_to_element(
            CartPageLocators.mobile_number_input,
            "Mobile_Number_Input_Field",
            read_excel(get_properties("PATH", "excel_path"), "Sagnick", 2, 2)
        )

    def click_on_login_icon(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_on_login_icon
        Description: Clicks on the login icon/button after entering the mobile number.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(CartPageLocators.login, "Login")

    def verify_resend_otp_is_present(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_resend_otp_is_present
        Description: Verifies that the 'RESEND OTP' text is present after login attempt.
        Return Type: None
        Parameters: None
        """
        self.helper.verify_text_presence(CartPageLocators.resend_otp, "RESEND OTP")

    def cart_page_operation(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: cart_page_operation
        Description: Executes the full cart page flow including verifying cart, proceeding, entering mobile number, logging in, and verifying OTP.
        Return Type: None
        Parameters: None
        """
        self.my_cart_is_present()
        self.click_on_proceed()
        self.enter_on_mobile_number()
        self.click_on_login_icon()
        self.verify_resend_otp_is_present()