from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def open_browser():
    global driver
    #launching browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    #Opening website
    driver.get('https://www.jeduka.com/')

    assert 'jeduka' in driver.current_url

    homepage_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='logo']")))
    
    return driver


def modal_box():
    try:
        modal_box = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='btn-close']")))
    
        modal_box.click()
        time.sleep(1)   
    except Exception as e:
        print(e)





