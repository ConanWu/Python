# coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import *

driver = webdriver.Firefox()
first_url1="https://mail.qq.com/"
driver.get(first_url1)

sleep(5)
driver.switch_to.frame("login_frame")
sleep(5)
driver.find_element_by_id("switcher_plogin").click()
