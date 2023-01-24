from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    text_100 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.CSS_SELECTOR, "button#book")
    button.click()


    label_x = browser.find_element(By.ID, "input_value")
    x = label_x.text
    res = calc(x)

    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(res)

    button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[-1])
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()