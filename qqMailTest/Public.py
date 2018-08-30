from time import *

class Login():
    #login
    def user_login(self, driver, username, password, password_indep):
        #driver.find_element_by_link_text("帐号密码登录").click()
        #driver.find_element_by_id("switcher_plogin").click()
        driver.find_element_by_id("u").clear()
        driver.find_element_by_id("u").send_keys(username)
        driver.find_element_by_id("p").clear()
        driver.find_element_by_id("p").send_keys(password)
        driver.find_element_by_id("go").click()
        sleep(5)

        driver.find_element_by_id("pwd").send_keys(password_indep)
        driver.find_element_by_id("submitBtn").click()

    #logout
    def user_logout(self, driver):
        driver.find_element_by_link_text("退出").click()
        #driver.quit()