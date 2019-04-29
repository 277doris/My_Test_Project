#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_product_approval(unittest.TestCase):
    
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
        
        #点击审核结果
        case_result = element('//*[@id="slideBar"]/ul/li[3]/a')
        case_result.click()
        time.sleep(1)
        #选择产品
        product = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select')
        Select(product).select_by_visible_text("聚信达产品")
        time.sleep(2)
        #选择审核结果
        case_result = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/select')
        Select(case_result).select_by_visible_text("审核通过")
        time.sleep(1)
        #选择来源
        source = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[5]/td[2]/select')
        Select(source).select_by_visible_text("助力钱包")
        time.sleep(1)
        #关键字搜索
        kw = element('//*[@id="search"]')
        kw.send_keys("李骢")
        time.sleep(1)
        #点击查询按钮
        query_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[7]/td[2]/div[1]')
        query_button.click()
        time.sleep(2)
        print("搜素案件成功")
        #点击查看按钮
        view_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[10]')
        view_button.click()
        time.sleep(1)
        #从详细信息滑动至返回按钮
        detail_info = element('//*[@id="detailInfo2"]/div')
        back_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/a')
        ActionChains(self.driver).drag_and_drop(detail_info, back_button).perform()
        time.sleep(1)
        #点击返回按钮
        back_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/a')
        back_button.click()
        print("查看成功")
        #点击全量导出按钮
        all_export = element('//*[@id="tableHD"]/button')
        all_export.click()
        time.sleep(3)
        print("全量导出成功")
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()