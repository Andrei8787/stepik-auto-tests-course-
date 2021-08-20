import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

class MyTestCase(unittest.TestCase):
    # def calc(self, x):
    #     return str(math.log(abs(12*math.sin(int(x)))))
    def test_step5(self):
        try:
            link = "http://suninjuly.github.io/selects1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Получаем Х и считаем по формуле
            x_element = browser.find_element_by_css_selector("#num1")
            x = x_element.text
            print(x)
            y_element = browser.find_element_by_css_selector("#num2")
            y = y_element.text
            print(y)
            sum = int(x)+int(y)
            print(sum)
            select = Select(browser.find_element_by_css_selector("#dropdown"))
            select.select_by_value(str(sum))

            # Нажимаем кнопку.
            button1 = browser.find_element_by_css_selector(".btn.btn-default")
            button1.click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
