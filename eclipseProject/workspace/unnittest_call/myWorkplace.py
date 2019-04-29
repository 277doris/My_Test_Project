#-*-  coding:utf-8 -*-
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_my_workplace(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://call.super.com/#/")  
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #输入外呼专员——账号和密码进行登录，用户名       
        element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input').send_keys("mz")
        element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input').send_keys("111111")
        #点击登录按钮
        login_button = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[3]/div/button')
        login_button.click()
        time.sleep(1)    
        
#         #点击工作台
#         workplace = element('//*[@id="app"]/div/section/section/div/aside/ul/li[1]/div')
#         workplace.click()
#         time.sleep(1)
        #点击外呼专员的工作台管理
        workplace_2 = element('//*[@id="app"]/div/section/section/div/aside/ul/li[1]/ul/li/ul/li[2]')
        workplace_2.click()
        time.sleep(1)
        
        #1、选择外呼状态
        call_status = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[1]/select')
        Select(call_status).select_by_visible_text("有意向")
        #2、输入任务名称
        task_name = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[2]/input')
        task_name.send_keys("蒙牛任务2")
        #3、点击登录密码的icon
        login_pw = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[2]/div[2]/img')
        login_pw.click()
        #4、输入手机号/姓名
        name_search = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[3]/input')
        name_search.send_keys("六")
        #5、点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[3]/button[1]')
        query_button.click()
        time.sleep(2)
        print("工作台——外呼专员工作台——查询客户成功")
        time.sleep(1)
        #6、点击拨打电话按钮
        call_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[2]/table/tr[2]/td[5]/img[1]')
        call_button.click()
        print("工作台——外呼专员工作台——拨打电话成功")
        time.sleep(2)
        
        #7、点击收藏按钮
        collection = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[2]/table/tr[2]/td[6]/img[3]')
        collection.click()
        time.sleep(2)
        #8、清空搜索项
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[3]/button[2]')
        clear_button.click()
        time.sleep(1)
        print("工作台——外呼专员工作台——清空搜索项成功")
        #9、搜索已标记客户
        collect_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[2]/div[3]/button')
        collect_button.click()
        time.sleep(2)
        print("工作台——外呼专员工作台——标记及搜索标记用户成功")
        print("工作台——外呼专员工作台——右边界面测试通过")
        
        #测试工作台左边
        #清空搜索项
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[3]/button[2]')
        clear_button.click()
        #1、输入手机号/姓名
        name_search = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[3]/input')
        name_search.send_keys("六")
        #2、点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[3]/button[1]')
        query_button.click()
        time.sleep(2)
        print("工作台——外呼专员工作台——查询客户成功")
        #3、点击拨打电话按钮
        call_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[2]/table/tr[2]/td[5]/img[1]')
        call_button.click()
        time.sleep(2)
       
        #操作左边数据
        #4、选择外呼状态
        call_status = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/select')
        Select(call_status).select_by_visible_text("有意向")
        #5、选择微信状态
        webchat = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/select')
        Select(webchat).select_by_visible_text("已添加")
        #6、输入外呼备注
        remarks = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[3]/textarea')
        remarks.send_keys("自动添加的外呼备注")
        #7、选择产品话术
        product_introduction = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[4]/div/select')
        Select(product_introduction).select_by_visible_text("酸酸乳")
        #8、选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[5]/div[2]/ul/li/div/div[1]/select')
        Select(loan_product).select_by_visible_text("酸酸乳")
        #9、点击上传图片按钮
        upload_img = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[5]/div[2]/ul/li/div/div[2]/div/div/button')
        upload_img.click()
        time.sleep(3)
        #10、调用上传分机.exe上传程序
        os.system("C:\\Users\\22648\\Desktop\\自动化上传文件\\上传身份证背面.exe")
        time.sleep(2)
        #11、点击保存按钮
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[5]/div[3]/button')
        save_button.click()
        time.sleep(3)
        print("工作台——外呼专员工作台——左边测试通过")
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()