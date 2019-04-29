#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_black_users(unittest.TestCase):
    
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
        
        #点击黑名单管理
        black_us = element('//*[@id="menu"]/div/ul/li[1]/a')
        black_us.click()
        time.sleep(1)
        #点击黑名单管理
        black_uss = element('//*[@id="slideBar"]/ul/li/a')
        black_uss.click()
        time.sleep(1)
        current_window = self.driver.current_window_handle
        #点击新建名单
        add_user = element('//*[@id="main"]/div[2]/div/div[1]/div[1]/div[2]/a')
        add_user.click()
        time.sleep(1)
        #输入姓名
        user_name = element('//*[@id="realName"]')
        user_name.send_keys("这是测试黑名单")
        #输入电话
        tel = element('//*[@id="userTel"]')
        tel.send_keys("13813339278")
        #输入备注信息
        other_info = element('//*[@id="remark"]')
        other_info.send_keys("自动添加备注信息；自动添加备注信息；自动添加备注信息；自动添加备注信息；")
        #点击保存按钮
        save_button = element('//*[@id="save"]')
        save_button.click()
        time.sleep(1)
        #点击dialog中的按钮确定
        yes = element('//*[@id="main"]/div[2]/div/div/div[4]/div/form/div[2]/a[1]')
        yes.click()
        time.sleep(1)
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(2)
        print("新建黑名单成功！")
        self.driver.switch_to_window(current_window)
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)
        
        #点击待移入按钮
        wait_add = element('//*[@id="buttonLists"]/button[3]')
        wait_add.click()
        time.sleep(1)
        #点击第一个案件的备注信息
        other_info = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[5]/span')
        other_info.click()
        time.sleep(2)
        #点击备注信息中的关闭按钮
        close_button = element('//*[@id="main"]/div[2]/div/div[1]/div[4]/div/form/div[1]/div')
        close_button.click()
        #点击第一个案件的编辑按钮
        edit_button = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/a[1]')
        edit_button.click()
        #修改姓名
        edit_name = element('//*[@id="realName"]')
        edit_name.clear()
        time.sleep(1)
        edit_name.send_keys("自动更改姓名")
        #修改电话
        edit_tel = element('//*[@id="userTel"]')
        edit_tel.clear()
        time.sleep(1)
        edit_tel.send_keys("13666666666")
        #修改备注信息
        edit_other_info = element('//*[@id="remark"]')
        edit_other_info.clear()
        time.sleep(1)
        edit_other_info.send_keys("自动测试修改信息！自动测试修改信息！自动测试修改信息！")
        #点击保存按钮
        save_button = element('//*[@id="save"]')
        save_button.click()
        #点击dialog中的按钮确定
        yes = element('//*[@id="main"]/div[2]/div/div/div[4]/div/form/div[2]/a[1]')
        yes.click()
        time.sleep(1)
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(2)
        print("修改黑名单成功！")
        #返回黑名单管理页
        self.driver.switch_to_window(current_window)
        time.sleep(1)
        #点击第一案件的移入按钮
        delete_button = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/a[2]')
        delete_button.click()
        time.sleep(1)
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3)
        print('移入黑名单成功！')
        #在关键字中搜索姓名
        kw = element('//*[@id="search"]')
        kw.send_keys('假测')
        #点击搜索按钮
        query_button = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]')
        query_button.click()
        time.sleep(2)
        print("搜索成功")
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()