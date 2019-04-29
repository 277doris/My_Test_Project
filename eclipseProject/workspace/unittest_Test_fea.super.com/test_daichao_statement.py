#-*-  coding:utf-8 -*-
import unittest
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver

class test_daichao_statement(unittest.TestCase):
    
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

        #点击贷超报表
        statement_daichao = element("/html/body/div/div/div[1]/ul/li[3]")
        statement_daichao.click()
        #点击CPA机构报表
        CPA_statement = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span")
        CPA_statement.click()
        time.sleep(2)
        #点击平台名称——第二个
        platform_name1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[2]')
        platform_name1.click()
        time.sleep(5)
        # 开始位置：定位到元素的原位置
        source = element("/html/body/div/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[1]")
        # 结束位置：定位到元素要移动到的目标位置
        target = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/table/tr[2]/td[1]")
        # 执行元素的拖放操作
        ActionChains(self.driver).drag_and_drop(source,target).perform()
        time.sleep(3)
        
        #点击CPC机构报表
        CPC_statement = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/span")
        CPC_statement.click()
        time.sleep(2)
        #点击平台名称——第三个
        platform_name2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[3]')
        platform_name2.click()
        time.sleep(3)
        # 开始位置：定位到元素的原位置
        source = element("/html/body/div/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[1]")
        # 结束位置：定位到元素要移动到的目标位置
        target = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/table/tr[2]/td[1]")
        # 执行元素的拖放操作
        ActionChains(self.driver).drag_and_drop(source,target).perform()
        time.sleep(3)
        
        #点击CPS机构报表
        CPS_statement = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[3]")
        CPS_statement.click()
        time.sleep(2)
        #点击平台名称——第四个
        platform_name3 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[4]')
        platform_name3.click()
        time.sleep(3)
        # 开始位置：定位到元素的原位置
        source = element("/html/body/div/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[1]")
        # 结束位置：定位到元素要移动到的目标位置
        target = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/table/tr[2]/td[1]")
        # 执行元素的拖放操作
        ActionChains(self.driver).drag_and_drop(source,target).perform()
        time.sleep(3)
    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()