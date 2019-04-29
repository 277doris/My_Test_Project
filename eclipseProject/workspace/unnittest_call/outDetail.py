#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_out_detail(unittest.TestCase):
    
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
        
        #点击外呼详情报表
        detail_report = element('//*[@id="app"]/div/section/section/div/aside/ul/li[2]/ul/li/ul/li[2]')
        detail_report.click()
        time.sleep(2)
        #输入姓名/手机号关键字
        keyword = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        keyword.send_keys("汤文钦")
        #输入任务名称
        task_name = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/input')
        task_name.send_keys('内部测试')
        #选择日期
        date1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div[1]/input')
        date1.send_keys("2018-12-28")
        date2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div[2]/input')
        date2.send_keys("2018-12-29")
        #选择放款状态
        loan_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(loan_status).select_by_visible_text("已放款")
        #选择机构角色
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[5]/select[1]')
        Select(organ).select_by_visible_text("聚信达")
        role = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[5]/select[2]')
        Select(role).select_by_visible_text("聚专员")
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[6]/select')
        Select(loan_product).select_by_visible_text("超享借")
        #选择审核状态
        audit_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[7]/select')
        Select(audit_status).select_by_visible_text("审批通过")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        
        #点击导出按钮
        export_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[3]')
        export_button.click()
        time.sleep(2)
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(3)
        
        #选择放款状态
        loan_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(loan_status).select_by_visible_text("已放款")
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[6]/select')
        Select(loan_product).select_by_visible_text("聚信达外部产品")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #点击查看按钮
        view_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[9]/span')
        view_button.click()
        time.sleep(2)
        #点击返回按钮
        back_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[1]/div[2]')
        back_button.click()
        time.sleep(2)
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(3)
        
        print("报表管理——外呼详情报表测试通过！")
    
    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()