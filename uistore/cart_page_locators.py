"""
Author Name: ROBIN MAHANTA
Module: cart_page_locators.py
Purpose: UI element locators for the Apollo Pharmacy cart page.
Description: Contains Selenium locators (XPath, CSS selectors, etc.) for all interactive
             elements on the shopping cart page.
"""

from selenium.webdriver.common.by import By

class CartPageLocators:
    """
    Author Name: ROBIN MAHANTA
    Class: CartPageLocators
    Purpose: Centralizes all cart page element locators.
    Description: Contains XPath and other selectors for cart operations,
                 checkout, and payment interactions.
    """
    
    my_cart_text=(By.XPATH,"//span[text()='1 item in your cart']")
    proceed=(By.XPATH,"//button[@title='Proceed']")
    mobile_number_input=(By.XPATH,"//input[@name='mobileNumber']")
    login=(By.XPATH,"//button[@title='Login']")
    resend_otp=(By.XPATH,"//p[contains(text(),'Resend OTP')]")
