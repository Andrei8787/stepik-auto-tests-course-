import unittest
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MyTestCase(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome(executable_path=os.path.abspath('browsers\chromedriver.exe'))
    #     self.driver.implicitly_wait(10)
    #     self.driver.maximize_window()
    #     self.driver.get('https://orenburg.hh.ru/')
    # Функция ожидания появления элемента
    def _WebDriverWait(self, time, _method, target):
        if _method == "XPATH":
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.XPATH, target)))
        elif _method == "ID":
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.ID, target)))
        elif _method == "CSS":
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, target)))
        else:
            raise SystemError("Метод выбран не верно.")

    def test_create_login(self):
        # Обход защиты
        webdriver.ChromeOptions().add_experimental_option("useAutomationExtension", False)
        webdriver.ChromeOptions().add_experimental_option("excludeSwitches", ["enable-automation"])
        webdriver.ChromeOptions().add_argument("--disable-blink-features=AutomationControlled")
        # Инициализация драйвера
        self.driver = webdriver.Chrome(executable_path=os.path.abspath('browsers\chromedriver.exe'))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://orenburg.hh.ru/employer')
        # Переменной присваиваем вкладку 1
        hh_tab = self.driver.window_handles[0]
        # Вызываем Java скрипт, создаём вкладку.
        self.driver.execute_script("window.open('');")
        # Переменной присваиваем вкладку 1
        mail_tab = self.driver.window_handles[1]
        # Переключаемся на вкладку 2.
        self.driver.switch_to.window(mail_tab)
        self.driver.get('https://temp-mail.org/ru/')
        # Определяем изменения поля временной почты для копирования по свойству disabled.
        attribute_title = self.driver.find_element_by_css_selector("button.btn-rds:nth-child(1)")
        while attribute_title.get_attribute('disabled'):
            time.sleep(1)
        # Копируем в буфер почту
        attribute_title.click()
        # Переходим на вкладку hh
        self.driver.switch_to.window(hh_tab)
        # Нажимаем кнопку Войти
        self._WebDriverWait(10, "CSS", "div.supernova-navi-item:nth-child(5) > a:nth-child(1)")
        self.driver.find_element_by_css_selector("div.supernova-navi-item:nth-child(5) > a:nth-child(1)").click()
        self._WebDriverWait(10,"XPATH", "//button[@class='bloko-button bloko-button_primary-minor bloko-button_rounded']")
        self.driver.find_element_by_xpath("//button[@class='bloko-button bloko-button_primary-minor bloko-button_rounded']").click()
        # Вставляем из буфера почту в поле.
        self._WebDriverWait(10, "CSS", "input.bloko-input:nth-child(1)")
        self.driver.find_element_by_css_selector("input.bloko-input:nth-child(1)").send_keys(Keys.CONTROL + 'v')
        # Нажимаем Продолжить
        self.driver.find_element_by_css_selector(".account-login-actions > button").click()
        #
        self.driver.switch_to.window(mail_tab)
        self._WebDriverWait(30, "XPATH", "//span[text()='Код подтверждения']/..")
        self.driver.find_element_by_xpath("//span[text()='Код подтверждения']/..").click()
        time.sleep(1000)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
