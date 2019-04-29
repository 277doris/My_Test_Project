#-*-  coding:utf-8 -*-
'''
Created on 2018年12月4日

@author: 汤文钦
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 
import unittest

class test_product_config(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://las.super.com/view/login.html")
        self.driver.maximize_window()        
        element = self.driver.find_element_by_xpath
 
        #输入用户名
        username = element("/html/body/div[2]/div/form/label[1]/div/input") 
        username.send_keys("doris")
        #输入密码
        password = element("/html/body/div[2]/div/form/label[2]/div/input")
        password.send_keys("222222")
        #输入验证码
        check_code = element("/html/body/div[2]/div/form/label[3]/div/input")
        check_code.send_keys("spxt")
        #点击登录按钮
        login = element("/html/body/div[2]/div/form/button")
        login.click()
        time.sleep(2)       
        
        #点击配置中心
        config_center = element('//*[@id="menu"]/div/ul/li[3]/a')
        config_center.click()
        time.sleep(1)
        #点击产品配置
        product_config = element('//*[@id="slideBar"]/ul/li[1]/a')
        product_config.click()
        time.sleep(2)
        #点击机构配置
        organization_config = element('//*[@id="slideBar"]/ul/li[2]/a')
        organization_config.click()
        time.sleep(2)
        #点击流程配置
        process_config = element('//*[@id="slideBar"]/ul/li[3]/a')
        process_config.click()
        time.sleep(2)
        #点击数据配置
        data_config = element('//*[@id="slideBar"]/ul/li[4]/a')
        data_config.click()
        time.sleep(2)
        
        
        
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()