import math
import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element=browser.find_element(By.XPATH, "//span[@id='num1']")
    num1= num1_element.text

    num2_element=browser.find_element(By.XPATH, "//span[@id='num2']")
    num2= num2_element.text

    sum_numbers = int(num1)+int(num2)
    print(sum_numbers)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_numbers))

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()