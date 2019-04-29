'''
Created on 2019年1月15日

@author: 汤文钦
'''
#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select

#测试准备：用j3添加黑名单——汤 13070123277

class test_my_workplace(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://call.super.com/#/")  
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #输入用户名      
        username = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input')
        username.send_keys("j2")
        #输入密码
        pw = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input')
        pw.send_keys("111111")
        #点击登录按钮
        login_button = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[3]/div/button')
        login_button.click()
        time.sleep(1)
        print("登录外呼主管成功")
        
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
        #筛选饼图数据
        pic_date = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[1]/div[1]/input')
        pic_date.clear()
        pic_date.send_keys('2018-12-26')
        #点击空白处消失
        element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[2]/table/tr[1]/th[3]').click()
        time.sleep(5)
        print("首页测试通过")
        
        #二、点击任务管理
        task_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[2]/div')
        task_manage.click()
        time.sleep(2)
        #二、1任务管理——任务列表（主管页）
        task_director = element('//*[@id="app"]/div/section/section/div/aside/ul/li[2]/ul/li/ul/li')
        task_director.click()
        time.sleep(2)
        #1、输入关键字
        keyword = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        keyword.send_keys('测试申请回收星标名单')
        #2、输入生效时间
        date1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[1]/input')
        date1.send_keys('2019-01-04 18:38')
        element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[1]/span').click()
        data2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[2]/input')
        data2.send_keys('2019-01-14 18:38')
        element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[1]/span').click()
        #3、选择任务状态
        task_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(task_status).select_by_visible_text('已分配')
        #4、点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #5、点击单选框，选择该任务进行分配
        radio = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[1]/img[1]')
        radio.click()
        #6、点击分配按钮
        distribute_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[3]')
        distribute_button.click()
        time.sleep(2)
        #7、选择分配给无任务的专员
        assistant = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/label/span[1]/span')
        assistant.click()
        #8、点击提交按钮
        submit_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[2]/div[3]/button')
        submit_button.click()
        time.sleep(5)
        print("任务管理——任务管理主管页测试通过")
        
        #三、点击报表管理
        report_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[3]/div')
        report_manage.click()
        time.sleep(2)
        #三、1点击坐席话务报表
        zuoxi = element('//*[@id="app"]/div/section/section/div/aside/ul/li[3]/ul/li/ul/li[1]')
        zuoxi.click()
        time.sleep(2)
        #输入姓名/手机号关键字
        keyword = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        keyword.send_keys("聚专员")
        #选择日期
        date1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[1]/input')
        date1.send_keys("2018-12-28")
        #点击日期处使日期弹框消失
        date = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[1]')
        date.click()
        date2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/div[2]/input')
        date2.send_keys("2018-12-29")
        date = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[1]/th[1]')
        date.click()
        #选择机构
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(organ).select_by_visible_text("聚信达")
        #选择排序——降序desc，升序asc
        order_by = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(order_by).select_by_visible_text("转化率高到低")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("报表管理——坐席话务报表——查询排序完成")
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(1)
        #点击导出按钮
        export_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[3]')
        export_button.click()
        time.sleep(2)
        print("报表管理——坐席话务报表——导出成功")
        #选择机构
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/select')
        Select(organ).select_by_visible_text("聚信达")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #查看下款数
        loan_num = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[8]/td[5]/img')
        loan_num.click()
        time.sleep(2)
        #点击下款详情的关闭按钮
        close_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[1]/div[2]/img')
        close_button.click()
        time.sleep(2)
        print("报表管理——坐席话务报表——查看下款详情通过")
        print("报表管理——坐席话务报表测试通过！")

        #三、2点击外呼详情报表
        detail_report = element('//*[@id="app"]/div/section/section/div/aside/ul/li[3]/ul/li/ul/li[2]')
        detail_report.click()
        time.sleep(2)
        #输入姓名/手机号关键字
        keyword = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        keyword.send_keys("汤文钦")
        #输入任务名称
        task_name = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/input')
        task_name.send_keys('内部测试')
        #选择日期
        date1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div[1]/input')
        date1.send_keys("2018-12-28")
        date2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div[2]/input')
        date2.send_keys("2018-12-29")
        #选择放款状态
        loan_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(loan_status).select_by_visible_text("已放款")
        #选择机构角色
        organ = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[5]/select[1]')
        Select(organ).select_by_visible_text("聚信达")
        role = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[5]/select[2]')
        Select(role).select_by_visible_text("聚专员")
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[6]/select')
        Select(loan_product).select_by_visible_text("超享借")
        #选择审核状态
        audit_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[7]/select')
        Select(audit_status).select_by_visible_text("审批通过")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #点击导出按钮
        export_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[3]')
        export_button.click()
        time.sleep(2)
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(3)
        #选择放款状态
        loan_status = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[4]/select')
        Select(loan_status).select_by_visible_text("已放款")
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[6]/select')
        Select(loan_product).select_by_visible_text("聚信达外部产品")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        #点击查看按钮
        view_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[9]/span')
        view_button.click()
        time.sleep(2)
        #点击返回按钮
        back_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[1]/div[2]')
        back_button.click()
        time.sleep(2)
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(3)
        print("报表管理——外呼详情报表测试通过！")
        
        #四、点击外呼管理管理
        out_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[4]/div')
        out_manage.click()
        time.sleep(2)
        #四、1点击通话记录
        tel_record = element('//*[@id="app"]/div/section/section/div/aside/ul/li[4]/ul/li/ul/li')
        tel_record.click()
        time.sleep(2)
        #输入姓名/手机号关键字
        keyword = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        keyword.send_keys("汤文钦")
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
        
        #五、点击客户管理
        custom_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[5]/div')
        custom_manage.click()
        time.sleep(1)
        #五、1点击黑名单
        black_list = element('//*[@id="app"]/div/section/section/div/aside/ul/li[5]/ul/li/ul/li[1]')
        black_list.click()
        time.sleep(1)
        #关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("汤")
        #输入增加人姓名
        add_name = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/input')
        add_name.send_keys("外呼专员")
        #输入添加时间
        add_time1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div[1]/input')
        add_time1.send_keys('2019-01-08 16:16')
        add_time2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div[2]/input')
        add_time2.send_keys('2019-01-18 18:15')
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("客户管理——黑名单——查询黑名单成功")
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        #听黑名单中的录音并删除黑名单用户
        #1、输入关键字   
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("汤")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(1)
        #2、听录音
        tape_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[6]/img[2]')
        tape_button.click()
        time.sleep(2)
        #点击关闭录音页面
        close_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[1]/div[2]/img')
        close_button.click()
        time.sleep(2)
        #3、单选用户
        radio_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[1]/img[1]')
        radio_button.click()
        #4、删除已选用户
        delete_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[3]')
        delete_button.click()
        time.sleep(2)
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(2)
        print("客户管理——黑名单——删除黑名单成功")
        print("客户管理——黑名单测试通过")
        
        #五、2点击客户列表
        user_list = element('//*[@id="app"]/div/section/section/div/aside/ul/li[5]/ul/li/ul/li[2]')
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