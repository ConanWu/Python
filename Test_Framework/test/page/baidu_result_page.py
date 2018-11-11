#!usr/bin/python3
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from Test_Framework.test.page.baidu_main_page import BaiduMainPage


class BaiduResultPage(BaiduMainPage):
    loc_result_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)