#-*-  coding:utf-8 -*-
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains 


class test_record(unittest.TestCase):
    
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
        
        #点击外呼管理管理
        out_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[3]/div')
        out_manage.click()
        time.sleep(2)
        
        #点击分配分机
        dis_tel = element('//*[@id="app"]/div/section/section/div/aside/ul/li[3]/ul/li/ul/li[2]')
        dis_tel.click()
        time.sleep(2)
        #选择分配时间
        dis_time1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/div/div[1]/input')
        dis_time1.send_keys("2018-12-27") 
        #点击空白处使时间弹框消失
        element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[5]').click()
        time.sleep(1)
        dis_time2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/input')
        dis_time2.send_keys("2018-12-27") 
        #点击空白处使时间弹框消失
        element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[5]').click()
        #选择分配状态
        dis_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/select')
        Select(dis_status).select_by_visible_text("已分配")
        #选择发放机构
        dis_organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(dis_organ).select_by_visible_text("测试")
        #选择使用状态
        use_stat = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(use_stat).select_by_visible_text("已使用")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("外呼管理——分配分机——查询分机成功")
       
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        
        #1、查看要分配机构的现有数量——选择发放机构
        dis_organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(dis_organ).select_by_visible_text("测试")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #将鼠标从查询按钮滑到分页按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        page_set = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/span[2]/div/input')
        #执行拖放操作，显示分配是否成功
        ActionChains(self.driver).drag_and_drop(query_button, page_set).perform()
        time.sleep(2)
        #2、点击分配按钮，分配给相应机构
        distribute_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/div/div[4]')
        distribute_button.click()
        time.sleep(1)
        #选择发放机构
        dis_organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/select')
        Select(dis_organ).select_by_visible_text("测试")
        #输入分配数量
        dis_num = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/input')
        dis_num.send_keys("2")
        #点击提交按钮
        submit_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/div[3]/button')
        submit_button.click()
        time.sleep(2)
        #3、测试发放分机是否成功——选择发放机构
        dis_organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(dis_organ).select_by_visible_text("测试")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #将鼠标从查询按钮滑到分页按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        page_set = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/span[2]/div/input')
        #执行拖放操作，显示分配是否成功
        ActionChains(self.driver).drag_and_drop(query_button, page_set).perform()
        time.sleep(2)
        print("外呼管理——分配分机——分配成功")
        
        #点击上传按钮
        upload = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/div/div[3]')
        upload.click()
        time.sleep(2)
        #点击上传按钮
        up_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/img')
        up_button.click()
        time.sleep(1)
        #调用上传分机.exe上传程序
        os.system("C:\\Users\\22648\\Desktop\\自动化上传文件\\上传分机.exe")
        time.sleep(2)
        #点击提交按钮
        submit_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/div[2]/button[2]')
        submit_button.click()
        time.sleep(3)
        print("外呼管理——分配分机——上传分机成功")
    
        print("外呼管理——分配分机测试通过！")
    
    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()