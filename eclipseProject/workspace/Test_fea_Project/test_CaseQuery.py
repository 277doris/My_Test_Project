#  -*-  coding:utf-8 -*-
import unittest
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver

class test_CaseQuery(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://fea.super.com/#/")
        self.driver.maximize_window()        
        element = self.driver.find_element_by_xpath
        
        #输入用户名
        username = element("/html/body/div/div/div[2]/div/div/div/form/div[1]/div/div/input") 
        username.send_keys("master")
        #输入密码
        password = element("/html/body/div/div/div[2]/div/div/div/form/div[2]/div/div/input")
        password.send_keys("111111")
        #点击登录按钮
        login = element("/html/body/div/div/div[2]/div/div/div/form/div[3]/div/button")
        login.click()
        time.sleep(2)       

        #案件查询页面
        case_query = element("/html/body/div/div/div[1]/ul/li[2]")
        case_query.click()
        #点击基础案件查询
        basic_case = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span")
        basic_case.click()
        #点击关键字搜索，输入姓名
        keyword_query1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/input")
        keyword_query1.send_keys("候云飞")
        #点击搜索按钮
        search_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/button")
        search_button1.click()
        time.sleep(2)
        #点击查看按钮
        view_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[4]/span")
        view_button.click()
        time.sleep(2)

        #####点击高级案件查询
        advance_case = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]")
        advance_case.click()
        #点击关键字搜索，输入姓名
        keyword_query2 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/input")
        keyword_query2.send_keys("张三")
        #点击搜索按钮
        search_button2 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/button")
        search_button2.click()
        time.sleep(2)
    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()