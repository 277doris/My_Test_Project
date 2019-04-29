'''
Created on 2019年1月16日

@author: 汤文钦
'''
#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
#下拉框操作
from selenium.webdriver.support.select import Select
#测试贷后专员/贷后客服/委外催收   账号：dingone   密码：111111（操作按钮一样）

class tomorrowCase(unittest.TestCase):
 
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

        #点击明日提醒案件
        tomorrow_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[3]')
        tomorrow_case.click()
        time.sleep(2)
        #今日案件——还款状态
        today_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select[1]')
        #选择还款状态——待还款
        Select(today_pay_sta).select_by_visible_text("待还款")
        #今日案件——还款方式
        today_pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select[2]')
        #选择还款方式——系统操作
        Select(today_pay_method).select_by_visible_text("系统操作")
        #今日案件——电话状态
        today_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        #选择电话状态——正常接听
        Select(today_pho_sta).select_by_visible_text("正常接听")
        #今日案件——案件跟进状态
        today_case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择案件跟进状态为——已提醒未回复
        Select(today_case_follow).select_by_visible_text("已提醒未回复")
        #在关键字中输入——汤文钦
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/div/input')
        kw.send_keys("汤文钦")
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/button').click()
        time.sleep(2)
        print("明日提醒案件搜索完毕")

    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
