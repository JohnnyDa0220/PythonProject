from selenium.webdriver.common.by import By
class HairOilPageLocator:
    verify_hair_oil_result=(By.XPATH,'//h1[text()="Hair Oils"]')
    first_product_hairoil=(By.XPATH,"//div[contains(@class,'CategoryCard_s')]/div[1]")
