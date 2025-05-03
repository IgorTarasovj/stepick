import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	treasure = browser.find_element(By.XPATH, "//img[@id='treasure']")
	x = treasure.get_attribute("valuex")

	value_x = calc(x)

	input_text = browser.find_element(By.XPATH, "//input[@id='answer']")
	input_text.send_keys(value_x)

	checkbox =  browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
	checkbox.click()

	radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
	radiobutton.click()

	submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
	submit_button.click()

finally:
	time.sleep(12)
	browser.quit()