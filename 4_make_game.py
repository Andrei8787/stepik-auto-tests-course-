import os
import random
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from array import *
from selenium.webdriver.common.keys import Keys
from pathlib import Path


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath('browsers\chromedriver.exe'))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://www.newart.ru/htm/flash/risovalka_9.php')
        time.sleep(4)

    def test_create_game(self):
        #time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        canvas = self.driver.find_element_by_xpath("//*[@id='canvas-background-view']")
        x, y = canvas.location['x'], canvas.location['y']
        w, h = canvas.size['width'], canvas.size['height']
        # Получаем массив
        balls = self.driver.find_elements_by_css_selector("div.palette_item[data-attr='fill fill-opacity']")
        count_balls = len(balls)
        rand_balls = random.choice(balls)
        # Выбираем элемент
        self.driver.find_element_by_id("tool_ellipse").click()
        # Рисуем рандомно
        for i in range(1):
            n = random.randint(1, 500)
            m = random.randint(1, 500)
            #self.driver.find_element_by_xpath("div.palette_item[data-attr='fill fill-opacity' title='#ffffff']").click()
            self.driver.find_element_by_xpath("//div[@class='palette_item' and @data-attr='fill fill-opacity' and @title='#eb1a1a']").click()
            ActionChains(self.driver).move_to_element_with_offset(canvas, x+n, y+m).click_and_hold().move_to_element_with_offset(canvas, x+n+100,y+m+100).release().perform()
            time.sleep(0.5)

       # self.driver.find_element_by_css_selector("div.tool-area button[data-hoveropen='file']").click()
       # time.sleep(2)

    def tearDown(self):
      self.driver.quit()

if __name__ == '__main__':
    unittest.main()
