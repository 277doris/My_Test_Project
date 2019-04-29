#  -*-  coding:utf-8 -*-
import unittest
import time
from selenium import webdriver

class test_Change_password_in(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()   
    def test_Change_password(self):
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
        #点击我的按钮
        my = element("/html/body/div/div/div/div[2]/div/ul/li[4]/a").click()
        time.sleep(2)
        #点击修改密码按钮
        change_card = element("/html/body/div/div/div/div[1]/div[2]/a[1]/div").click()
        time.sleep(2)
        #点击输入原密码按钮
        old_pw = element("/html/body/div/div/div[1]/div[1]/div[2]/p/input")
        old_pw.send_keys("abc123")
        #点击输入新密码
        new_pw = element("/html/body/div/div/div[1]/div[2]/div[2]/p/input")
        new_pw.send_keys("abc123")
        #点击再次输入新密码
        confirm_pw = element("/html/body/div/div/div[1]/div[3]/div[2]/p/input")
        confirm_pw.send_keys("abc123")
        #点击确定按钮
        element("/html/body/div/div/button").click()
 
    def test_tearDown(self):
        #退出浏览器
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()