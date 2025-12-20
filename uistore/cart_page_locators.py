from selenium.webdriver.common.by import By

class CartPageLocators:
    my_cart_text=(By.XPATH,"//span[text()='1 item in your cart']")
    proceed=(By.XPATH,"//button[@title='Proceed']")
    mobile_number_input=(By.XPATH,"//input[@name='mobileNumber']")
    login=(By.XPATH,"//button[@title='Login']")
    resend_otp=(By.XPATH,"//p[contains(text(),'Resend OTP')]")
