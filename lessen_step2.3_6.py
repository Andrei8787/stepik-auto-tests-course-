import unittest
from selenium import webdriver
import time
import math
import os

class MyTestCase(unittest.TestCase):
    def calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))
    def test_step5(self):
        try:
            link = "http://suninjuly.github.io/redirect_accept.html"
            browser = webdriver.Chrome()
            browser.get(link)

            button = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
            button.click()

            new_window = browser.window_handles[1]
            browser.switch_to.window(new_window)

            x_element = browser.find_element_by_css_selector("#input_value")
            x = x_element.text
            y = self.calc(x)

            answer = browser.find_element_by_css_selector("#answer")
            answer.send_keys(y)

            button1 = browser.find_element_by_css_selector(".btn.btn-primary")
            button1.click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
