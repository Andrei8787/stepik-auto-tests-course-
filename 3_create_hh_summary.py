# ======================================================================================================================
# данный скрипт является примером возможностей взаимодействия с элементами интерфейса web-страниц
# используемые интернет-ресурсы выбраны случайно
# time.sleep() - добавлено для визуализации процессов
# сценарий: регистрация на internet-ресурсе
# Гунченко М.П.
# ======================================================================================================================
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class create_hh_summary(unittest.TestCase):
    

       # регистрация и создание резюме на HH
    def test_create_hh_summary(self):
        # инициализация браузера
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(executable_path=os.path.abspath('browsers\chromedriver.exe'), options=options)
        driver.implicitly_wait(10)

        # первая вкладка - hh
        driver.get('https://orenburg.hh.ru/')
        hh_tab = driver.window_handles[0]

        # вторая вкладка - почта
        driver.execute_script("window.open('');")
        mail_tab = driver.window_handles[1]
        driver.switch_to.window(mail_tab)
        driver.get('https://temp-mail.org/ru/')

        # получение временного адреса
        el = driver.find_element_by_xpath("//button[@class='btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn']")
        # ожидание изменения свойства элемента
        while el.get_property('disabled'):
            time.sleep(0.5)
        # ожидание
        time.sleep(2)
        # нажатие кнопки 'Скопировать в буфер обмена'
        el.click()

        # переход на вкладку HH
        driver.switch_to.window(hh_tab)
        # переход на форму регистрации
        driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[4]").click()
        # ввод адреса
        driver.find_element_by_name("login").send_keys(Keys.CONTROL,'v')
        time.sleep(2)
        # отправка
        driver.find_element_by_xpath("//button[@data-qa='account-signup-submit']").click()

        # переход на вкладку почты, обновляем ящик, открываем письмо, копируем код HH
        driver.switch_to.window(mail_tab)
        # ожидание письма - изменение интерфейса
        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//p[text()='Ожидание входящих писем']")))
        # выбор письма
        driver.find_element_by_xpath("//span[text()='Код подтверждения']/..").click()
        # прокрутка страницы вниз
        driver.execute_script("window.scrollTo(0, 200)")
        # ожидание
        time.sleep(2)
        # получение кода
        code = driver.find_element_by_xpath("//p[contains(text(),'ваш код для авторизации')]/../../td/p/b").text

        # переход на вкладку HH
        driver.switch_to.window(hh_tab)
        # ввод кода
        driver.find_element_by_name("otp-code-input").send_keys(code)
        # ожидание
        time.sleep(2)
        # нажатие 'Регистрация'
        driver.find_element_by_xpath("//div[@class='verification-submit']/button").click()

        ### регистрация пользователя
        # ввод имени
        driver.find_element_by_name("firstName").send_keys("Иван")
        # ввод пароля
        driver.find_element_by_name("lastName").send_keys("Попов")
        # нажатие 'Продолжить'
        driver.find_element_by_xpath("//div[@class='signup-submit']/button").click()

        ### заполнение резюме
        # номер телефона
        driver.find_element_by_name("phone[0].formatted").send_keys("9878560000")
        # прокрутка страницы вниз
        driver.execute_script("window.scrollTo(0, 100)")
        # дата рождения
        driver.find_element_by_xpath("//input[@data-name='birthday[0].date.day']").send_keys("22")
        driver.find_element_by_xpath("//select[@data-name='birthday[0].date.month']").click()
        driver.find_element_by_xpath("//select[@name='birthday[0].date']/option[text()='января']").click()
        driver.find_element_by_xpath("//input[@data-name='birthday[0].date.year']").send_keys("1984")
        # опыт работы
        driver.find_element_by_xpath("//label[@data-qa='with-experience']").click()
        # должность
        driver.find_element_by_xpath("(//div/span[@class='bloko-input-wrapper']/input)[4]").send_keys("Тестировщик ПО (автоматизация)")
        # зарплата
        driver.find_element_by_name("salary[0].amount").send_keys("9999999")
        # профессиональная область
        driver.find_element_by_name("specialization").click()
        driver.find_element_by_xpath("//input[@data-qa='bloko-tree-selector-popup-search']").send_keys("тестирование")
        driver.find_element_by_xpath("//span[text()='Тестирование']").click()
        driver.find_element_by_xpath("//button[@data-qa='bloko-tree-selector-popup-submit']").click()
        # прокрутка страницы вниз
        about_field = driver.find_element_by_name("skills[0].string")
        driver.execute_script("window.scrollTo(0, "+str(about_field.location['y'])+")")
        # о себе
        about_field.send_keys("Да просто умница!!!")

        # ожидание
        time.sleep(8)
        # нажатие 'Сохранить и опубликовать - закомментировано
        ## driver.find_element_by_xpath("//button[@data-qa='resume-submit']")
        # закрытие браузера
        driver.quit()
       

if __name__ == '__main__':
    unittest.main()