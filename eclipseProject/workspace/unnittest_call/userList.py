#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_user_list(unittest.TestCase):
    
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
        
        #点击客户管理
        custom_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[4]/div')
        custom_manage.click()
        time.sleep(1)
        #点击客户列表
        user_list = element('//*[@id="app"]/div/section/section/div/aside/ul/li[4]/ul/li/ul/li[2]')
        user_list.click()
        time.sleep(1)
        #关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("汤")
        #输入添加的开始时间
        create_time1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[1]/input')
        create_time1.send_keys('2018-12-28 00:00')
        time.sleep(1)
        #点击空白处使时间弹框消失
        blank_place = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[5]')
        blank_place.click()
        time.sleep(1)
        #输入添加的结束时间
        create_time2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[2]/input')
        create_time2.send_keys('2019-01-01 00:00')
        time.sleep(1)
        #点击空白处使时间弹框消失
        blank_place = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[5]')
        blank_place.click()
        time.sleep(1)
        #选择放款状态
        loan_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(loan_status).select_by_visible_text("已放款")
        #输入任务名称
        task_name = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/input')
        task_name.send_keys("内部测试")
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[5]/select')
        Select(loan_product).select_by_visible_text("聚信达外部产品")
        #选择通话状态
        call_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[6]/select')
        Select(call_status).select_by_visible_text("有意向")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("客户管理——客户列表——查询客户成功")
        
        #查看放款
        #点击放款图标
        loan_img = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[8]')
        loan_img.click()
        time.sleep(2)
        #关闭放款页面图标
        close_button =element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[1]/div[2]/img')
        close_button.click()
        time.sleep(2)
        print("客户管理——客户列表——查看放款成功")
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        print("客户管理——客户列表测试通过")
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()