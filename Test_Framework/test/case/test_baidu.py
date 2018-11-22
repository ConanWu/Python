#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Framework.utils.config import Config, DATA_PATH, DRIVER_PATH, REPORT_PATH
from Test_Framework.utils.log import logger
from Test_Framework.utils.file_reader import ExcelReader
from Test_Framework.utils.HTMLTestRunner import HTMLTestRunner
from Test_Framework.test.page.baidu_result_page import BaiduMainPage, BaiduResultPage
from Test_Framework.utils.assertion import Assertion
from Test_Framework.utils.client import HTTPClient


class TestBaidu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu百度.xlsx'
    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')
    driver = webdriver.Chrome(executable_path=os.path.join(DRIVER_PATH, 'chromedriver.exe'))

    def sub_setUp(self):
        self.page = BaiduMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_search_0(self):
        self.driver.get(self.URL)
        self.driver.find_element(*self.locator_kw).send_keys('selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)
            logger.info(link.text)

    def test_search_1(self):
        try:
            self.driver.get(self.URL)
            self.driver.find_element(*self.locator_kw).send_keys('250')
            self.driver.find_element(*self.locator_su).click()
            time.sleep(2)
            links = self.driver.find_elements(*self.locator_result)
            for link in links:
                print(link.text)
                logger.info(link.text)
        finally:
            self.driver.quit()

    def execute_add(self):
        print("bbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.assertEqual('1', '1')
        Assertion.assert_compare(1, 2)
        raise AssertionError('For testing')

    def test_baidu_http(self):
        self.client = HTTPClient(self.URL, method='GET')
        res = self.client.send()
        logger.debug(res.text)
        self.assertIn('百度一下，你就知道', res.text)

    def test_search_excel(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            try:
                with self.subTest(aa=d):
                    self.sub_setUp()
                    self.page.search(d['search'])
                    time.sleep(2)
                    self.page = BaiduResultPage(self.page)
                    links = self.page.result_links
                    for link in links:
                        print(link.text)
                        logger.info(link.text)
            finally:
                self.sub_tearDown()


if __name__ == '__main__':
    unittest.main()




