"""
Author Name: ROBIN MAHANTA
Module: first_product_page_locator.py
Purpose: UI element locators for the Apollo Pharmacy product detail page.
Description: Contains Selenium locators (XPath, CSS selectors, etc.) for all interactive
             elements on the product details page.
"""

from selenium.webdriver.common.by import By

class FirstProductPageLocator:
    """
    Author Name: ROBIN MAHANTA
    Class: FirstProductPageLocator
    Purpose: Centralizes all product detail page element locators.
    Description: Contains XPath and other selectors for product interactions,
                 subscription options, and add-to-cart operations.
    """
    
    consume_type=(By.XPATH,"//h3[text()='Consume Type']")
    join_circle=(By.XPATH,"//span[text()='Join Circle']")
    twelve_months=(By.XPATH,"//label[@for='Circle_Anually']")
    close_icon=(By.XPATH,"//span[@aria-label='close button']")
    strip_select=(By.XPATH,"//span[text()='1 Strip']")
    two_strips=(By.XPATH,"//p[text()='2 Strips']")
    view_cart=(By.XPATH,"//span[text()='View Cart']")

