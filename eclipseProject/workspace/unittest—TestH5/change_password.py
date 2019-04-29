#  -*-  coding:utf-8 -*-
import unittest
from selenium import webdriver
import time

class test_change_password(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_chang_pw(self):
        #self.driver.get("http://h5.super.com/login")
        self.driver.get("http://h5follow.super.cn/login")
        self.driver.set_window_size(480, 800)
        element = self.driver.find_element_by_xpath
        #点击忘记密码按钮
        element('/html/body/div/div/a/span').click()
        time.sleep(2)
        #输入手机号
        phone_numb = element('/html/body/div/div/div[1]/div[1]/div[2]/p/input')
        phone_numb.send_keys("13070123277")
        time.sleep(2)
        #输入图形验证码
        check_img = element("/html/body/div/div/div[1]/div[2]/div[2]/p/input").click()
        time.sleep(5)
        #点击发送短信验证码按钮
        element("/html/body/div/div/div[1]/div[3]/p/span").click()
        time.sleep(2)
        #输入短信验证码
        phone_message = element("/html/body/div/div/div[1]/div[3]/div[2]/p/input")
        phone_message.send_keys("8674")
        time.sleep(10)
        #点击下一步按钮
        element("/html/body/div/div/button").click()
        time.sleep(2)
        #输入密码
        user_password = element('/html/body/div/div/div[1]/div[1]/div[2]/p/input')
        user_password.send_keys("abc123")
        #确定密码
        confirm_pw = element('/html/body/div/div/div[1]/div[2]/div[2]/p/input')
        confirm_pw.send_keys("abc123")
        #点击下一步按钮
        element('/html/body/div/div/button').click()
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()