from config import *
# Clicking on request for free advice button
def request_advice_button_019():
    driver = open_browser()
    modal_box()

    request_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".free_advice_btn.btn-2")))

    request_button.click()
    
#registration form fillup
    FullName = "Supriya"
    Email = "pebaf15310@nastyx.com"
    Contact_no = "9841456456"

#personal details
    full_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='name']"))
    )
    full_name.send_keys(FullName)

    email_id = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='email_address']"))
    ).send_keys(Email)

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

#Future Education Prospects
    intake = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='intake']"))
    )
#select instance
    select = Select(intake)
    select.select_by_index(0)
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

#Current education details

    education = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='edu_qualification']"))
    )
#select instance
    select = Select(education)
    select.select_by_visible_text("Bachelor Degree – 4th Year")
    time.sleep(3)

    exam_appeared = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='IELTS']"))
    )
    exam_appeared.click()
    
    score = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='exam_score_2']"))
    ).send_keys("7")
    time.sleep(2)

    checkmark = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='checkmark']"))
    ).click()
    time.sleep(2)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='signup']"))
    ).click()

    time.sleep(2)

    assert "thankyou" in driver.current_url
    print("Submission successful")
    
    driver.quit()
    print("Browser closed")
