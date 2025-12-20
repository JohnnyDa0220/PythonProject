from selenium.webdriver.common.by import By
class ToothpastePageLocator:
    verify_toothpaste=(By.XPATH,'//h1[text()="Toothpaste"]')
    first_product_toothpaste=(By.XPATH,"//div[contains(@class,'CategoryCard_s')]/div[1]")
