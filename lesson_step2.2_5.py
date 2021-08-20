import unittest
from selenium import webdriver
import time
import math

class MyTestCase(unittest.TestCase):
    def calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))
    def test_step5(self):
        try:
            link = "http://SunInJuly.github.io/execute_script.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Получаем Х и считаем по формуле
            x_element = browser.find_element_by_css_selector("#input_value")
            x = x_element.text
            y = self.calc(x)
            print(y)
            # вставляем в текстовое поле
            answer = browser.find_element_by_css_selector("#answer")
            answer.send_keys(y)
            # ставием чекбокс
            check = browser.find_element_by_css_selector("#robotCheckbox")
            check.click()
            # ставим радиобатон
            button1 = browser.find_element_by_css_selector(".btn.btn-primary")
            browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
            radio = browser.find_element_by_css_selector("#robotsRule")
            radio.click()
            # Нажимаем кнопку
            button1.click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
