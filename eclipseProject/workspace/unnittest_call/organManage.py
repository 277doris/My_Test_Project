#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_organ_control(unittest.TestCase):
    
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
        
        #点击权限管理
        right_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[5]/div')
        right_manage.click()
        time.sleep(1)
        #点击机构管理
        organ_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[5]/ul/li/ul/li[3]')
        organ_manage.click()
        time.sleep(1)
        
        #1、关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("聚信达")
        #2、选择机构属性
        product_attribute = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/select')
        Select(product_attribute).select_by_visible_text("金融行业")
        #3、点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("权限管理——机构管理——查询机构成功")
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        print("权限管理——机构管理——清空查询项测试通过")
        
        #点击新增按钮
        add_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[3]')
        add_button.click()
        time.sleep(1)
        #1、选择机构属性
        product_attribute = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[1]/div/select')
        Select(product_attribute).select_by_visible_text("其他行业")
        #2、输入机构名称
        organ_name = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[2]/div/div/input')
        organ_name.send_keys("自动测试添加机构")
        #3、输入可建用户数
        create_num = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[3]/div/div/input')
        create_num.send_keys("10")
        #4、输入备注
        remarks = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[4]/div/textarea')
        remarks.send_keys("测试自动添加")
        #5、鼠标滑到最下方点击保存按钮
        create_num = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[3]/div/div/input')
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[5]/div/button[1]')
        ActionChains(self.driver).drag_and_drop(create_num, save_button).perform()
        time.sleep(2)
        #6、点击保存按钮
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[5]/div/button[1]')
        save_button.click()
        time.sleep(1)
        #7、捕获弹框并确定保存
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3) 
        
        #验证并新增机构
        #1、关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("自动测试添加机构")
        #2、点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print('权限管理——机构管理——新增机构成功') 
        #3、点击编辑图标
        edit_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[4]')
        edit_button.click()
        time.sleep(1)
        #4、编辑可建用户数
        create_num = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[3]/div/div/input')
        create_num.clear()
        create_num.send_keys(80)
        #5、鼠标滑到最下方点击保存按钮
        create_num = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[3]/div/div/input')
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[5]/div/button[1]')
        ActionChains(self.driver).drag_and_drop(create_num, save_button).perform()
        time.sleep(2)
        #6、点击保存按钮
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[5]/div/button[1]')
        save_button.click()
        time.sleep(1)
        #7、捕获弹框并确定保存
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3) 
        print("权限管理——机构管理——编辑机构成功")
        time.sleep(2)
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        print("权限管理——机构管理——清空搜索项成功")
        
        
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()