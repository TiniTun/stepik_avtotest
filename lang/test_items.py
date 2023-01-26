import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShop():

    def test_button(self, browser):

        try:
            url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

            browser.maximize_window()
            browser.get(url)

            button_check = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket"))
            )
            
            assert button_check, f"There isn't a button: {button_check}"

        finally:
            time.sleep(30)
