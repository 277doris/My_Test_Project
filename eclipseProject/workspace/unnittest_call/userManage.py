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
        #点击客户管理
        user_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[5]/ul/li/ul/li[1]')
        user_manage.click()
        time.sleep(1)
        #关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("j")
        #选择机构
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/select[1]')
        Select(organ).select_by_visible_text("聚信达")
        #选择角色
        role = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/select[2]')
        Select(role).select_by_visible_text("机构管理员")
        time.sleep(1)
        
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("权限管理——用户管理——查询用户成功")
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        print("权限管理——用户管理——清空查询项测试通过")
        
        #点击新增按钮
        add_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[3]')
        add_button.click()
        time.sleep(1)
        #1、输入用户名
        user_name = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[1]/div/div/input')
        user_name.send_keys("testa3")
        #2、输入真实姓名
        real_name = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[2]/div/div/input')
        real_name.send_keys("自动测试主管")
        #3、输入邮箱
        email_address = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[3]/div/div/input')
        email_address.send_keys("tangwenqin@juxinda360.com")
        #4、选择所属机构
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[4]/div/select')
        Select(organ).select_by_visible_text("聚信达")
        #5、选择角色
        role = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[5]/div/select')
        Select(role).select_by_visible_text("外呼主管")
        #6、选择上级
        leader = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[6]/div/select')
        Select(leader).select_by_visible_text("聚信达机构管理员")
        #7、输入备注
        remarks = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[7]/div/textarea')
        remarks.send_keys("用selenium+python自动添加构管理员")
        #8、鼠标滑到最下方点击保存按钮
        leader = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[6]/div/select')
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[8]/div/button[1]')
        ActionChains(self.driver).drag_and_drop(leader, save_button).perform()
        time.sleep(1)
        #9、点击保存按钮
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[8]/div/button[1]')
        save_button.click()
        time.sleep(1)
        #10、捕获弹框并确定保存
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(3) 
        #11、关键字搜索，验证新创建的用户是否添加成功
        #关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("testa3")
        time.sleep(2)
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("权限管理——用户管理——添加用户成功")
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        
        #点击转移按钮
        change_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[4]')
        change_button.click()
        time.sleep(2)
        
        #编辑操作：
        #1、关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("testa1")
        time.sleep(2)
        #2、点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #3、点击编辑按钮
        edit_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[7]/img[2]')
        edit_button.click()
        time.sleep(1)
        #4、编辑邮箱
        email_address = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[7]/div/textarea')
        email_address.clear()
        email_address.send_keys('2264866101@qq.com')
        #5、编辑备注
        remarks = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[7]/div/textarea')
        remarks.clear()
        remarks.send_keys('自动化测试')
        #6、滑到底部
        leader = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[6]/div/select')
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[8]/div/button[1]')
        ActionChains(self.driver).drag_and_drop(leader, save_button).perform()
        time.sleep(1)
        #7、点击保存按钮
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/form/div[8]/div/button[1]')
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
        print('权限管理——用户管理——编辑用户成功')
        
        #点击重新发送邮件按钮
        remail = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[7]/img[1]')
        remail.click()
        time.sleep(2)
        print("权限管理——用户管理——重新发送邮件成功")
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()