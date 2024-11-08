from config import *

#selection of a articles from nav bar
def selecting_articles():
    driver = open_browser()
    modal_box()
    action = ActionChains(driver)

#clicking on article from nav bar
    hover_article = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='Articles']")))
    action.move_to_element(hover_article).perform()

    hover_article.click()

#filter article category
    filter_article_category = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='vcategory']"))
    )
    #select instance
    select = Select(filter_article_category)
    select.select_by_visible_text('Canada')
    time.sleep(3)

# filter article
    filter = "mba"

    filter_article = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='vArticle']"))
    )
    filter_article.send_keys(filter)
    time.sleep(3)
    filter_mba = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//li[text()= "1 Year MBA in Canada"]'))
    )
    filter_mba.click()
    time.sleep(3)

    assert "1-year-mba-programs-in-canada" in driver.current_url, "URL doesnot match"
    print("url matched")

    driver.quit()



