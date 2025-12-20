
from selenium.webdriver.common.by import By

class MedicineCartPageLocator:
    add_address_button=(By.XPATH,"//span[text()='ADD ADDRESS']")
    close_modal_icon=(By.XPATH,"//span[contains(@class,'moda')]")
    add_items_button=(By.XPATH,"//span[text()='Add Items']")
    search_product_input=(By.ID,"searchProduct")
    first_volini_product_card =(By.XPATH,"(//div[contains(@class,'r_ ')])[1]")
