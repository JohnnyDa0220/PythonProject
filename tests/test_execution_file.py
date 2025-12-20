# tests/test_execution_file.py
import pytest
from utilities.config_reader import get_properties
from utilities.logger import Log
from pages.homepage import HomePage

# from pages.baby_body_wash_page import BabyBodyWash
# from pages.baby_contact_us_page import BabyContactUs
# from pages.baby_diaper_page import BabyDiaper
# from pages.baby_product_page import BabyProduct
# from pages.honey_results_page import HoneyPage
# from pages.tablet_product_page import TabletProductPage
# from pages.crocin_result_page import CrocinResultPage
# from pages.first_product_page import FirstProductPage
# from pages.home_page import HomePage
# from pages.doctors_page import DoctorPage
# from pages.product_page import ProductPage
# from pages.cart_page import CartPage
# from pages.search_medicine_page import SearchMedicinePage
# from pages.dolo_search_result_page import DoloSearchPage
# from pages.medicine_cart_page import MedicineCartPage
# from pages.baby_care_page import BabyCare
# from pages.health_devices_page import HealthDevicesPage
# from pages.ayurveda_page import AyurvedaPage
# from pages.hair_oil_page import HairOilPage
# from pages.first_product_hair_oil_page import FirstHairOilPage
# from pages.toothpaste_page import ToothpastePage
# from pages.first_product_toothpaste_page import FirstToothpastePage
# from pages.beauty_products_page import BeautyPage

class Test_Page:
    logger = Log.capture_logger()

    @pytest.mark.smoke
    def test_method_add_crocin_to_cart(self, driver):
        """
        Author Name: Robin Mahanta
        Method Name: test_method_add_crocin_to_cart
        Description: Verifies the flow of searching for a medicine, selecting it, adding to cart, and performing cart operations.
        """
        url = get_properties("URL", "website_url")
        driver.get(url)
        driver.maximize_window()

        home = HomePage(driver, Test_Page.logger)
        home.click_on_search_bar()
        # search = SearchMedicinePage(self.driver, Test_Page.logger)
        # search.click_and_enter_medicine_name_and_press_enter(
        #     read_excel(get_properties("PATH", "excel_path"), "Sagnick", 2, 1)
        # )
        # crocin = CrocinResultPage(self.driver, Test_Page.logger)
        # crocin.click_on_first_item()
        # first = FirstProductPage(self.driver, Test_Page.logger)
        # first.add_crocin()
        # cart = CartPage(self.driver, Test_Page.logger)
        # cart.cart_page_operation()

    # @pytest.mark.smoke
    # def test_method_add_honey_to_cart_and_click_on_about_us(self):
    #     """
#         Author Name: Robin Mahanta
    #     Method Name: test_method_add_honey_to_cart_and_click_on_about_us
    #     Description: Verifies the honey product flow and About Us navigation from the home page.
    #     Return Type: None
    #     Parameters: None
    #     """
    #     home = HomePage(self.driver, Test_Page.logger)
    #     home.honey_operations()
    #     honey = HoneyPage(self.driver, Test_Page.logger)
    #     honey.honey_page_operation()
    #     home.click_on_about_us()

    # @pytest.mark.smoke
    # def test_verify_links_in_services_from_footer(self):
    #     '''
#         Author Name: Robin Mahanta
    #     Method Name: test_verify_links_in_services_from_footer
    #     Description: This test verifies that all links under the Services section in the footer are working correctly.
    #     Return Type: None
    #     Parameter: None
    #     '''
    #     home=HomePage(self.driver,Test_Page.logger)
    #     home.verify_links_in_services_from_footer()

    # @pytest.mark.smoke
    # def test_personal_care_products(self):
    #     '''
#         Author Name: Robin Mahanta
    #     Method Name: test_personal_care_products
    #     Description: This test navigates through multiple personal care product categories and verifies product access.
    #     Return Type: None
    #     Parameter: None
    #     '''
    #     home=HomePage(self.driver,Test_Page.logger)
    #     home.click_hair_oil_under_personal_care()
    #     hair_oil=HairOilPage(self.driver,Test_Page.logger)
    #     hair_oil.clicking_on_first_product_in_hair_oil()
    #     first_prod=FirstHairOilPage(self.driver,Test_Page.logger)
    #     first_prod.click_toothpaste_under_personal_care()
    #     toothpaste=ToothpastePage(self.driver,Test_Page.logger)
    #     toothpaste.clicking_on_first_product_in_toothpaste()
    #     first_prod_toothpaste=FirstToothpastePage(self.driver,Test_Page.logger)
    #     first_prod_toothpaste.click_beauty_under_personal_care()
    #     beauty=BeautyPage(self.driver,Test_Page.logger)
    #     beauty.click_first_product_in_lakme_and_verify_cart()

    # @pytest.mark.smoke
    # def test_ayurveda_and_health_devices(self):
    #     """
#         Author Name: Robin Mahanta
    #     Method Name: test_method_test_case_5
    #     Description: Verifies Health Devices and Ayurveda page functionalities by navigating through respective flows.
    #     Return Type: None
    #     Parameters: None
    #     """
    #     fifth1 = HomePage(self.driver, Test_Page.logger)
    #     fifth1.click_health_devices()
    #     fifth2 = HealthDevicesPage(self.driver, Test_Page.logger)
    #     fifth2.health_devices_all_functions()
    #     fifth3 = AyurvedaPage(self.driver, Test_Page.logger)
    #     fifth3.ayurveda_all_functions()

    # @pytest.mark.smoke
    # def test_verify_urls_of_book_lab_tests_at_home(self):
    #     """
#         Author Name: Robin Mahanta
    #     Method Name: test_method_test_case_6
    #     Description: Verifies all URLs related to 'Book Lab Tests at Home' from the homepage.
    #     Return Type: None
    #     Parameters: None
    #     """
    #     sixth = HomePage(self.driver, Test_Page.logger)
    #     sixth.verify_urls_of_book_lab_tests_at_home()

    # @pytest.mark.smoke
    # def test_search_and_add_medicine_to_cart(self):
    #     """
#         Author Name: Robin Mahanta
    #     Method Name: test_method_test_case_7
    #     Description: Executes a complete test flow that includes searching for a medicine, applying filters,
    #                 selecting a product, and performing cart interactions.
    #     Return Type: None
    #     Parameters: None
    #     """
    #     home=HomePage(self.driver,Test_Page.logger)
    #     home.click_on_search_bar()
    #     home1=SearchMedicinePage(self.driver,Test_Page.logger)
    #     home1.search_and_open_medicine_results(read_excel(get_properties("PATH","excel_path"),"Debjani",1,2))
    #     home2=DoloSearchPage(self.driver,Test_Page.logger)
    #     home2.perform_dolo_search_actions()
    #     home3=TabletProductPage(self.driver,Test_Page.logger)
    #     home3.perform_cart_actions()
    #     home4=MedicineCartPage(self.driver,Test_Page.logger)
    #     home4.perform_cart_interactions()

    # @pytest.mark.smoke
    # def test_women_care_and_minerals(self):
    #     doctor=DoctorPage(self.driver,Test_Page.logger)
    #     doctor.operation_one()

    # @pytest.mark.smoke
    # def test_find_doctors_in_chennai(self):
    #     products=ProductPage(self.driver,Test_Page.logger)
    #     products.opeartion_two()

    # @pytest.mark.smoke
    # def test_baby_care_products(self):
    #     """
    #     Author: Robin Mahanta
    #     Method Name: test_method_test_case_10
    #     Description:   Runs a basic test to check if all major Baby Care sections—like diapers, body wash, products, and contact—are working correctly.
    #     Returns:None
    #     Parameters: self:Instance of the test class containing WebDriver and logger setup.
    #     """
    #     baby = BabyCare(self.driver, Test_Page.logger)
    #     diaper = BabyDiaper(self.driver, Test_Page.logger)
    #     body = BabyBodyWash(self.driver, Test_Page.logger)
    #     product = BabyProduct(self.driver, Test_Page.logger)
    #     contact = BabyContactUs(self.driver, Test_Page.logger)
    #
    #     baby.babycare_test_execution()
    #     diaper.baby_diaper_execution()
    #     body.baby_body_wash_execution()
    #     product.baby_product_execution()
    #     contact.baby_contact_us_execution()