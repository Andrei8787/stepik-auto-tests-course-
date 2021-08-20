# ======================================================================================================================
# данный скрипт является примером возможностей взаимодействия с элементами интерфейса web-страниц
# используемые интернет-ресурсы выбраны случайно
# time.sleep() - добавлено для визуализации процессов
# сценарий: использование графического редактора
# Гунченко М.П.
# ======================================================================================================================
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pathlib import Path

class MakePoster(unittest.TestCase):
    # используемый браузер: 1 - chrome, 2 - firefox
    browser = 1;

    def setUp(self):
        if self.browser == 1:
            if Path("C:\Program Files\Google\Chrome\Application\chrome.exe").is_file() == False:
                raise SystemError("Браузер chrome не установлен, либо расположен по нештатному пути")
            self.driver = webdriver.Chrome(executable_path=os.path.abspath('browsers\chromedriver.exe'))
        elif self.browser ==2:
            if Path("C:\Program Files\Mozilla Firefox\firefox.exe").is_file() == False:
                raise SystemError("Браузер firefox не установлен, либо расположен по нештатному пути")
            self.driver = webdriver.Firefox(executable_path=os.path.abspath('geckodriver.exe'))
        else:
            raise SystemError("Тип браузера указан некорректно.")

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://www.newart.ru/htm/flash/risovalka_9.php')


    # пример создания постера
    def test_create_simple_poster(self):
        # ожидание
        time.sleep(4)
        # переход в область фрейма
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        # размер канвы
        canvas = self.driver.find_element_by_xpath("//*[@id='canvas-background-view']")
        x, y = canvas.location['x'], canvas.location['y']
        w, h = canvas.size['width'], canvas.size['height']

        # выбор инструмента - линия
        self.driver.find_element_by_id("tool_line").click()
        # рисование
        ActionChains(self.driver).move_to_element_with_offset(canvas, x+100, y+100).click_and_hold().move_to_element_with_offset(canvas, x+200, y+100).release().\
            move_to_element_with_offset(canvas, x+200, y+100).click_and_hold().move_to_element_with_offset(canvas, x+200, y+200).release().\
            move_to_element_with_offset(canvas, x+200, y+200).click_and_hold().move_to_element_with_offset(canvas, x+100, y+200).release().\
            move_to_element_with_offset(canvas, x+100, y+200).click_and_hold().move_to_element_with_offset(canvas, x+100, y+100).release().\
            move_to_element_with_offset(canvas, x+90, y+100).click_and_hold().move_to_element_with_offset(canvas, x+150, y+50).release().\
            move_to_element_with_offset(canvas, x+150, y+50).click_and_hold().move_to_element_with_offset(canvas, x+210, y+100).release().perform()

        # выбор инструмента - прямоугольник
        self.driver.find_element_by_id("tool_rect").click()
        # рисование
        ActionChains(self.driver).move_to_element_with_offset(canvas, x+120, y+120).click_and_hold().move_to_element_with_offset(canvas, x+140,y+140).release().perform()

        # выбор инструмента - фигуры
        self.driver.find_element_by_id("tools_shapelib_show").click()
        # выбор категории
        self.driver.find_element_by_xpath("//div[@data-cat='basic']").click()
        # выбор "смайлик"
        self.driver.find_element_by_id("shapelib_smiley").click()
        # быбор элемента палитры - Stroke
        self.driver.find_element_by_xpath("//div[@class='palette_item' and @data-attr='stroke stroke-opacity' and @title='#41e841']").click()
        # выбор элемента палитры - Fill
        self.driver.find_element_by_xpath("//div[@class='palette_item' and @data-attr='fill fill-opacity' and @title='#e8e841']").click()
        # рисование
        ActionChains(self.driver).move_to_element_with_offset(canvas, x+300, y+300).click_and_hold().move_to_element_with_offset(canvas, x+400,y+400).release().perform()

        # выбор инструмента
        self.driver.find_element_by_id("tool_foreign").click()
        # рисование
        ActionChains(self.driver).move_to_element_with_offset(canvas, x+150, y+100).click_and_hold().move_to_element_with_offset(canvas, x+1050,y+350).release().perform()
        # выбор объекта
        text = self.driver.find_element_by_xpath("//p[text()='text']")
        text.click()
        text.click()
        time.sleep(2)
        # выделение текста
        text.send_keys(Keys.CONTROL,'a')
        # ввод текста
        text.send_keys('selenium')

        # выбор инструмента - стрелка
        self.driver.find_element_by_id("tool_select").click()
        # изменение размера шрифта
        font_size = self.driver.find_element_by_xpath("//input[@data-attr='font-size']")
        font_size.click()
        for i in range(35):
            font_size.send_keys(Keys.DOWN)

        # выбор инструмента - поворот элемента
        text.click()
        mover = self.driver.find_element_by_id("selectorGrip_rotate")
        movement = ActionChains(self.driver)
        offset = -2
        for i in range(4):
            movement.click_and_hold(mover).move_to_element_with_offset(mover, offset, -10).move_to_element_with_offset(mover, offset-2, -10).release().perform()
            offset = offset - 2
        # ожидание
        time.sleep(8)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()