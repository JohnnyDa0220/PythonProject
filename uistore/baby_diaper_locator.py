from selenium.webdriver.common.by import By

class BabyDiaperLocator:
    baby_care=(By.XPATH,"//a[@href='/shop-by-category/baby-care']")
    diapers=(By.XPATH,"//a[@href='/shop-by-category/diapers']")
    diaper_label=(By.XPATH,"//p[text()='Diapers']")
    body_wash=(By.XPATH,"//a[@href='/shop-by-category/body-wash']")
    body_wash_label=(By.XPATH,"//p[text()='Body Wash']")
    total_items=(By.XPATH,"//div[@class='PaginatedCategoryListing_cpHeader__pp_t2']")
    sort=(By.XPATH,"//i[@class='ProductSortWeb_arrow__smwA7 ']")
    high_to_low=(By.XPATH,"(//div[@class='ProductSortWeb_listRoot__r04MX'])[3]")
    first_product=(By.XPATH,"(//div[@class='ProductCard_productCardGrid__NHfRH   '])[1]")
    # footer=(By.XPATH,"//div[text()='Product-Type']")
    footer=(By.XPATH,"(//div[@class='revampedContainer'])[2]")
    contact=(By.XPATH, "(//a[@rel='noopener noreferrer'])[5]")
    contact_us_label=(By.XPATH,"//h1[text()='Contact Us']")