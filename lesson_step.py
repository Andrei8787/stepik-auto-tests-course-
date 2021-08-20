import unittest
from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):
    def test_something(self):



        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ищем все поля и заполняем.
            elements1 = browser.find_element_by_css_selector("div.first_block .form-group.first_class .form-control.first")
            elements1.send_keys("Андрей")

            elements2 = browser.find_element_by_css_selector("div.first_block .form-group.second_class .form-control.second")
            elements2.send_keys("Андреев")

            elements3 = browser.find_element_by_css_selector("div.first_block .form-group.third_class .form-control.third")
            elements3.send_keys("emailyadex.ru")


            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
