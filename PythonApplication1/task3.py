from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.CSS_SELECTOR, "[type=\"text\"]")

    for element in elements:
        element.send_keys("qwe")
        
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    
    time.sleep(30)
    
    browser.quit()

     