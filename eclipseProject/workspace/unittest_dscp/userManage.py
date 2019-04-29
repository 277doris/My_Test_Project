
# '''
#  Created on 2019年1月21日
#  
#  @author: 汤文钦
# '''
# *-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
#操作下拉框
from selenium.webdriver.support.select import Select

class users_manage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://dscp.super.com/#/")
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #登录超级管理员     admin   111111
        #输入账号
        username = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input")
        username.send_keys("admin")
        pw = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/input")
        pw.send_keys("111111")
        #输入验证码
        check_code = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/input")
        check_code.send_keys("dscp")
        #点击登录密码
        login = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[4]/div/button")
        login.click()
        time.sleep(3)
        
        #点击用户管理
        user_control = element('//*[@id="app"]/div/div[1]/div[2]/ul/li[3]')
        user_control.click()
        time.sleep(1)
        #点击新建用户
        add_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div/button')
        add_user.click()
        time.sleep(1)
        #新建用户——催收专员
        new_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/input')
        new_user.send_keys("cuishouZY")
        #新建用户——姓名
        new_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/input')
        new_name.send_keys('自动添加催收')  
        #新建用户——手机号
        new_tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        new_tel.send_keys("13313331333")
        #新建用户——密码
        new_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        new_pw.send_keys("111111")
        #新建用户——确认密码
        comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        comfirm_pw.send_keys('111111')
        #新建用户——选择岗位
        position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #新建用户——选择岗位
        Select(position).select_by_visible_text("委外催收")
        #新建用户——选择产品
        checkbox1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[1]/span[1]/span')
        checkbox1.click()
        checkbox2 =element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[2]/span[1]/span')
        checkbox2.click()
        checkbox3 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[3]/span[1]/span')
        checkbox3.click()
        time.sleep(1)
        #点击创建按钮
        create_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        create_button.click()
        time.sleep(1)
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3)
        print('用户管理——新建委外催收成功')
        
        #编辑第一个账号
        edit_first = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[6]/span/span[1]')
        edit_first.click()
        time.sleep(1)
        #编辑手机号
        edit_phone = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        edit_phone.clear()
        edit_phone.send_keys('13313333333')
        #编辑密码
        edit_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        edit_pw.clear()
        edit_pw.send_keys('111111')
        #编辑——确认密码
        edit_comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        edit_comfirm_pw.clear()
        edit_comfirm_pw.send_keys('111111')
        #编辑岗位
        edit_position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #编辑岗位为贷后专员
        Select(edit_position).select_by_visible_text("贷后专员")
        #选择直属领导
        immediate_boss = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/select')
        time.sleep(1)
        #选择直属领导为三个产品贷管
        Select(immediate_boss).select_by_visible_text("一个产品贷管")
        time.sleep(2)
        #点击修改按钮
        edit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        edit_button.click()
        time.sleep(1)
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3)
        print('用户管理——编辑账号成功')
        
        #删除账号——aaa
        delect_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[5]/td[6]/span/span[2]')
        delect_user.click()
        time.sleep(5)
        print('用户管理——删除账号成功')
        
        #新建用户——贷后主管
        new_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/input')
        new_user.send_keys("daihouZG")
        #新建用户——姓名
        new_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/input')
        new_name.send_keys("测试自动添加贷后主管")       
        #新建用户——手机号
        new_tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        new_tel.send_keys("13313331333")
        #新建用户——密码
        new_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        new_pw.send_keys("111111")
        #新建用户——确认密码
        comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        comfirm_pw.send_keys('111111')
        #新建用户——选择岗位
        position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #新建用户——选择岗位
        Select(position).select_by_visible_text("贷后主管")
        #新建用户——选择产品
        checkbox1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[1]/span[1]/span')
        checkbox1.click()
        checkbox2 =element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[2]/span[1]/span')
        checkbox2.click()
        checkbox3 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/div/label[3]/span[1]/span')
        checkbox3.click()
        time.sleep(1)
        #点击创建按钮
        create_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        create_button.click()
        time.sleep(1)
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3)
        print('用户管理——新建贷后主管成功')
        
        #新建用户——贷后专员
        new_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/input')
        new_user.send_keys("daihouZY")
        #新建用户——姓名
        new_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/input')
        new_name.send_keys("测试自动添加贷后专员")    
        #新建用户——手机号
        new_tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        new_tel.send_keys("13313331333")
        #新建用户——密码
        new_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        new_pw.send_keys("111111")
        #新建用户——确认密码
        comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        comfirm_pw.send_keys('111111')
        #新建用户——选择岗位
        position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #新建用户——选择岗位
        Select(position).select_by_visible_text("贷后专员")
        #选择直属领导
        immediate_boss = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/select')
        Select(immediate_boss).select_by_visible_text("两个产品贷管")
        time.sleep(1)
        #点击创建按钮
        create_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        create_button.click()
        time.sleep(1)
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3)
        print('用户管理——新建贷后专员成功')
        
        #新建用户——贷后客服
        new_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/input')
        new_user.send_keys("daihouKF")
        #新建用户——姓名
        new_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/input')
        new_name.send_keys("测试自动添加贷后客服")   
        #新建用户——手机号
        new_tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input')
        new_tel.send_keys("13313331333")
        #新建用户——密码
        new_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input')
        new_pw.send_keys("111111")
        #新建用户——确认密码
        comfirm_pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input')
        comfirm_pw.send_keys('111111')
        #新建用户——选择岗位
        position = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/select')
        #新建用户——选择岗位
        Select(position).select_by_visible_text("贷后客服")
        #选择直属领导
        immediate_boss = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/select')
        Select(immediate_boss).select_by_visible_text("两个产品贷管")
        time.sleep(1)
        #点击创建按钮
        create_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/button[1]')
        create_button.click()
        time.sleep(1)
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3)
        print('用户管理——新建贷后客服成功')
    
    def test_tearDown(self):
        #退出浏览器
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()