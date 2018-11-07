#!usr/bin/python3
# -*- coding:utf-8 -*-

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Framework.utils.config import Config, DRIVER_PATH, LOG_PATH, DATA_PATH, REPORT_PATH
import logging
from logging import handlers
import xlrd
from Test_Framework.test.case.test_baidu import TestBaidu
from HTMLTestRunner import HTMLTestRunner


class TestBaidu1(unittest.TestCase):
    URL = Config().get('URL')

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.join(DRIVER_PATH, 'chromedriver.exe'))
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def te1st_baidu_search0(self):
        self.driver.find_element(*self.locator_kw).send_keys('hello world')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def te1st_baidu_search1(self):
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

        file_hander = logging.handlers.TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, 'test1.log'),
                                                                when='s',
                                                                interval=1,
                                                                backupCount=10,
                                                                delay=True,
                                                                encoding='utf-8')
        file_hander.setLevel(logging.INFO)
        file_hander.setFormatter(format_obj)
        logger.addHandler(file_hander)
        return logger

    def readExcel(self):
        datalist = list()
        dataexcel = xlrd.open_workbook(DATA_PATH + '/baidu百度.xlsx')
        sheet1 = dataexcel.sheet_by_name("Sheet1")
        title = sheet1.row_values(0)
        for i in range(1, sheet1.nrows):
            datalist.append(dict(zip(title, sheet1.row_values(i))))
        return datalist

#
# if __name__ == '__main__':
#     # unittest.main()
#     a = TestBaidu1()
#     data = a.readExcel()
#     for d in data:
#         a.subTest(aa=d)
#         a.sub_setUp()
#         a.driver.find_element(*a.locator_kw).send_keys(d['search'])
#         a.driver.find_element(*a.locator_su).click()
#         time.sleep(2)
#         links =a.driver.find_elements(*a.locator_result)
#         for link in links:
#             print(link.text)
#         a.sub_tearDown()
#
#     a = 2
if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试百度搜索', description='修改报告')
        runner.run(TestBaidu('test_search_excel'))
