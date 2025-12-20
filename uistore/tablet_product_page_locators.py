from selenium.webdriver.common.by import By

class TabletProductPageLocator:
   add_to_cart_button=(By.XPATH,"//span[text()='Add to Cart']")
   cart_icon_link=(By.XPATH,"//a[contains(@href,'/medicines')]")
   