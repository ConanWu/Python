# coding=utf-8

from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest
import time

class MyTestYoudao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"

    def test_baidu3(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "selenium_百度搜索")


    def tearDown(self):
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
