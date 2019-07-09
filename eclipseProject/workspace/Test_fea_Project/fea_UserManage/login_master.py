#-*-  coding:utf-8 -*-
import unittest
import time
from selenium import webdriver


class Lgin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://fea.super.com/cn/#/")
        self.driver.maximize_window()
        # @unittest.skip(reason) ， 直接跳过被装饰的用例 ，reason用于填写跳过用例的原因

    def test_login(self):
        driver = self.driver
        element = driver.find_element_by_xpath
        username = element("/html/body/div/div/div[2]/div/div/div/form/div[1]/div/div/input")
        username.send_keys("master")
        password = element("/html/body/div/div/div[2]/div/div/div/form/div[2]/div/div/input")
        password.send_keys("111111")
        login = element("/html/body/div/div/div[2]/div/div/div/form/div[3]/div/button")
        login.click()
        time.sleep(2)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()