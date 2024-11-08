from config import *

def logo_visibility_001():
    driver = open_browser()
    modal_box()

#TC_HP_001 locate company logo
    company_logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='logo']")))

    if company_logo.is_displayed:    
        print("TC_001 PASSED: logo is visible")
    else:
        print("TC_001 FAILED:logo is not visible")

    driver.quit()
    print("Browser closed")


#TC_HP_002 hovering navigation menu 
def hover_nav_menu_002():
    driver = open_browser()
    modal_box()
    action = ActionChains(driver)
 #country
    hover_country = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='Country']")))
    action.move_to_element(hover_country).perform()
    

 #courses
    hover_courses = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='Courses']")))
    action.move_to_element(hover_courses).perform()

 #exam
    hover_exam = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='Exam']")))
    action.move_to_element(hover_exam).perform()

 #articles
    hover_articles = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='Articles']")))
    action.move_to_element(hover_articles).perform()

 #jeduka zone
    hover_jeduka_zone = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='JedukaZone']")))
    action.move_to_element(hover_jeduka_zone).perform()

 #student support service
    hover_student_support = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Student Support Services']")))
    action.move_to_element(hover_student_support).perform()
    time.sleep(1)
    
    driver.quit()

    

def whatsapp_icon_020():
    driver = open_browser()
    modal_box()

    time.sleep(2)
    icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-whatsapp']"))
    )

    icon.click()
    time.sleep(2)

    assert "api.whatsapp.com" in driver.current_url

    driver.quit()
    print("Browser closed")


def find_courses_to_study_abroad():
    driver = open_browser()
    modal_box()

    preferred_country = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='searchby-country']"))
    )
    #select instance
    select = Select(preferred_country)
    select.select_by_visible_text('UK')
    time.sleep(3)


    select_courses = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='searchby-course']"))
    )
    #select instance
    select = Select(select_courses)
    select.select_by_visible_text('Arts')
    time.sleep(3)

    select_courses_type = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='searchby-course-specialization']"))
    )
    #select instance
    select = Select(select_courses_type)
    select.select_by_visible_text('Arts')
    time.sleep(3)

    search_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='filterCountry']")))
    
    search_now_button.click()



def reach_out_to_us_025():
    driver = open_browser()
    modal_box()

    # #scroll to reachout section
    # action = ActionChains(driver)

    # element_to_scroll = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='Study Abroad']"))
    # )

    # action.move_to_element(element_to_scroll).perform()

    Full_name = "Supriya"
    Contact_no = "9841456456"
    Email = "xilat87677@asaud.com"
    

    fullname = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).send_keys(Full_name)
   

    mobile = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='mobile_number']"))).send_keys(Contact_no)
    

    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='email_address']"))).send_keys(Email)
    time.sleep(5)
## selecting country
    select_country = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='current_country']"))
    )

    #select instance
    select = Select(select_country)
    select.select_by_visible_text('Nepal')
    time.sleep(3)

## selecting state
    select_state = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='current_state']"))
    )

    #select instance
    select = Select(select_state)
    select.select_by_visible_text('Bagmati')
    time.sleep(3)

    
## selecting 
    select_city = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='current_city']"))
    )

    #select instance
    select = Select(select_city)
    select.select_by_visible_text('Kathmandu')
    time.sleep(3)

    subscribe_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='newsletter_submit']"))).click()
    
    
    if 'thankyou' in driver.current_url:
        print("Thank you is visible")
    else:
        print("Test failed")
    
    time.sleep(5)

    driver.quit()







