#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
import unittest

from Test_Framework.utils.config import Config, DATA_PATH, REPORT_PATH
from Test_Framework.utils.log import logger
from Test_Framework.utils.file_reader import ExcelReader
from Test_Framework.utils.HTMLTestRunner import HTMLTestRunner
from Test_Framework.test.page.baidu_result_page import BaiduMainPage, BaiduResultPage


class TestBaidu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu百度.xlsx'

    def sub_setUp(self):
        self.page = BaiduMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

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
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试百度搜索', description='修改报告')
        runner.run(TestBaidu('test_search_excel'))
    #f.close()



