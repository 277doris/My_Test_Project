'''
Created on 2019年1月15日

@author: 汤文钦
'''
#-*-  coding:utf-8 -*-

import time
import unittest
from selenium import webdriver
#操作下拉框
from selenium.webdriver.support.select import Select

class bothcase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://dscp.super.com/#/")
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #登录贷后主管     daihouZG   111111
        #输入账号
        username = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input")
        username.send_keys("daihouZG")
        pw = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/input")
        pw.send_keys("111111")
        #输入验证码
        check_code = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/input")
        check_code.send_keys("dscp")
        #点击登录密码
        login = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[4]/div/button")
        login.click()
        time.sleep(3)
        
        #点击案件管理
        Case_Manage = element('//*[@id="app"]/div/div[1]/div[2]/ul/li[2]')
        Case_Manage.click()
        time.sleep(2)
        #点击所有案件
        both_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        both_case.click()
        time.sleep(1)
        #输入放款日期
        loan_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/input')
        loan_data1.send_keys('2018-12-30')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        loan_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
        loan_data2.send_keys('2019-01-22')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        time.sleep(1)
        #输入应还款日期
        repay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[1]/input')
        repay_data1.send_keys('2019-01-1')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        repay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[2]/input')
        repay_data2.send_keys('2019-01-22')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        time.sleep(1)
#         #输入实际回款日期
#         real_pay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/input')
#         real_pay_data1.send_keys('2019-01-18')
#         element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
#         real_pay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/input')
#         real_pay_data2.send_keys('2019-01-20')
#         element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
#         time.sleep(1)
        #选择还款状态
        loan_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        Select(loan_status).select_by_visible_text('逾期')
        time.sleep(1)
        #选择负责人
        charge = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        Select(charge).select_by_visible_text('秒借委外')
        time.sleep(1)
        #关键字搜索
        kw_search = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw_search.send_keys('张37')
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button')
        search_button.click()
        time.sleep(1)
        print('案件管理——所有案件查询成功')
        
    def test_tearDown(self):
        #退出浏览器
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
        