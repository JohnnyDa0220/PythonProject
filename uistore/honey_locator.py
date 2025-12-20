from selenium.webdriver.common.by import By

class HoneyLocator:
    honey=(By.XPATH,"//h1[text()='Honey']")
    brand=(By.XPATH,"//div[text()='Brands']")
    apollo_honey=(By.XPATH,"(//input[@type='checkbox'])[9]")
    sort=(By.XPATH,"//button[contains(@class,'P')]")
    hightolow=(By.XPATH,"(//input[@type='radio'])[3]")
    add=(By.XPATH,"(//span[text()='Add'])[1]")
    view_cart=(By.XPATH,"//span[text()='View Cart']")
