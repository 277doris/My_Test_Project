#  -*-  coding:utf-8 -*-
import unittest
import time
from selenium import webdriver

class test_Change_Bank_Card(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_Change_card(self):
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
        #点击更改绑定银行卡按钮
        change_card = element("/html/body/div/div/div/div[1]/div[2]/a[3]/div").click()
        time.sleep(2)
        New_card = element("/html/body/div/div/div[2]/div[1]/div[2]/input")
        #清空银行卡号
        New_card.clear()
        #输入银行卡号
        New_card.send_keys("6228480018865092375")
        #点击绑定银行卡按钮
        time.sleep(5)
        element("/html/body/div/div/div[2]/p/button").click()
 
    def test_tearDown(self):
        #退出浏览器
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()