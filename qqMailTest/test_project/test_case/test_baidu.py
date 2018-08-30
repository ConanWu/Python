# coding=utf-8

from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest
import time

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        # self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(30)
        # self.base_url = "https://www.baidu.com/"
        # self.verificationErrors = []
        # self.accept_next_alert = True

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "unittest_百度搜索")
        # driver = self.driver
        # driver.get("https://www.baidu.com")
        # driver.find_element_by_id("kw").clear()
        # driver.find_element_by_id("kw").send_keys("selenium")
        # driver.find_element_by_id("su").click()
        # for i in range(60):
        #     try:
        #         if u"selenium_百度搜索" == driver.title: break
        #     except: pass
        #     time.sleep(1)
        # else: self.fail("time out")
        # try: self.assertEqual(u"selenium_百度搜索", driver.title)
        # except AssertionError as e: self.verificationErrors.append(str(e))

    def test_baidu2(self):
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
