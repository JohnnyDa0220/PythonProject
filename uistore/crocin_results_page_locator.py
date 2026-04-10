"""
Author Name: ROBIN MAHANTA
Module: crocin_results_page_locator.py
Purpose: UI element locators for the Apollo Pharmacy search results page.
Description: Contains Selenium locators (XPath, CSS selectors, etc.) for all interactive
             elements on the medicine search results page.
"""

from selenium.webdriver.common.by import By

class CrocinResultsPageLocator:
    """
    Author Name: ROBIN MAHANTA
    Class: CrocinResultsPageLocator
    Purpose: Centralizes all search results page element locators.
    Description: Contains XPath and other selectors for interacting with
                 medicine search results and product selection.
    """
    
    crocin_first_product=(By.XPATH,"(//div[contains(@class,'ProductCard_pr')])[1]")
    