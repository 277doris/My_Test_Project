#  -*-  coding:utf-8 -*-
import unittest
import time
from selenium import webdriver

class test_Signed(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_sign(self):
        #测试H5登录
        #self.driver.get("http://h5.super.com/login")
        self.driver.get("http://h5follow.super.cn/login")
        self.driver.set_window_size(480, 800)
        #用账号、密码进行登录
        element = self.driver.find_element_by_xpath
        phone_numb = element("//*[@id='tab1']/div/div[1]/div[2]/p/input")
        phone_numb.send_keys("13070123277")
        #请输入密码
        user_password = element("//*[@id='tab1']/div/div[2]/div[2]/p/input")
        user_password.send_keys("abc123")
        #点击登录按钮
        element("//*[@id='showModel']").click()
        time.sleep(2)
        #点击签约按钮
        sign = element("/html/body/div/div/div/div[2]/div/ul/li[3]/a").click()
        time.sleep(2)
        #未签约状态——点击领取现金弹框
        own_money = element("/html/body/div/div/div/div/div/div[4]/button").click()
        time.sleep(2)
 
    def test_tearDown(self):
         #退出浏览器
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()