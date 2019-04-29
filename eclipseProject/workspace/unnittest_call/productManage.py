#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_user_control(unittest.TestCase):
    
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
        #点击产品管理
        product_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[5]/ul/li/ul/li[2]')
        product_manage.click()
        time.sleep(1)
        
        #1、关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("8371")
        #2、输入创建的开始时间
        create_time1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[1]/input')
        create_time1.send_keys("2018-12-27")
        #点击空白处使时间控件消失
        blank = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[6]')
        blank.click()
        #输入创建的结束时间
        creat_time2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[2]/input')
        creat_time2.send_keys("2019-1-9")
        #点击空白处使时间控件消失
        blank = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[6]')
        blank.click()
        #3、选择所属机构
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(organ).select_by_visible_text("最后测")
        #4、选择合作方
        partner = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(partner).select_by_visible_text("不知道")
        time.sleep(1)
        #5、选择产品状态
        product_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[5]/select')
        Select(product_status).select_by_visible_text("已生效")
        #6、选择产品类型
        product_type = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[6]/select')
        Select(product_type).select_by_visible_text("外部产品")
        #7、点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("权限管理——产品管理——查询产品成功")
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        print("权限管理——产品管理——清空查询项测试通过")
        
        #点击新增按钮
        add_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[3]')
        add_button.click()
        time.sleep(1)
        #1、输入产品名称
        product_name = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[1]/div/div/input')
        product_name.send_keys("添加产品自动")
        #2、选择所属机构
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[2]/div/select')
        Select(organ).select_by_visible_text("聚信达")
        #3、选择产品类型
        product_type = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[3]/div/select')
        Select(product_type).select_by_visible_text("外部产品")
        #4、选择产品状态
        product_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[4]/div/select')
        Select(product_status).select_by_visible_text("已生效")
        #5、输入合作方
        partner = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[5]/div/div/input')
        partner.send_keys("外部产品")
        #6、输入话术
        product_introduction = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[6]/div/textarea')
        product_introduction.send_keys("这是自动添加的一款产品的话术介绍")
        #7、鼠标滑到最下方点击保存按钮
        partner = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[5]/div/div/input')
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[7]/div/button[1]')
        ActionChains(self.driver).drag_and_drop(partner, save_button).perform()
        time.sleep(2)
        #8、点击保存按钮
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[7]/div/button[1]')
        save_button.click()
        time.sleep(1)
        #9、捕获弹框并确定保存
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3) 
        #10、关键字搜索，验证新创建的用户是否添加成功
        #关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("添加产品自动")
        time.sleep(2)
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("权限管理——产品管理——添加产品成功")
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        
        #编辑操作：
        #1、关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("最后测试1")
        time.sleep(2)
        #2、点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #3、点击编辑按钮
        edit_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[7]')
        edit_button.click()
        time.sleep(1)
        #4、编辑话术
        produce_introduction = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[6]/div/textarea')
        produce_introduction.clear()
        produce_introduction.send_keys('自动化测试')
        #5、鼠标滑到最下方点击保存按钮
        partner = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[5]/div/div/input')
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[7]/div/button[1]')
        ActionChains(self.driver).drag_and_drop(partner, save_button).perform()
        time.sleep(2)
        #6、点击保存按钮
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[7]/div/button[1]')
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
        print('权限管理——产品管理——编辑产品成功')
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()