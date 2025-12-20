from selenium.webdriver.common.by import By

class HealthDevicesPageLocator:
    total_items=(By.XPATH,"//h1[text()='Health Devices']")
    category=(By.XPATH,"//div[text()='Category']")
    bp_monitors=(By.XPATH,"//label[text()='bp monitors']")
    first_product_health_devices=(By.XPATH,"(//div[@class='B_'])[1]")
    ayurveda=(By.XPATH,"(//a[text()='Ayurveda'])[1]")
    cold_and_cough=(By.XPATH,"//span[text()='Cold & Cough']")

    
