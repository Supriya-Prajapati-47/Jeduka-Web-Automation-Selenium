from config import *

#selectio of a course from nav bar
def selecting_course():
    try:
        driver = open_browser()
        action = ActionChains(driver)
        modal_box()

        

        hover_courses = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@id='Courses']")))
        action.move_to_element(hover_courses).perform()
        
        click_program_type = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Computer Engineering']"))
        )
        click_program_type.click()
        
        time.sleep(2)

        driver.quit()
    
    except Exception as e:
        driver.quit()
    
    



    


