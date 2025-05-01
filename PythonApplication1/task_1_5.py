from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ��� ���, ������� ��������� ������������ ����
    input_first_name = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
    input_first_name.send_keys("Ivan")

    input_last_name = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
    input_last_name.send_keys("Ivanov")

    input_email = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
    input_email.send_keys("ivanovivan@mail.com")


    # ���������� ����������� �����
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

    # ������� �������, ���������� �����
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # ���������� � ���������� welcome_text ����� �� �������� welcome_text_elt
    welcome_text = welcome_text_elt.text

    # � ������� assert ���������, ��� ��������� ����� ��������� � ������� �� �������� �����
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()