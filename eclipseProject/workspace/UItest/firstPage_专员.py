#-*-  coding:utf-8 -*-
import pdb
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from readconfig import ReadConfig

class FirstPage(unittest.TestCase):
    def setUp(self):
        #读取数据文件
        self.data = ReadConfig
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://call.juxinda360.com/#/")  
        self.driver.maximize_window()
        element = self.driver.find_element_by_xpath
        #输入外呼专员——账号和密码进行登录，用户名       
        user_name = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input')
        user_name.send_keys(self.data.get_user("用户名"))
        #打断点
        pdb.set_trace()
#         pwd = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input')
#         pwd.send_keys(self.data.get_Users('UserInfo', '密码'))
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()