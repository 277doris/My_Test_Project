#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_detail_report(unittest.TestCase):
    
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
        
        #点击报表管理
        report_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[2]/div')
        report_manage.click()
        time.sleep(2)
        
        #点击坐席话务报表
        zuoxi = element('//*[@id="app"]/div/section/section/div/aside/ul/li[2]/ul/li/ul/li[1]')
        zuoxi.click()
        time.sleep(2)
        #输入姓名/手机号关键字
        keyword = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        keyword.send_keys("专员董b")
        #选择日期
        date1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[1]/input')
        date1.send_keys("2018-12-28")
        #点击日期处使日期弹框消失
        date = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[1]')
        date.click()
        date2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[2]/input')
        date2.send_keys("2018-12-29")
        date = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[1]')
        date.click()
        #选择机构
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(organ).select_by_visible_text("最后测")
        #选择排序——降序desc，升序asc
        order_by = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(order_by).select_by_visible_text("转化率高到低")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("报表管理——坐席话务报表——查询排序完成")
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(1)
        #点击导出按钮
        export_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[3]')
        export_button.click()
        time.sleep(2)
        print("报表管理——坐席话务报表——导出成功")
        #选择机构
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(organ).select_by_visible_text("聚信达")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #查看下款数
        loan_num = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[8]/td[5]/img')
        loan_num.click()
        time.sleep(2)
        #点击下款详情的关闭按钮
        close_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[1]/div[2]/img')
        close_button.click()
        time.sleep(2)
        print("报表管理——坐席话务报表——查看下款详情通过")
        print("报表管理——坐席话务报表测试通过！")
    
    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()