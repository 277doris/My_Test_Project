#  -*-  coding:utf-8 -*-
import unittest
import time
from selenium import webdriver

class test_pay_money(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_pay_money(self):
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
        #点击还款按钮
        pay_moeny = element("/html/body/div/div/div/div[2]/div/ul/li[2]/a/img[1]").click()
        time.sleep(2)
        
        #点击我要展期按钮
        defer = element("/html/body/div/div/div/div[1]/div[2]/div/a[2]/div").click()
        ####
        time.sleep(5)
        
        #点击我的还款计划
        pay_moeny_plan = element("/html/body/div/div/div/div[1]/div[2]/div/a[3]/div").click()
        time.sleep(2)
        #点击我的还款计划中的返回按钮
        pay_back = element("/html/body/div/div/header/img").click()
        time.sleep(5)
        
        #点击我要还款按钮
        pay_all_moeny_all = element("/html/body/div/div/div/div[1]/div[2]/div/a[1]/div").click()
        ####
        time.sleep(5)

    def test_tearDown(self):
         #退出浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()