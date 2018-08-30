#!usr/bin/python3
# -*- coding:utf-8 -*-

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Framework.utils.config import Config, DRIVER_PATH, LOG_PATH
import logging


class TestBaidu1(unittest.TestCase):
    URL = Config().get('URL')

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.join(DRIVER_PATH, 'chromedriver.exe'))
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search0(self):
        self.driver.find_element(*self.locator_kw).send_keys('hello world')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def test_baidu_search1(self):
        self.driver.find_element(*self.locator_kw).send_keys('desperate to live')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def log(self):
        logger = logging.getLogger('test')
        logger.setLevel(logging.DEBUG)
        format_obj = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # logging.basicConfig()
        stream_hander = logging.StreamHandler()
        stream_hander.setLevel(logging.WARNING)
        stream_hander.setFormatter(format_obj)
        logger.addHandler(stream_hander)

        file_hander = logging.FileHandler(os.path.join(LOG_PATH, 'test1.log'))
        file_hander.setLevel(logging.INFO)
        file_hander.setFormatter(format_obj)
        logger.addHandler(file_hander)
        return logger

if __name__ == '__main__':
    # unittest.main()
    TestBaidu1().log().warning('warning')

    a = 2




