'''
Created on 2019年1月22日

@author: 汤文钦
'''
#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
#下拉框操作
from selenium.webdriver.support.select import Select
#测试贷后专员/贷后客服/委外催收   账号：dingone   密码：111111（操作按钮一样）

class allcase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://dscp.super.com/#/")
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #测试委外/贷后专员账号：dingone   111111
        #输入用户名      
        username = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input")
        username.send_keys("dingone")
        #输入密码
        pw = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/input")
        pw.send_keys("111111")
        #输入验证码
        check_code = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/input")
        check_code.send_keys("dscp")
        #点击登录
        login = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[4]/div/button")
        login.click()
        time.sleep(3)
        print("登录成功")
        
        #点击逾期案件
        overdue = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[4]')
        overdue.click()
        time.sleep(2)
        #输入应还款日期
        repay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/input')
        repay_data1.send_keys('2019-01-10')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        repay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
        repay_data2.send_keys('2019-01-12')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        time.sleep(1)
        #逾期案件——还款状态
        overdue_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        #选择还款状态——逾期
        Select(overdue_pay_sta).select_by_visible_text("逾期")
        #逾期案件——电话状态
        overdue_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择电话状态——无人接听
        Select(overdue_pho_sta).select_by_visible_text("请选择")
        #逾期案件——案件跟进状态
        overdue_case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #选择案件跟进状态为——已提醒未回复
        Select(overdue_case_follow).select_by_visible_text("请选择")
        #在关键字中输入——汤文钦
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw.send_keys("张4")
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button').click()
        time.sleep(2)
        print('逾期案件搜索完毕')
        print('贷后专员——我的工作台测试通过')
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
        
        