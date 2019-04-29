#  -*-  coding:utf-8 -*-
import unittest
from selenium import webdriver
class test_pw(unittest.TestCase):
    #初始化webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        
    def test_login(self):
        #测试H5登录
        self.driver.get("http://h5.super.com/login")
        #用账号、密码进行登录
        element = self.driver.find_element_by_xpath
        phone_numb = element("//*[@id='tab1']/div/div[1]/div[2]/p/input")
        phone_numb.send_keys("13070123277")
        #请输入密码
        user_password = element("//*[@id='tab1']/div/div[2]/div[2]/p/input")
        user_password.send_keys("abc123")
        #点击登录按钮
        element("//*[@id='showModel']").click()
    
    def test_tearDown(self):
        #退出浏览器
        self.driver.quit()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()