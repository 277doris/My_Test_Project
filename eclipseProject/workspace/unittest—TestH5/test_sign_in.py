#  -*-  coding:utf-8 -*-
import unittest
from selenium import webdriver
import time

class test_sign_in(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def test_sign_in(self):
        ####注册新用户
        #self.driver.get("http://h5.super.com/login")
        self.driver.get("http://h5follow.super.cn/login")
        self.driver.set_window_size(480, 800)
        element = self.driver.find_element_by_xpath
        #点击立即注册按钮
        login_in = element("/html/body/div/div/div[3]/a").click()
        #输入手机号
        phone_numb = element("/html/body/div/div/div[1]/ul/li[1]/input")
        phone_numb.send_keys("13070123277")
        #输入图形验证码 
        check_img = element("/html/body/div/div/div[1]/ul/li[2]/input")
        #输入图形验证码
        check_img.send_keys() 
        time.sleep(5)
        #点击并发送短信验证码
        element("/html/body/div/div/div[1]/ul/li[3]/span").click()
        time.sleep(5)
        phone_message = element("/html/body/div/div/div[1]/ul/li[3]/input")
        #输入短信验证码
        phone_message.send_keys()
        time.sleep(15)
        #输入密码
        user_password = element("/html/body/div/div/div[1]/ul/li[4]/input")
        user_password.send_keys("abc1234")
        #确认密码
        confirm_pw = element("/html/body/div/div/div[1]/ul/li[5]/input")
        confirm_pw.send_keys("abc1234")
        #点击注册按钮
        element("/html/body/div/div/div[2]/button").click()
        time.sleep(5)

    def tearDown(self):     
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()