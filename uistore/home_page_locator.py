"""
Author Name: ROBIN MAHANTA
Module: home_page_locator.py
Purpose: UI element locators for the Apollo Pharmacy home page.
Description: Contains Selenium locators (XPath, CSS selectors, etc.) for all interactive
             elements on the home page, following the Page Object Model pattern.
"""

from selenium.webdriver.common.by import By

class HomePageLocator:
    """
    Author Name: ROBIN MAHANTA
    Class: HomePageLocator
    Purpose: Centralizes all home page element locators.
    Description: Contains XPath and other selectors for navigating and interacting
                 with elements on the Apollo Pharmacy home page.
    """
    
    search_bar_field = (By.XPATH, "//div[contains(@data-placeholder,'Search')]")
    # TestCase 5
    health_devices = (By.XPATH, "(//a[text()='Health Devices'])[2]")

    # TestCase 6
    book_lab_tests_at_home = (By.XPATH, "//h2[text()='Book Lab Tests at Home']")
    rt_pcr_test = (By.XPATH, "//a[text()='RT PCR Test At Home']")
    lab_tests = (By.XPATH, "//a[text()='Book Lab Tests at Home']")
    renal_profile_test = (By.XPATH, "//a[text()='Renal Profile (KFT, RFT Test)']")
    hemogram_test = (By.XPATH, "//a[text()='Hemogram Test']")
    lipid_profile_test = (By.XPATH, "//a[text()='Lipid Profile Test']")
    thyroid_profile_test = (By.XPATH, "//a[text()='Thyroid Profile Test (T3 T4 Tsh Test)']")
    d_dimer_test = (By.XPATH, "//a[text()='D Dimer Test']")
    urine_culture_test = (By.XPATH, "//a[text()='Urine Culture Test']")
    complete_blood_count_test = (By.XPATH, "//a[text()='Complete Blood Count (CBC Test)']")
    widal_test = (By.XPATH, "//a[text()='Widal Test']")
    liver_function_test = (By.XPATH, "//a[text()='Liver Function Test (LFT Test)']")
    search_bar = (By.XPATH, "(//div[@data-placeholder='Search Medicines'])[1]")
    apollo_products = (By.XPATH, "//a[@href='/shop-by-category/apollo-products']")
    honey = (By.XPATH, "(//span[text()='Honey'])")
    about_us = (By.XPATH, "//a[@href='https://www.apollopharmacy.in/about-us']")
    read = (By.XPATH, "//span[text()='Show more']")

    # TestCase 3
    services_in_footer = (By.XPATH, '//h2[text()="Services"]')
    consult_physicians = (By.XPATH, '//a[text()="Consult Physicians"]')
    consult_dermatologists = (By.XPATH, '//a[text()="Consult Dermatologists"]')
    consult_paediatricians = (By.XPATH, '//a[text()="Consult Paediatricians"]')
    consult_gynaecologists = (By.XPATH, '//a[text()="Consult Gynaecologists"]')
    consult_gastroenterologists = (By.XPATH, '//a[text()="Consult Gastroenterologists"]')
    consult_cardiologists = (By.XPATH, '//a[text()="Consult Cardiologists"]')
    consult_dietitians = (By.XPATH, '//a[text()="Consult Dietitians"]')
    consult_ENT_specialists = (By.XPATH, '//a[text()="Consult ENT Specialists"]')
    consult_geriatricians = (By.XPATH, '//a[text()="Consult Geriatricians"]')
    consult_diabetologists = (By.XPATH, '//a[text()="Consult Diabetologists"]')
    apollo_health_insurance = (By.XPATH, '//a[text()="Apollo Health Insurance"]')

    # TestCase 4
    personal_care = (By.XPATH, '(//a[text()="Personal Care"])[1]')
    hair_oils = (By.XPATH, '//span[text()="Hair Oils"]')

