from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    label_x = browser.find_element(By.ID, "input_value")
    x = label_x.text
    res = calc(x)

    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(res)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[-1])
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()