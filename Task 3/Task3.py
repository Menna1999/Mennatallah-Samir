from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def start():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.Google.com")
    sourcetext = driver.page_source
    lang = "English"
    if lang in sourcetext:
        driver.find_element(By.LINK_TEXT,"English").click()
    return driver


# Write "Python" in search bar --> click enter
def test_enter_normal(driver):
    search_box = driver.find_elements(By.NAME,"q")
    assert len(search_box)          # Search box element is displayed
    search_box[0].send_keys("Python")
    search_box[0].send_keys(Keys.ENTER)

    feeling_lucky = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]")
    assert not len(feeling_lucky)   # "Feeling Lucky" element is no longer displayed --> moved to results page
    stats = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[7]/div[1]/div/div/div/div") # result stats --> search results were returned
    if stats.is_displayed():
        print("Test Passed!")
    else:
        print("Test Failed!")
    driver.close()



# Write nothing in search bar --> click enter
def test_enter_abnormal(driver):
    search_box = driver.find_elements(By.NAME,"q")
    assert len(search_box)            # Search box element is displayed
    search_box[0].send_keys("")       # Don't write anything
    search_box[0].send_keys(Keys.ENTER)

    feeling_lucky = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]")
    assert len(feeling_lucky)         # "Feeling Lucky" element is still displayed --> no moving to results page
    if feeling_lucky[0].is_displayed():
        print("Test Passed!")
    else:
        print("Test Failed!")
    driver.close()



# Write "Python" in search bar --> click Google Search
def test_button_normal(driver):
    search_box = driver.find_elements(By.NAME,"q")
    assert len(search_box)          # Search box element is displayed
    search_box[0].send_keys("Python")

    search_button = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")  # "Google Search" button
    
    assert len(search_button)       # Search button element is displayed
    search_button[0].click()

    assert not len(driver.find_elements(By.CLASS_NAME,"RNmpXc"))  # "Feeling Lucky" element is no longer displayed --> moved to results page
    stats = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[7]/div[1]/div/div/div/div") # result stats --> search results were returned
    if stats.is_displayed():
        print("Test Passed!")
    else:
        print("Test Failed!")
    driver.close()



# Write Nothing in search bar --> click Google Search
def test_button_abnormal(driver):
    search_box = driver.find_elements(By.NAME,"q")
    assert len(search_box)          # Search box element is displayed
    search_box[0].send_keys("")     # Don't write anything

    search_button = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")  # "Google Search" button
    assert len(search_button)       # Search button element is displayed
    search_button[0].click()

    feeling_lucky = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]")
    assert len(feeling_lucky)       # "Feeling Lucky" element is still displayed --> no moving to results page
    if feeling_lucky[0].is_displayed():
        print("Test Passed!")
    else:
        print("Test Failed!")
    driver.close()


# Write "Python" in search bar --> clear
def test_clear(driver):
    search_box = driver.find_elements(By.NAME,"q")
    assert len(search_box)          # Search box element is displayed
    search_box[0].send_keys("Python")

    clear_button = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[1]/span[1]")  # "X" button
    assert len(clear_button)        # Clear button element is displayed
    clear_button[0].click()

    input_text = search_box[0].get_attribute('value')
    if input_text == "":
        print("Test Passed!")
    else:
        print("Test Failed!")
    driver.close()


# Write nothing in search bar --> clear button is not displayed
def test_no_clear(driver):
    search_box = driver.find_elements(By.NAME,"q")
    assert len(search_box)             # Search box element is displayed

    clear = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[1]/span[1]")

    if clear[0].is_displayed() == False: # Clear button element is not displayed 
        print("Test Passed!")
    else:
        print("Test Failed!")
    driver.close()



def main():
    driver1 = start() 
    test_enter_normal(driver1)    # Write "Python" in search bar --> click enter

    driver2 = start()
    test_enter_abnormal(driver2)  # Write nothing in search bar --> click enter

    driver3 = start()
    test_button_normal(driver3)   # Write "Python" in search bar --> click Google Search

    driver4 = start()
    test_button_abnormal(driver4) # Write nothing in search bar --> click Google Search

    driver5 = start()
    test_clear(driver5)             # Write "Python" in search bar --> clear input

    driver6 = start()
    test_no_clear(driver6)          # Write nothing in search bar --> no clear input



if __name__ == "__main__":
    main()
