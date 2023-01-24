from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    label_x = browser.find_element(By.ID, "input_value")
    x = label_x.text
    res = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(res)

    cb_robot = browser.find_element(By.ID, "robotCheckbox")
    cb_robot.click()

    rb_robot = browser.find_element(By.ID, "robotsRule")
    rb_robot.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()