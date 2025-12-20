from selenium.webdriver.common.by import By

class DoloSearchResultPageLoactor:

    search_result_heading=(By.XPATH,"//h3[contains(text(), '200')]")
    in_stock_filter_button=(By.XPATH,"//div[text()='In-stock']")
    ten_percent_off_filter=(By.XPATH,"//label[text()='10% Off or more']")
    dolo_first_product=(By.XPATH,"(//div[contains(@class,'v_')])[1]")
    