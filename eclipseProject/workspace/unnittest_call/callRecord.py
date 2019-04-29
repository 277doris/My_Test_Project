#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_record(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://call.super.com/#/")  
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #输入用户名      
        username = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input')
        username.send_keys("admin")
        #输入密码
        pw = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input')
        pw.send_keys("111111")
        #点击登录按钮
        login_button = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[3]/div/button')
        login_button.click()
        time.sleep(1)
        
        #点击外呼管理管理
        out_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[3]/div')
        out_manage.click()
        time.sleep(2)
        
        #点击通话记录
        tel_record = element('//*[@id="app"]/div/section/section/div/aside/ul/li[3]/ul/li/ul/li[1]')
        tel_record.click()
        time.sleep(2)
        #输入姓名/手机号关键字
        keyword = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        keyword.send_keys("汤文钦")
        #输入专员姓名
        worker = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/input')
        worker.send_keys('聚专员')
        
        #选择通话时间
        date1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div/div[1]/input')
        date1.send_keys("2018-12-29 00:00") 
        #点击空白处使时间弹框消失
        blank = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[6]').click()
        time.sleep(1)
        date2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div/div[2]/input')
        date2.send_keys("2019-01-03 00:00")
        blank = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[6]').click()
        #选择通话状态
        tel_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(tel_status).select_by_visible_text("接通")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #获取当前页面的handle
        current_handle = self.driver.current_window_handle
        print(current_handle)
        #点击录音按钮
        tape_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[7]')
        tape_button.click()
        time.sleep(2)
        #跳转回当前句柄
        self.driver.switch_to_window(current_handle)
        time.sleep(2)
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        
        #选择通话状态
        tel_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(tel_status).select_by_visible_text("其它")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("外呼管理——通话记录测试通过！")
    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()