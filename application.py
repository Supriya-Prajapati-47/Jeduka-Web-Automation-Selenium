from config import *

def application_form():
    driver = open_browser()
    modal_box()
#page redirection
    action = ActionChains(driver)

    hover_courses = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='Courses']")))
    action.move_to_element(hover_courses).perform()
    
    click_program_type = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Computer Engineering']"))
    )
    click_program_type.click()
    time.sleep(2)

    apply_now_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='https://www.jeduka.com/apply-now-mykolas-romeris-university']")))
    
    apply_now_button.click()
    
    time.sleep(2)


    FullName = "Supriya"
    Email = "pebaf15310@nastyx.com"
    Contact_no = "9841456456"
#filling form
    full_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='name']"))
    )
    full_name.send_keys(FullName)

    email_id = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='email_address']"))
    )
    email_id.send_keys(Email)

    mobile_no = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='mobile_number']"))
    ).send_keys(Contact_no)

    current_country = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='country']"))
    )

    #select instance
    select = Select(current_country)
    select.select_by_visible_text('Nepal')
    time.sleep(3)
        
    Current_state = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='state']"))
    )

    #select instance
    select = Select(Current_state)
    select.select_by_visible_text('Bagmati')
    time.sleep(3)

    current_city = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='city']"))
    )  

    #select instance
    select = Select(current_city)
    select.select_by_visible_text('Kathmandu')
    time.sleep(3)


    preferred_country = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='program_country']"))
    )
    #select instance
    select = Select(preferred_country)
    select.select_by_visible_text('UK')
    time.sleep(3)

    preferred_courses = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='program']"))
    )

    #select instance
    select = Select(preferred_courses)
    select.select_by_visible_text('Arts')
    time.sleep(3)

    preferred_course_specialization = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='program_type']"))
    )
    #select instance
    select = Select(preferred_course_specialization)
    select.select_by_visible_text('Arts')
    time.sleep(3)
    
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='signup']"))
    ).click()

    time.sleep(3)

    assert "thankyou" in driver.current_url
    print("Submission successful")
    
    driver.quit()
    print("Browser closed")
