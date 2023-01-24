from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    label_x = browser.find_element(By.ID, "num1")
    x = label_x.text

    label_y = browser.find_element(By.ID, "num2")
    y = label_y.text

    res = int(x) + int(y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(res))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()