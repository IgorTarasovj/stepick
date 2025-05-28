import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser =  webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x= x_element.text

    math_answer=calc(x)
    
    answer = browser.find_element(By.XPATH, "//input[@id='answer']")
    answer.send_keys(math_answer)
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

    checkbox =  browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    checkbox.click()
    
    radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    radiobutton.click()
    
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    

finally:
    time.sleep(12)
    browser.quit()