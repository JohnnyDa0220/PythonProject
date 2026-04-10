"""
Author Name: ROBIN MAHANTA
Module: search_medicines_page_locator.py
Purpose: UI element locators for the Apollo Pharmacy medicine search page.
Description: Contains Selenium locators (XPath, CSS selectors, etc.) for all interactive
             elements on the medicine search page.
"""

from selenium.webdriver.common.by import By

class SearchMedicineLocator:
    """
    Author Name: ROBIN MAHANTA
    Class: SearchMedicineLocator
    Purpose: Centralizes all medicine search page element locators.
    Description: Contains XPath and other selectors for searching medicines
                 and viewing search results.
    """
    
    search_medicine_input=(By.XPATH,"//input[contains(@placeholder,'Search')]")
    view_all_results_button=(By.XPATH,"//a[@href='/search-medicines/Dolo']")
    search_input=(By.XPATH,"//input[@id='searchProduct']")
