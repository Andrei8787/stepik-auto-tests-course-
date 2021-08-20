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
            link = "http://suninjuly.github.io/file_input.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first = browser.find_element_by_name("firstname")
            first.send_keys("Первое")

            last = browser.find_element_by_name("lastname")
            last.send_keys("второе")

            email = browser.find_element_by_name("email")
            email.send_keys("Мыло")

            file = browser.find_element_by_css_selector("#file")
            current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
            file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
            file.send_keys(file_path)

            button = browser.find_element_by_css_selector(".btn.btn-primary")
            button.click()


        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
