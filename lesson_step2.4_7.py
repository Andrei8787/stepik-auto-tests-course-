import unittest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase(unittest.TestCase):
    def calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))
    def test_step5(self):
        try:
            link = "http://suninjuly.github.io/explicit_wait2.html"
            browser = webdriver.Chrome()
            # Не явное ожидание
            browser.implicitly_wait(1)
            browser.get(link)

            # Явное ожидание
            WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

            button = browser.find_element_by_id("book")
            button.click()

            # Считаем формулу
            x_element = browser.find_element_by_css_selector("#input_value")
            x = x_element.text
            y = self.calc(x)

            # заполняем ответ в поле
            answer = browser.find_element_by_css_selector("#answer")
            answer.send_keys(y)

            # Ищем кнопку и скролим окно до него
            button1 = browser.find_element_by_id("solve")
            browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
            button1.click()

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
