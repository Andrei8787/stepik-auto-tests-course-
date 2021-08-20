
import keyboard
from pathlib import Path
from selenium.webdriver import ActionChains
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath('browsers\chromedriver.exe'))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://mail.yandex.ru/')
        time.sleep(4)

    def _WebDriverWait(self, time, _method, target):
        if _method == "XPATH":
         WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.XPATH, target)))
        elif _method == "ID":
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.ID, target)))
        elif _method == "CSS":
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, target)))
        else:
            raise SystemError("Метод выбран не верно.")
    #Вход
    def test_something(self):
        self.driver.find_element_by_css_selector("div.HeadBanner-ButtonsWrapper a:nth-child(2)").click()
        self._WebDriverWait(10, "XPATH", "//input[@id='passp-field-login']")
        #WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='passp-field-login']")))
        self.driver.find_element_by_id("passp-field-login").click()
        keyboard.write('Ancherdincev8787@yandex.ru')
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='passp-button passp-sign-in-button']")))
        self.driver.find_element_by_xpath("//div[@class='passp-button passp-sign-in-button']").click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "passp-field-passwd")))
        self.driver.find_element_by_id("passp-field-passwd").click()
        keyboard.write('rfpfxtcndj87Q1987')
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "passp:sign-in")))
        self.driver.find_element_by_id("passp:sign-in").click()

    #Пустое значение логин
    def test_empty_value_login(self):
        self.driver.find_element_by_css_selector("div.HeadBanner-ButtonsWrapper a:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element_by_id("passp:sign-in").click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_id("field:input-login:hint").text, 'Логин не указан')

    #Пустое значение пароль
    def test_empty_value_pass(self):
        self.driver.find_element_by_css_selector("div.HeadBanner-ButtonsWrapper a:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element_by_id("passp-field-login").click()
        keyboard.write('Ancherdincev8787@yandex.ru')
        time.sleep(2)
        self.driver.find_element_by_id("passp:sign-in").click()
        time.sleep(2)
        self.driver.find_element_by_id("passp:sign-in").click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_id("field:input-passwd:hint").text, 'Пароь не указан')
        time.sleep(2)

    #установка аватарки
    def test_avatar(self):
        self.driver.find_element_by_css_selector("div.HeadBanner-ButtonsWrapper a:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element_by_id("passp-field-login").click()
        keyboard.write('Ancherdincev8787@yandex.ru')
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='passp-button passp-sign-in-button']").click()
        time.sleep(2)
        self.driver.find_element_by_id("passp-field-passwd").click()
        time.sleep(2)
        keyboard.write('rfpfxtcndj87Q1987')
        time.sleep(2)
        self.driver.find_element_by_id("passp:sign-in").click()
        time.sleep(2)
        if Path("D:\868vXowiL.jpg").is_file() == False:
            raise SystemError("Файл отсутсвует или переименован")
        self.driver.find_element_by_id("attach-control").send_keys("D:\868vXowiL.jpg")
        time.sleep(2)
        box = self.driver.find_element_by_css_selector("div.cropper-crop-box span.cropper-face")
        ActionChains(self.driver).move_to_element_with_offset(box, 50, 50).click_and_hold().move_to_element_with_offset(box, 130, 120).release().perform()
        time.sleep(2)

    def test_send_email(self):
        self.test_something()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.mail-ComposeButton-Wrap a.mail-ComposeButton")))
        self.driver.find_element_by_css_selector("div.mail-ComposeButton-Wrap a.mail-ComposeButton").click()
        self.assertEqual(self.driver.find_element_by_css_selector("div.composeYabbles[spellcheck='false']").text,'')
        keyboard.write("goltaeva@1c-connect.com")
        self.driver.find_element_by_css_selector("div.compose-LabelRow-Content input.composeTextField").send_keys("Привет")
        # keyboard.write("Это тестовое сообщение от Python")
        self.driver.find_element_by_css_selector("div.ComposeAttachFileButton").click()
        time.sleep(3)
        # Отправка письма
        # self.driver.find_element_by_css_selector("Button.Button2_view_action").click()
        # time.sleep(2)
    def test_avatar(self):
        self.test_something()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.user-pic__image")))
        self.driver.find_element_by_css_selector("img.user-pic__image").click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.user-pic__link")))
        self.driver.find_element_by_css_selector("a.user-pic__link").click()
        self.driver.find_element_by_id("passp_load_avatar").send_keys("D:\Для теста\ddd.jpeg")
        time.sleep(4)
        elem = self.driver.find_element_by_css_selector("div.Avatar-controlBtns button:nth-child(2)")
        if elem.is_displayed():
            self.driver.find_element_by_css_selector("span.Icon").click()
            time.sleep(4)
        else:
            self.driver.find_element_by_css_selector("span.user-account__name").click()
            time.sleep(4)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
