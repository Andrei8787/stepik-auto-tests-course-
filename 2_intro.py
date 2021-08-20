import os
import string
import time
import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import unittest
import keyboard
import urllib.request

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#
#
#
#
# time.sleep() - добавлено для визуализации
from selenium.webdriver.support.wait import WebDriverWait


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        if Path("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe").is_file() == False:
            raise SystemError("Браузер chrome не установлен, либо расположен по нештатному пути")

        self.driver = webdriver.Chrome(executable_path=os.path.abspath('browsers\chromedriver.exe'))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')


    # # Динамическое добавление/удаление элементов интерфейса
    # def test_add_delete_elements(self):
    #     # переход в соответствующий пункт меню
    #     self.driver.find_element_by_link_text("Add/Remove Elements").click()
    #     time.sleep(1)
    #     # добавление 4 элементов
    #     elem = self.driver.find_element_by_css_selector("div.example>button")
    #     for i in range(4):
    #         elem.click()
    #         time.sleep(1)
    #     # проверка количества элементов на странице
    #     assert len(self.driver.find_elements_by_css_selector("div#elements>button.added-manually")) == 4, "4 Кнопки Delete присутствуют"
    #
    #     # удаление первого элемента
    #     self.driver.find_element_by_css_selector("div#elements>button.added-manually:nth-child(1)").click()
    #     # удаление последнего элемента
    #     self.driver.find_element_by_css_selector("div#elements>button.added-manually:last-child").click()
    #
    #     # проверка количества элементов на странице
    #     assert len(self.driver.find_elements_by_css_selector("div#elements>button.added-manually")) == 2, "2 Кнопки Delete присутствуют"
    #
    #     # удаление остальных элементов
    #     elms = self.driver.find_elements_by_css_selector("div#elements>button.added-manually")
    #     for e in elms:
    #         time.sleep(1)
    #         e.click()
    #     # проверка количествя элементов на странице
    #     assert len(self.driver.find_elements_by_css_selector("div#elements>button.added-manually")) == 0, "Кнопки Delete отсутствуют"
    #
    # # прохождение basic авторизации - успех
    # def test_basic_auth(self):
    #     # переход в соответствующий пункт меню
    #     self.driver.find_element_by_link_text("Basic Auth").click()
    #     # ввод логина
    #     keyboard.write('admin')
    #     time.sleep(1)
    #     # переход на следующий элемент
    #     keyboard.press_and_release('tab')
    #     # ввод пароля
    #     keyboard.write('admin')
    #     time.sleep(1)
    #     # нажатие кнопки
    #     keyboard.press_and_release('enter')
    #     time.sleep(2)
    #     # проверка наличия текста на странице
    #     assert self.driver.find_element_by_css_selector('div.example p').text == 'Congratulations! You must have the proper credentials.', "Проверка успешной авторизации"
    #
    # # проверка (ресурс доступен, изображение отображается) картинок на странице
    # def test_check_images(self):
    #     # переход в соответствующий пункт меню
    #     self.driver.find_element_by_link_text('Broken Images').click()
    #     # получение списка элементов
    #     imgs = self.driver.find_elements_by_css_selector('div.example img')
    #     time.sleep(1)
    #
    #     # обход элементов в обратном порядке (для успеха первая интеррация)
    #     for img in reversed(imgs):
    #         img_src = img.get_attribute('src')
    #         # проверка1 - на доступность ресурса
    #         request = urllib.request.Request(img_src)
    #
    #         available = True
    #         try: urllib.request.urlopen(request)
    #         except urllib.error.URLError as e:
    #             available = False
    #
    #         assert available == True, "Доступность ресурса. Элемент - " + img_src
    #
    #         # проверка2 - на отображение на странице
    #         assert img.is_displayed() == True, "Отображение картинки на странице. Элемент - " + img_src
    #
    # # проверка состояния элементов Checkbox интефейса - состояние не меняется
    # def test_checkboxes(self):
    #     # переход в соответствующий пункт меню
    #     self.driver.find_element_by_link_text('Checkboxes').click()
    #     for i in range(4):
    #         els = self.driver.find_elements_by_css_selector("div.example form#checkboxes input[type='checkbox']")
    #         # проверка на штатное состояние элементов
    #         assert els[0].get_attribute("checked") != "true", "Загрузка страницы. Первый элемент откючен"
    #         assert els[1].get_attribute('checked') == "true", "Загрузка страницы. Второй элемент включен"
    #
    #         els[0].click()
    #         els[1].click()
    #         time.sleep(1)
    #         self.driver.refresh()
    #
    # # проверка СSS свойств элемента по-умолчанию и при наведении курсора мыши
    # def test_check_elements_properties(self):
    #     # переход в соответствующий пункт меню
    #     self.driver.find_element_by_link_text('Disappearing Elements').click()
    #     home_link = self.driver.find_element_by_css_selector("div.example li a[href='/']")
    #     # свойства элемента ДО наведения курсора мыши
    #     state1 = home_link.value_of_css_property('text-decoration') + "-" + home_link.value_of_css_property('font-size') + "-" + home_link.value_of_css_property('padding') + "-" +home_link.value_of_css_property('border')
    #     time.sleep(2)
    #     # наведение курсорв мыши на элемент
    #     ActionChains(self.driver).move_to_element(home_link).perform()
    #     # свойства элемента ПОСЛЕ наведения курсора мыши
    #     state2 = home_link.value_of_css_property('text-decoration') + "-" + home_link.value_of_css_property('font-size') + "-" + home_link.value_of_css_property('padding') + "-" + home_link.value_of_css_property('border')
    #     time.sleep(2)
    #     # проверка атрибутов элемента интерфейса
    #     self.assertEqual(state1, 'none solid rgb(218, 75, 75)-18px-0px 20px-1px solid rgb(204, 204, 204)', 'Ссылка Home: оформление, по-умолчанию')
    #     self.assertEqual(state2, 'none solid rgb(0, 0, 0)-20px-0px 20px-1px solid rgb(204, 204, 204)', 'Ссылка Home: оформление, hover')
    #
    # # проверка Drag and Drop элементов интерфейса
    # def test_DragAndDrop(self):
    #     # drag_and_drop и их эмуляции не работают... загрузка JS файла
    #     with open(os.path.abspath('drag_and_drop_helper.js'), 'r') as js_file:
    #         line = js_file.readline()
    #         script = ''
    #         while line:
    #             script += line
    #             line = js_file.readline()
    #     # переход в соответствующий пункт меню
    #     self.driver.find_element_by_link_text('Drag and Drop').click()
    #
    #     #el_a = self.driver.find_element_by_css_selector("div.column#column-a")
    #     #el_b = self.driver.find_element_by_css_selector("div.column#column-b")
    #     el_a_text = self.driver.find_element_by_css_selector("div.column#column-a>header").text
    #     el_b_text = self.driver.find_element_by_css_selector("div.column#column-b>header").text
    #     els = self.driver.find_elements_by_css_selector("div.column")
    #
    #     # проверка расположение элементов по-умолчанию A - B
    #     self.assertEqual(el_a_text, "A", "По-умолчанию у элемента column-a текст А")
    #     self.assertEqual(el_b_text, "B", "По-умолчанию у элемента column-b текст B")
    #     self.assertEqual(els[0].get_attribute("id"), "column-a", "По-умолчанию элемент column-a первый")
    #     self.assertEqual(els[1].get_attribute("id"), "column-b", "По-умолчанию элемент column-b первый")
    #     time.sleep(2)
    #     # перетаскивание элемента column-a на место элемента olumn-b
    #     self.driver.execute_script(script + "$('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    #     time.sleep(2)
    #     # считывание текста у элементов после перетаскивания
    #     el_a_text = self.driver.find_element_by_css_selector("div.column#column-a>header").text
    #     el_b_text = self.driver.find_element_by_css_selector("div.column#column-b>header").text
    #     # проверка на изменение текста элементов интерфейса
    #     self.assertEqual(el_a_text, "B", "По-умолчанию у элемента column-a текст B")
    #     self.assertEqual(el_b_text, "A", "По-умолчанию у элемента column-b текст A")
    #
    # # проверка динамики элементов интерфейса
    # def test_waiting_element(self):
    #     # переход в соответствующий пункт меню
    #     self.driver.find_element_by_link_text('Dynamic Controls').click()
    #     time.sleep(1)
    #
    #     self.driver.find_element_by_xpath('//form[@id="checkbox-example"]/button').click()
    #     time.sleep(2)
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@id='message']")))
    #     finally:
    #         # проверка, что элемент отсутствует
    #         self.assertEqual( len(self.driver.find_elements_by_xpath("//form[@id='checkbox-example']/div/input")), 0, "Элемент интерфейса checkbox отсутствует")
    #
    # # сценарий работы пользователя
    # def test_waiting_element(self):
    #     # переход в соответствующий пункт меню
    #     self.driver.find_element_by_link_text('WYSIWYG Editor').click()
    #     time.sleep(1)
    #     # меню
    #     self.driver.find_element_by_xpath("//span[@class='tox-mbtn__select-label']").click()
    #     time.sleep(1)
    #     # новый документ
    #     self.driver.find_element_by_xpath("//div[@class='tox-collection__item-label']").click()
    #     time.sleep(1)
    #
    #     # переход в область фрейма
    #     #self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
    #     self.driver.switch_to.frame('mce_0_ifr')
    #     # ввод текста - 3 строки
    #     self.driver.find_element_by_xpath("//body[@class='mce-content-body ']/p").click()
    #     self.driver.find_element_by_xpath("//body[@class='mce-content-body ']/p").send_keys("Строка1")
    #     self.driver.find_element_by_xpath("//body[@class='mce-content-body ']/p").send_keys(Keys.ENTER)
    #     self.driver.find_element_by_xpath("//body[@class='mce-content-body ']/p").send_keys("Строка2")
    #     self.driver.find_element_by_xpath("//body[@class='mce-content-body ']/p").send_keys(Keys.ENTER)
    #     self.driver.find_element_by_xpath("//body[@class='mce-content-body ']/p").send_keys("Строка3")
    #
    #     # обнаружение и выделение второй строки
    #     line2 = self.driver.find_element_by_xpath("//body[@id='tinymce']/p[2]")
    #     line2.click()
    #     line2.send_keys(Keys.SHIFT+Keys.HOME)
    #     time.sleep(2)
    #
    #     # переход в основной контент
    #     self.driver.switch_to.default_content()
    #     # параметры форматирования текста - жирный
    #     self.driver.find_element_by_xpath("//button[@aria-label='Bold']").click()
    #     time.sleep(1)
    #     # параметры форматирования текста - по центру
    #     self.driver.find_element_by_xpath("//button[@aria-label='Align center']").click()
    #     time.sleep(1)
    #     # параметры форматирования текста - шрифт 24pt
    #     self.driver.find_element_by_xpath("//div[@role='menubar']/button[4]").click()
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath("//div[@title='Font sizes']").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("//div[@title='24pt']").click()
    #     time.sleep(2)
    #
    #     # проверка на соответствие заданным параметрам форматирования текста
    #     # переход в область фрейма
    #     self.driver.switch_to.frame('mce_0_ifr')
    #     #
    #     line2 = self.driver.find_element_by_xpath("//body[@id='tinymce']/p[2]")
    #     decor = line2.value_of_css_property('text-decoration')
    #     print("sssssssssssssss..:"+decor)
    #     time.sleep(2)
    #
    #
    #     self.driver.switch_to.default_content()
    #     editor = self.driver.find_element_by_xpath("//div[@class='tox tox-tinymce']")
    #     x, y = editor.location['x'], editor.location['y']
    #     w, h = editor.size['width'], editor.size['height']
    #     print("x=",x ,";y=",y,"; w=",w,"; h=",h)
    #
    #     action = ActionChains(self.driver)
    #     #action.move_to_element(self.driver.find_element_by_xpath("//div[@class='tox-statusbar__resize-handle']")).pause(1).click_and_hold().pause(1).move_by_offset(x+w, y+h+50).release().perform()
    #     action.click_and_hold(self.driver.find_element_by_xpath("//div[@class='tox-statusbar__resize-handle']")).move_by_offset(x, y+20).perform()
    #     time.sleep(2)
    #
    # # проверка JavaScript сообщений (часть тестов)
    # def test_waiting_element(self):
    #     # переход в соответствующий пункт меню
    #     self.driver.find_element_by_link_text('JavaScript Alerts').click()
    #     time.sleep(1)
    #     # нажатие на кнопку Click for JS Alert - вызов сообщения
    #     self.driver.find_element_by_xpath("//button[text()='Click for JS Alert']").click()
    #     time.sleep(2)
    #     # переключение на сообщение
    #     alert = self.driver.switch_to.alert
    #     # проверка текста сообщения
    #     self.assertEqual("I am a JS Alert", alert.text, "Проверка текста сообщения - 1")
    #     # закрытие сообщения
    #     alert.accept()
    #     # проверка текста сообщения Result
    #     self.assertEqual("You successfully clicked an alert" , self.driver.find_element_by_xpath("//p[@id='result']").text, "Проверка сообщения Result. Первая кнопка.")
    #     time.sleep(2)
    #
    #     # нажатие на кнопку Click for JS Alert - вызов сообщения
    #     self.driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
    #     time.sleep(2)
    #     # переключение на сообщение
    #     alert = self.driver.switch_to.alert
    #     # проверка текста сообщения
    #     self.assertEqual("I am a JS Confirm", alert.text, "Проверка текста сообщения - 2")
    #     # закрытие сообщения -  ок
    #     alert.accept()
    #     # проверка текста сообщения Result
    #     self.assertEqual("You clicked: Ok" , self.driver.find_element_by_xpath("//p[@id='result']").text, "Проверка сообщения Result. Вторая кнопка. Ок.")
    #
    #     self.driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
    #     time.sleep(2)
    #     # переключение на сообщение
    #     alert = self.driver.switch_to.alert
    #     # проверка текста сообщения
    #     self.assertEqual("I am a JS Confirm", alert.text, "Проверка текста сообщения - 3")
    #     # закрытие сообщения -  ок
    #     alert.dismiss()
    #     # проверка текста сообщения Result
    #     self.assertEqual("You clicked: Cancel" , self.driver.find_element_by_xpath("//p[@id='result']").text, "Проверка сообщения Result. Вторая кнопка. Cancel.")
    #
    #     self.driver.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()
    #     time.sleep(2)
    #     # переключение на сообщение
    #     alert = self.driver.switch_to.alert
    #     # проверка текста сообщения
    #     self.assertEqual("I am a JS prompt", alert.text, "Проверка текста сообщения - 4")
    #     # ввод текста
    #     letters = string.ascii_letters
    #     randomString = ( ''.join(random.choice(letters) for i in range(10)) )
    #     alert.send_keys(randomString)
    #     # закрытие сообщения -  ок
    #     alert.accept()
    #     # проверка текста сообщения Result
    #     self.assertEqual("You entered: " + randomString , self.driver.find_element_by_xpath("//p[@id='result']").text, "Проверка сообщения Result. Третья кнопка. Ввод текста.")
    #     time.sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
