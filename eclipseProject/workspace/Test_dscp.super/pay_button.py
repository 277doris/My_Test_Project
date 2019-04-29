#-*-  coding:utf-8 -*-
import os
import time
import unittest
from selenium import webdriver
#弹框操作
from selenium.webdriver.common.alert import Alert
#下拉框操作
from selenium.webdriver.support.select import Select
#模拟鼠标操作
from selenium.webdriver.common.action_chains import ActionChains 

class Workplace(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
    
    def test_myworkplace(self):
        self.driver.get("http://dscp.super.com/#/")
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #测试委外/贷后专员账号：dingone   111111
        #输入用户名      
        username = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input")
        username.send_keys("dingtwo")
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
        
        #点击还款按钮
        pay_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[10]/span[3]')
        pay_button.click()
        time.sleep(1)
        #还款金额
        account = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[1]/input')
        account.send_keys('200')
        #选择还款类型
        pay_type = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[1]/select')
        Select(pay_type).select_by_visible_text('部分还款')
        #选择还款方式
        pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/select')
        Select(pay_method).select_by_visible_text('微信转账')
        #输入提现银行卡
        bank_cd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/input')
        bank_cd.send_keys('ICBC1234567890')
        #输入备注
        marked = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[3]/textarea')
        marked.send_keys('这是一条自动输入的备注信息')
        #点击上传图片按钮
        upload = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[3]/div/ul/li[1]/div/div/div')
        upload.click()
        #调用上传分机.exe上传程序
        os.system("C:\\Users\\22648\\Desktop\\自动化上传文件\\贷后上传还款图片.exe")
        time.sleep(2)
        #模拟鼠标滑动
        target1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[3]/div/ul/li[1]/div/div/div')
        target2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[4]/button[2]')
        ActionChains(self.driver).drag_and_drop(target1, target2).perform()
        time.sleep(1)
        #点击提交按钮
        submit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[4]/button[2]')
        submit_button.click()
        time.sleep(3)
        #对弹框进行操作
        dig_alert = self.driver.switch_to_alert()
        print(dig_alert)
        time.sleep(1)
        dig_alert.accept()
        time.sleep(1)
        def test_tearDown(self):
            #关闭浏览器
            self.driver.quit()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
        