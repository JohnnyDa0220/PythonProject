from utilities.web_driver_helper import WebDriverHelper
from uistore.home_page_locator import HomePageLocator
from time import sleep

class HomePage:
    def __init__(self, driver, logger):
        """
        Author Name: ROBIN MAHANTA
        Method Name: __init__
        Description: Initializes the HomePage with WebDriver and Logger instances, and sets up WebDriverHelper.
        Return Type: None
        Parameters: driver, logger
        """
        self.driver = driver
        self.logger = logger
        self.helper = WebDriverHelper(self.driver, self.logger)

    def click_on_search_bar(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_on_search_bar
        Description: Clicks on the search bar field on the home page using the WebDriverHelper.
        Return Type: None
        Parameters: None
"""
        self.helper.click_on_element(HomePageLocator.search_bar_field, "Search Bar")

    def hover_on_apollo(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: hover_on_apollo
        Description: Hovers over the Apollo products section on the home page.
        Return Type: None
        Parameters: None
        """
        self.helper.hover_on_single_element(HomePageLocator.apollo_products, "Apollo_Products")

    def click_on_honey(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_on_honey
        Description: Clicks on the Honey product category from the Apollo section.
        Return Type: None
        Parameters: None
        """
        self.helper.click_on_element(HomePageLocator.honey, "Honey")

    def honey_operations(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: honey_operations
        Description: Performs the complete flow to access the Honey product section by hovering and clicking.
        Return Type: None
        Parameters: None
        """
        self.hover_on_apollo()
        self.click_on_honey()

    def click_on_about_us(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_on_about_us
        Description: Scrolls to and clicks on the 'About Us' section, then switches to the new window.
        Return Type: None
        Parameters: None
        """
        self.helper.scroll_to_element(HomePageLocator.read, "About_Us")
        self.helper.click_on_element(HomePageLocator.about_us, "About_Us")
        self.helper.switch_to_new_window()

    def verify_text_services_in_footer(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_text_services_in_footer
        Description: This method scrolls to the Services section in the footer and verifies its presence.
        Return Type: None
        Parameter: None
        '''
        self.helper.scroll_to_element(HomePageLocator.services_in_footer, "Services")
        self.logger.info("scroll down")
        self.helper.verify_text_presence(HomePageLocator.services_in_footer, "Services")

    def verify_consult_physicians_link(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_physicians_link
        Description: This method verifies the Consult Physicians link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult Physicians", "general-physician-internal-medicine")

    def verify_consult_dermatologists_link(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_dermatologists_link
        Description: This method verifies the Consult Dermatologists link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult Dermatologists", "dermatology")

    def verify_consult_paediatricians_link(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_paediatricians_link
        Description: This method verifies the Consult Paediatricians link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult Paediatricians", "paediatrics")

    def verify_consult_gynaecologists_link(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_gynaecologists_link
        Description: This method verifies the Consult Gynaecologists link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult Gynaecologists", "obstetrics-and-gynaecology")

    def verify_consult_gastroenterologists_link(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_gastroenterologists_link
        Description: This method verifies the Consult Gastroenterologists link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult Gastroenterologists", "gastroenterology-gi-medicine")

    def verify_consult_cardiologists_link(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_cardiologists_link
        Description: This method verifies the Consult Cardiologists link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult Cardiologists", "cardiology")

    def verify_consult_dietitians_link(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_dietitians_link
        Description: This method verifies the Consult Dietitians link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult Dietitians", "dietetics")

    def verify_consult_ENT_specialists(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_ENT_specialists
        Description: This method verifies the Consult ENT Specialists link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult ENT Specialists", "ent")

    def verify_consult_geriatricians(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_geriatricians
        Description: This method verifies the Consult Geriatricians link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult Geriatricians", "elderly-care-and-concerns")

    def verify_consult_diabetologists(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_consult_diabetologists
        Description: This method verifies the Consult Diabetologists link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Consult Diabetologists", "diabetology")

    def verify_apollo_health_insurance_link(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_apollo_health_insurance_link
        Description: This method verifies the Apollo Health Insurance link under Services.
        Return Type: None
        Parameter: None
        '''
        self.helper.replace_string_and_verify_url("Apollo Health Insurance", "https://www.apollo247.com/insurance")

    def verify_links_in_services_from_footer(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: verify_links_in_services_from_footer
        Description: This method verifies all the links listed under the Services section in the footer.
        Return Type: None
        Parameter: None
        '''
        self.verify_text_services_in_footer()
        self.verify_consult_physicians_link()
        self.verify_consult_dermatologists_link()
        self.verify_consult_paediatricians_link()
        self.verify_consult_gynaecologists_link()
        self.verify_consult_gastroenterologists_link()
        self.verify_consult_cardiologists_link()
        self.verify_consult_dietitians_link()
        self.verify_consult_ENT_specialists()
        self.verify_consult_geriatricians()
        self.verify_consult_diabetologists()
        self.verify_apollo_health_insurance_link()

    def click_hair_oil_under_personal_care(self):
        '''
        Author Name: ROBIN MAHANTA
        Method Name: click_hair_oil_under_personal_care
        Description: This method hovers over the Personal Care section and clicks on the Hair Oils option.
        Return Type: None
        Parameter: None
        '''
        self.helper.hover_on_single_element(HomePageLocator.personal_care, "Personal Care")
        self.helper.click_on_element(HomePageLocator.hair_oils, "Hair Oils")

    def verify_text_book_lab_tests_at_home(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_text_book_lab_tests_at_home
        Description: Verifies the presence of the 'Book Lab Tests at Home' text on the homepage.
        Return Type: None
        Parameters: None
        """
        self.helper.scroll_to_element(HomePageLocator.book_lab_tests_at_home, "Services")
        self.helper.verify_text_presence(HomePageLocator.book_lab_tests_at_home, "Book Lab Tests at Home")
        self.logger.info("Book lab tests at home verified")

    def verify_rt_pcr_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_rt_pcr_url
        Description: Verifies the URL for the RT PCR Test At Home.
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("RT PCR Test At Home",
                                                  "https://www.apollo247.com/lab-tests/covid-19-rt-pcr-with-home-collection")
        self.logger.info("verified RT PCR url")

    def verify_book_lab_tests_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_book_lab_tests_url
        Description: Verifies the URL for the Book Lab Tests at Home service.
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("Book Lab Tests at Home", "https://www.apollo247.com/lab-tests")
        self.logger.info("verified book lab tests url")

    def verify_rental_profile_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_rental_profile_url
        Description: Verifies the URL for the Renal Profile (KFT, RFT Test).
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("Renal Profile (KFT, RFT Test)",
                                                  "https://www.apollo247.com/lab-tests/renal-profile-kidney-function-test-rft-kft")
        self.logger.info("verified rental profile url")

    def verify_hemogram_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_hemogram_url
        Description: Verifies the URL for the Hemogram Test.
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("Hemogram Test", "https://www.apollo247.com/lab-tests/hemogram")
        self.logger.info("verified hemogram url")

    def verify_lipid_profile_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_lipid_profile_url
        Description: Verifies the URL for the Lipid Profile Test.
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("Lipid Profile Test",
                                                  "https://www.apollo247.com/lab-tests/lipid-profile")
        self.logger.info("verified lipid profile url")

    def verify_thyroid_profile_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_thyroid_profile_url
        Description: Verifies the URL for the Thyroid Profile Test (T3 T4 Tsh Test).
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("Thyroid Profile Test (T3 T4 Tsh Test)",
                                                  "https://www.apollo247.com/lab-tests/free-and-total-thyroid-profile-t3-t4-ft3-ft4-tsh")
        self.logger.info("verified thyroid profile url")

    def verify_d_dimer_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_d_dimer_url
        Description: Verifies the URL for the D Dimer Test.
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("D Dimer Test", "https://www.apollo247.com/lab-tests/d-dimer")
        self.logger.info("verified d dimer url")

    def verify_urine_culture_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_urine_culture_url
        Description: Verifies the URL for the Urine Culture Test.
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("Urine Culture Test",
                                                  "https://www.apollo247.com/lab-tests/culture-and-sensitivity-urine-automated")
        self.logger.info("verified urine culture url")

    def verify_complete_blood_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_complete_blood_url
        Description: Verifies the URL for the Complete Blood Count (CBC Test).
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("Complete Blood Count (CBC Test)",
                                                  "https://www.apollo247.com/lab-tests/complete-blood-count-cbc")
        self.logger.info("verified complete blood url")

    def verify_widal_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_widal_url
        Description: Verifies the URL for the Widal Test.
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("Widal Test",
                                                  "https://www.apollo247.com/lab-tests/widal-test-slide-method")
        self.logger.info("verified widal url")

    def verify_liver_function_url(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_liver_function_url
        Description: Verifies the URL for the Liver Function Test (LFT Test).
        Return Type: None
        Parameters: None
        """
        self.helper.replace_string_and_verify_url("Liver Function Test (LFT Test)",
                                                  "https://www.apollo247.com/lab-tests/liver-function-test-lft-with-ggt")
        self.logger.info("verified liver function url")

    def verify_urls_of_book_lab_tests_at_home(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: verify_urls_of_book_lab_tests_at_home
        Description: Executes all verification methods for URLs and text related to 'Book Lab Tests at Home'.
        Return Type: None
        Parameters: None
        """
        self.verify_text_book_lab_tests_at_home()
        self.verify_rt_pcr_url()
        self.verify_book_lab_tests_url()
        self.verify_rental_profile_url()
        self.verify_hemogram_url()
        self.verify_lipid_profile_url()
        self.verify_thyroid_profile_url()
        self.verify_d_dimer_url()
        self.verify_urine_culture_url()
        self.verify_complete_blood_url()
        self.verify_widal_url()
        self.verify_liver_function_url()

    def click_health_devices(self):
        """
        Author Name: ROBIN MAHANTA
        Method Name: click_health_devices
        Description: Scrolls to the 'health_devices' section and clicks on the corresponding element.
        Return Type: None
        Parameters: None
        """
        self.helper.scroll_to_element(HomePageLocator.read, "health_devices")
        sleep(5)
        self.helper.click_on_element(HomePageLocator.health_devices, "healthdevices")
