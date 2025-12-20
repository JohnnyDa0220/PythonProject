from selenium.webdriver.common.by import By

class FirstProductPageLocator:
    consume_type=(By.XPATH,"//h3[text()='Consume Type']")
    join_circle=(By.XPATH,"//span[text()='Join Circle']")
    twelve_months=(By.XPATH,"//label[@for='Circle_Anually']")
    close_icon=(By.XPATH,"//span[@aria-label='close button']")
    strip_select=(By.XPATH,"//span[text()='1 Strip']")
    two_strips=(By.XPATH,"//p[text()='2 Strips']")
    view_cart=(By.XPATH,"//span[text()='View Cart']")

