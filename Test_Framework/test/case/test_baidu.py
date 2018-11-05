#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ...utils.config import Config, DRIVER_PATH, DATA_PATH
from ...utils.log import logger
from ...utils.file_reader import ExcelReader


class TestBaidu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu百度.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe', chrome_options=option)
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def te1st_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)
            logger.info(link.text)

    def te1st_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('250')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)
            logger.info(link.text)

    def test_search_excel(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    print(link.text)
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    unittest.main()



