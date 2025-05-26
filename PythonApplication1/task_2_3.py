import math
import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

    select_list = browser.find_element(By.XPATH, "//select[@id='dropdown']")
    select_list.click()

    select_answer = browser.find_element(By.XPATH, "//option[@value='"+str(sum_numbers)+"']")
    select_answer.click()

    select_list.click()

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()