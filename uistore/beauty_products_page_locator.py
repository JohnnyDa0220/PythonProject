from selenium.webdriver.common.by import By
class BeautyPageLocator:
    brands_filter=(By.XPATH,'//div[text()="Brands"]')
    lakme_checkbox=(By.XPATH,'//label[text()="lakme"]')
    first_product_lakme=(By.XPATH,"//div[contains(@class,'CategoryCard_s')]/div[1]")
    add_to_cart=(By.XPATH,'//span[@class="Il Xl"]')
