#  -*-  coding:utf-8 -*-
import unittest
from selenium import webdriver
import time
# 
class test_quick_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
         
    def test_quick_log(self):
        #登录H5系统
        #self.driver.get("http://h5.super.com/login")
        self.driver.get("http://h5follow.super.cn/login")
        self.driver.set_window_size(480, 800)
        element = self.driver.find_element_by_xpath
        #点击快速登录
        quick_login = element("/html/body/div/div/div[2]/div[1]/div[2]/div")
        quick_login.click()
        #输入手机号
        phone_numb = element("/html/body/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/p/input")
        phone_numb.click()
        phone_numb.send_keys("13070123277")
        #输入图形验证码
        check_img = element("/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/p[1]/input")
        check_img.click()
        time.sleep(5)
        #点击并输入短信验证码
        phone_message_c = element("/html/body/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/p[2]/span")
        phone_message_c.click()
        time.sleep(10)
        phone_message = element("/html/body/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/p[1]/input")
        phone_message.send_keys("8624")
        time.sleep(5)
        #点击确定按钮
        element("/html/body/div/div/div[2]/div[2]/div[2]/button").click()
        time.sleep(5)   
    def tearDown(self):
        self.driver.quit()
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
  
