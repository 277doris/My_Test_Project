'''
Created on 2019年1月15日

@author: 汤文钦
'''
#-*-  coding:utf-8 -*-
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select

#测试准备：汤，13070123277未收藏

class test_my_workplace(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://call.super.com/#/")  
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #输入用户名      
        username = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input')
        username.send_keys("j3")
        #输入密码
        pw = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input')
        pw.send_keys("111111")
        #点击登录按钮
        login_button = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[3]/div/button')
        login_button.click()
        time.sleep(1)
        print("登录外呼专员成功")
        #一、点击工作台
        #一、1点击工作台——首页
        first_page = element('//*[@id="app"]/div/section/section/div/aside/ul/li[1]/ul/li/ul/li')
        first_page.click()
        time.sleep(2)
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[1]/select')
        Select(loan_product).select_by_visible_text("超享借")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[1]')
        query_button.click()
        time.sleep(2)
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[1]/select')
        Select(loan_product).select_by_visible_text("超享借")
        #操作时间控件
        date1 = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/input')
        date1.send_keys("2018-12-29")
        date2 = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input')
        date2.send_keys("2018-12-29")
        #输入任务名称
        task_name = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[3]/input')
        task_name.send_keys("内部测试")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[1]')
        query_button.click()
        time.sleep(2)
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[2]')
        clear_button.click()
        time.sleep(2)
        #点击申请名单按钮
        apply_name = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[3]')
        apply_name.click()
        time.sleep(2)
        #输入名单提取个数
        extract_name = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[3]/div/div/div[2]/input')
        extract_name.send_keys("5")
        time.sleep(2)
        #点击提交任务按钮
        submit_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[3]/div/div/div[2]/div/button')
        submit_button.click()
        time.sleep(2)
        #关闭弹框页面
        close_img = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[3]/div/div/div[1]/div[2]/img')
        close_img.click()
        time.sleep(2)
        #筛选饼图数据
        pic_date = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[1]/div[1]/input')
        pic_date.clear()
        pic_date.send_keys('2018-12-26')
        #点击空白处消失
        element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[2]/table/tr[1]/th[3]').click()
        time.sleep(5)
        print("首页测试通过")
        
        #一、2点击外呼专员的工作台管理
        workplace_2 = element('//*[@id="app"]/div/section/section/div/aside/ul/li[1]/ul/li/ul/li[2]')
        workplace_2.click()
        time.sleep(1)
        #1、选择外呼状态
        call_status = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[1]/select')
        Select(call_status).select_by_visible_text("有意向")
        #2、输入任务名称
        task_name = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[2]/input')
        task_name.send_keys("内部测试")
        #3、点击登录密码的icon
        login_pw = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[2]/div[2]/img')
        login_pw.click()
        #4、输入手机号/姓名
        name_search = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[3]/input')
        name_search.send_keys("汤")
        #5、点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div/div[1]/div[3]/button[1]')
        query_button.click()
        time.sleep(2)
        print("工作台——外呼专员工作台——查询客户成功")
        #6、点击拨打电话按钮
        call_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[2]/table/tr[2]/td[5]/img[1]')
        call_button.click()
        print("工作台——外呼专员工作台——拨打电话成功")
        #7、点击收藏按钮
        collection = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[2]/table/tr[2]/td[5]/img[3]')
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
        name_search.send_keys("测试")
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
        Select(product_introduction).select_by_visible_text("自动测试添加产品")
        #8、选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[5]/div[2]/ul/li/div/div[1]/select')
        Select(loan_product).select_by_visible_text("自动测试添加产品")
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
        
        #二、点击外呼管理管理
        out_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[2]/div')
        out_manage.click()
        time.sleep(2)
        #二、1点击通话记录
        tel_record = element('//*[@id="app"]/div/section/section/div/aside/ul/li[2]/ul/li/ul/li')
        tel_record.click()
        time.sleep(2)
        #输入姓名/手机号关键字
        keyword = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        keyword.send_keys("汤文钦")
        time.sleep(1)
        #输入专员姓名
        worker = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/input')
        worker.send_keys('聚专员')
        #选择通话时间
        date1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div/div[1]/input')
        date1.send_keys("2018-12-29 00:00") 
        #点击空白处使时间弹框消失
        element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[6]').click()
        time.sleep(1)
        date2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div/div[2]/input')
        date2.send_keys("2019-01-03 00:00")
        element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[6]').click()
        #选择通话状态
        tel_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(tel_status).select_by_visible_text("接通")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #获取当前页面的handle
        current_handle = self.driver.current_window_handle
        print(current_handle)
        #点击录音按钮
        tape_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[7]')
        tape_button.click()
        time.sleep(2)
        #跳转回当前句柄
        self.driver.switch_to_window(current_handle)
        time.sleep(2)
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        #选择通话状态
        tel_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(tel_status).select_by_visible_text("其它")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("外呼管理——通话记录测试通过！")
        
        #三、点击客户管理
        custom_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[3]/div')
        custom_manage.click()
        time.sleep(1)
        #三、1点击客户列表
        user_list = element('//*[@id="app"]/div/section/section/div/aside/ul/li[3]/ul/li/ul/li')
        user_list.click()
        time.sleep(1)
        #关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("汤")
        #输入添加的开始时间
        create_time1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[1]/input')
        create_time1.send_keys('2018-12-20 00:00')
        time.sleep(1)
        #点击空白处使时间弹框消失
        blank_place = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[5]')
        blank_place.click()
        time.sleep(1)
        #输入添加的结束时间
        create_time2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[2]/input')
        create_time2.send_keys('2019-01-08 00:00')
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