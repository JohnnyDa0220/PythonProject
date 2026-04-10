"""
Author Name: ROBIN MAHANTA
Module: eventhandler.py
Purpose: Provides event listener for Selenium WebDriver automation.
Description: This module contains the EventHandler class which implements AbstractEventListener
             to log WebDriver events for debugging and traceability.
"""

import os
import logging

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

class EventHandler(AbstractEventListener):
    """
    Author Name: ROBIN MAHANTA
    Class: EventHandler
    Purpose: Listens to Selenium WebDriver events for logging and debugging.
    Description: Implements AbstractEventListener to intercept navigation and other WebDriver events
                 and log them for test execution traceability.
    """
    
    def before_navigate_to(self, url, driver):
        """
        Author Name: ROBIN MAHANTA
        Method: before_navigate_to
        Purpose: Logs when navigation is about to occur.
        Description: Called before the browser navigates to a URL.
        Parameters:
            - url (str): The URL being navigated to
            - driver (WebDriver): Selenium WebDriver instance
        Return Type: None
        """
        print("Before navigating to:", url)
    
    def after_navigate_to(self, url, driver):
        """
        Author Name: ROBIN MAHANTA
        Method: after_navigate_to
        Purpose: Logs when navigation has completed.
        Description: Called after the browser successfully navigates to a URL.
        Parameters:
            - url (str): The URL that was navigated to
            - driver (WebDriver): Selenium WebDriver instance
        Return Type: None
        """
        print("After navigating to:", url)