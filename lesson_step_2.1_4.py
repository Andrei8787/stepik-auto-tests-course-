import unittest
from selenium import webdriver
import time
import math

class MyTestCase(unittest.TestCase):
    def calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))
    def test_step5(self):
        try:
            link = "http://suninjuly.github.io/get_attribute.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Получаем Х и считаем по формуле
            x_element = browser.find_element_by_css_selector("#treasure")
            x = x_element.get_attribute("valuex")
            y = self.calc(x)
            # Вводим ответ в текстовое поле.
            answer = browser.find_element_by_css_selector("#answer")
            answer.send_keys(y)
            # Ставим чекбокс
            chek_robot = browser.find_element_by_css_selector("#robotCheckbox")
            chek_robot.click()
            # Ставим радиобатон
            radio_robot = browser.find_element_by_css_selector("#robotsRule")
            radio_robot.click()

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
