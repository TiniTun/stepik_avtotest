from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element(By.XPATH, "//label[contains(text(), 'First name*')]/following-sibling::input")
    element1.send_keys("Test")
    element2 = browser.find_element(By.XPATH, "//label[contains(text(), 'Last name*')]/following-sibling::input")
    element2.send_keys("Testov")
    element3 = browser.find_element(By.XPATH, "//label[contains(text(), 'Email *')]/following-sibling::input")
    element3.send_keys("e@e.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    label_x = browser.find_element(By.ID, "file")
    label_x.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()