#!/usr/bin/python3
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from Test_Framework.test.common.Page import Page


class BaiduMainPage(Page):
    loc_search_input = (By.ID, 'kw')
    loc_search_button = (By.ID, 'su')

    def search(self, kw):
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()

