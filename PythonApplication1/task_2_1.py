import math
from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "https://suninjuly.github.io/math.html"

	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
	x = x_element.text
	y = calc(x)

	input_text = browser.find_element(By.XPATH, "//input[@id='answer']")
	input_text.send_keys(y)

	checkbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
	checkbox.click()

	radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
	radiobutton.click()

	button = browser.find_element(By.XPATH, "//button[@type='submit']")
	button.click()


finally:
	time.sleep(12)
	browser.quit()