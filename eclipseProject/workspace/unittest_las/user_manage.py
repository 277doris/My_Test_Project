#-*-  coding:utf-8 -*-
'''
Created on 2018年12月4日

@author: 汤文钦
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 
import unittest

class test_product_config(unittest.TestCase):

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
        
        #用户管理
        user_control = element('//*[@id="menu"]/div/ul/li[2]/a')
        user_control.click()
        time.sleep(1)
        #点击用户管理
        user_cont = element('//*[@id="slideBar"]/ul/li[1]/a')
        user_cont.click()
        time.sleep(2)
        current_window = self.driver.current_window_handle
        print(current_window)
        #新建用户
        add_user = element('//*[@id="main"]/div[2]/div/div[1]/div[1]/div[2]/a')
        add_user.click()
        time.sleep(2)
        #选择角色
        role_select = element('//*[@id="roleid"]/div[2]')
        role_select.click()
        role_sp = element('//*[@id="roleid"]/div[1]/label[1]/input')
        role_sp.click()
        #输入账号
        account = element('//*[@id="username1"]')
        account.send_keys("testsp")
        #输入姓名
        name = element('//*[@id="realName"]')
        name.send_keys("自动添加")
        #输入邮箱
        mail = element('//*[@id="userMail"]')
        mail.send_keys('tangwenqin@juxinda360.com')
        #点击保存按钮
        save_button = element('//*[@id="save"]')
        save_button.click()
        time.sleep(2)
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(2)
        #切换至原来页面
        self.driver.switch_to_window(current_window)
        time.sleep(2)
        self.driver.refresh()
        time.sleep(1)
        print("新建账号成功")
        
        #点击角色管理
        user_cont = element('//*[@id="slideBar"]/ul/li[2]/a')
        user_cont.click()
        time.sleep(3)
        #点击新建角色按钮
        add_role = element('//*[@id="main"]/div[2]/div/div/div/div[1]/div[2]/a')
        add_role.click()
        time.sleep(2)
        #角色ID
        role_id = element('//*[@id="roleId"]')
        role_id.send_keys("SPAA")
        #角色昵称
        role_name = element('//*[@id="roleName"]')
        role_name.send_keys("自动添加审批")
        #点击保存按钮
        save_button = element('//*[@id="btnSave"]')
        save_button.click()
        time.sleep(3)
        print("新建角色成功")
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()