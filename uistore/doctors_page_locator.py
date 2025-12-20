from selenium.webdriver.common.by import By

class DoctorsPageUI:
    find_doctors=(By.XPATH,"//a[text()='Find Doctors']")
    speacility=(By.CLASS_NAME,"icon-down-arrow")
    cardialogy=(By.XPATH,"//span[text()='Cardiology']")
    city=(By.XPATH,"//input[@placeholder='Search location']")
    submit_button=(By.XPATH,"//span[text()='Submit']")
    please_select_area=(By.CLASS_NAME,"QuickBook_errorMsg__U8Me2")
    health_records=(By.XPATH,"//a[text()='Health Records']")
    sign_inn=(By.XPATH,"//h3[text()='Sign In ']")
    track_monitor=(By.XPATH,"//div[text()='Track & Monitor']")
    login_button=(By.XPATH,"//span[text()='Login Now']")
    privacy_polocy=(By.XPATH,"//a[text()='Privacy Policy']")







