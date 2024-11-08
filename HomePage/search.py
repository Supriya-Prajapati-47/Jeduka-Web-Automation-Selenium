from config import *

#checking visiblity of seach button       
def search_button_visibility_003():
    driver = open_browser()
    modal_box()

    search_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//i[@class='icofont-search']"))
    )
    if search_icon.is_displayed:
        print("TC_003 PASSED: Search button is visible")
    else:
        print("TC_003 FAILED:Search button is not visible")
    
    driver.quit()
    print("Browser closed")

#search with empty search input
def search_empty_input_004():
    driver = open_browser()
    modal_box()

    search_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//i[@class='icofont-search']"))
    ).click()
    

    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='google_serach']"))
    ).send_keys("")
    
    
    
    search_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//i[@class='icofont-search']"))).click()
    

    driver.quit()
    print("Browser closed")

#searching with a single keyword search input
def search_single_keyword_005():
    driver = open_browser()
    modal_box()

    search_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//i[@class='icofont-search']"))
    ).click()
    

    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='google_serach']"))
    ).send_keys("Masters")
   
    
    search_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//i[@class='icofont-search']"))).click()
    

    driver.quit()
    print("Browser closed")


#searching with dropdown option selection
def search_from_dropdown_007():
    driver = open_browser()
    modal_box()

    search_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//i[@class='icofont-search']"))
    ).click()
   

    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='google_serach']"))
    ).send_keys("Masters in Computer Science in Canada")
   

    search_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='getName']"))
    ).click()
   
    driver.quit()
    print("Browser closed")