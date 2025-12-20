from selenium.webdriver.common.by import By

class SearchMedicineLocator:
    search_medicine_input=(By.XPATH,"//input[contains(@placeholder,'Search')]")
    view_all_results_button=(By.XPATH,"//a[@href='/search-medicines/Dolo']")
    search_input=(By.XPATH,"//input[@id='searchProduct']")
