'''
Created on 2019年1月15日

@author: 汤文钦
'''
#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
#操作下拉框
from selenium.webdriver.support.select import Select
#模拟鼠标操作
from selenium.webdriver.common.action_chains import ActionChains 

class super(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://dscp.super.com/#/")
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #登录超级管理员     admin   111111        #输入账号
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
        
        #点击全部案件
        all_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        all_case.click()
        time.sleep(1)
        #输入应还款日期
        repay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/input')
        repay_data1.send_keys('2019-01-21')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        repay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
        repay_data2.send_keys('2019-01-22')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        time.sleep(1)
        #选择还款状态
        pay_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select[1]')
        Select(pay_status).select_by_visible_text('已结清')
        time.sleep(1)
        #选择还款方式
        pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select[2]')
        Select(pay_method).select_by_visible_text('系统操作')
        time.sleep(1)
        #选择电话状态
        cell_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        Select(cell_status).select_by_visible_text('正常接听')
        time.sleep(1)
        #选择案件跟进状态
        case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        Select(case_follow).select_by_visible_text('承诺还款')
        time.sleep(1)
        #关键字搜索
        kw_search = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw_search.send_keys('张三')
        time.sleep(1)
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button')
        search_button.click()
        time.sleep(1)
        print('全部案件搜索完毕')
        
        #点击今日案件
        today_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]')
        today_case.click()
        time.sleep(2)
        #今日案件——还款状态
        today_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select[1]')
        #选择还款状态——待还款
        Select(today_pay_sta).select_by_visible_text("待还款")
        #今日案件——还款方式
        today_pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select[2]')
        #选择还款方式——系统操作
        Select(today_pay_method).select_by_visible_text("系统操作")
        #今日案件——电话状态
        today_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        #选择电话状态——正常接听
        Select(today_pho_sta).select_by_visible_text("正常接听")
        #今日案件——案件跟进状态
        today_case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择案件跟进状态为——已提醒未回复
        Select(today_case_follow).select_by_visible_text("已提醒未回复")
        #在关键字中输入
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/div/input')
        kw.send_keys("张23")
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/button').click()
        time.sleep(2)
        print("今日案件搜索完毕")
        
        #点击明日提醒案件
        tomorrow_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[3]')
        tomorrow_case.click()
        time.sleep(2)
        #今日案件——还款状态
        today_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select[1]')
        #选择还款状态——待还款
        Select(today_pay_sta).select_by_visible_text("待还款")
        #今日案件——还款方式
        today_pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select[2]')
        #选择还款方式——系统操作
        Select(today_pay_method).select_by_visible_text("系统操作")
        #今日案件——电话状态
        today_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        #选择电话状态——正常接听
        Select(today_pho_sta).select_by_visible_text("正常接听")
        #今日案件——案件跟进状态
        today_case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择案件跟进状态为——已提醒未回复
        Select(today_case_follow).select_by_visible_text("已提醒未回复")
        #在关键字中输入——汤文钦
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/div/input')
        kw.send_keys("汤文钦")
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/button').click()
        time.sleep(2)
        print("明日提醒案件搜索完毕")
        
        #点击逾期案件
        overdue = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[4]')
        overdue.click()
        time.sleep(2)
        #输入应还款日期
        repay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/input')
        repay_data1.send_keys('2019-01-21')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        repay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
        repay_data2.send_keys('2019-01-22')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        time.sleep(1)
        #逾期案件——还款状态
        overdue_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        #选择还款状态——逾期
        Select(overdue_pay_sta).select_by_visible_text("逾期")
        #逾期案件——电话状态
        overdue_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择电话状态——无人接听
        Select(overdue_pho_sta).select_by_visible_text("无人接听")
        #逾期案件——案件跟进状态
        overdue_case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #选择案件跟进状态为——已提醒未回复
        Select(overdue_case_follow).select_by_visible_text("已提醒未回复")
        #在关键字中输入——汤文钦
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw.send_keys("汤文钦")
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button').click()
        time.sleep(2)
        print('逾期案件搜索完毕')
        print('超级管理员——我的工作台测试通过')
        
        #点击案件管理
        Case_Manage = element('//*[@id="app"]/div/div[1]/div[2]/ul/li[2]')
        Case_Manage.click()
        time.sleep(2)
        #点击所有案件
        both_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        both_case.click()
        time.sleep(1)
        #输入放款日期
        loan_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/input')
        loan_data1.send_keys('2019-01-18')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        loan_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
        loan_data2.send_keys('2019-01-24')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        time.sleep(1)
        #输入应还款日期
        repay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[1]/input')
        repay_data1.send_keys('2019-01-21')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        repay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div[2]/input')
        repay_data2.send_keys('2019-01-22')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        time.sleep(1)
        #输入实际回款日期
        real_pay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/input')
        real_pay_data1.send_keys('2019-01-18')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        real_pay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/input')
        real_pay_data2.send_keys('2019-01-20')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        time.sleep(1)
        #选择还款状态
        loan_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        Select(loan_status).select_by_visible_text('已结清')
        time.sleep(1)
        #选择负责人
        charge = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        Select(charge).select_by_visible_text('请选择')
        time.sleep(1)
        #关键字搜索
        kw_search = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw_search.send_keys('汤文钦')
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button')
        search_button.click()
        time.sleep(1)
        print('案件管理——所有案件查询成功')
        
        #点击案件分配
        distribute = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]')
        distribute.click()
        time.sleep(2)
        #点击定员按钮
        choose_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/h1/div[2]/button')
        choose_button.click()
        time.sleep(1)
        choose_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/label[2]/span[1]/span')
        choose_user.click()
        time.sleep(1)
        #点击提交按钮
        submit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button')
        submit_button.click()
        time.sleep(1)
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(2)
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(2)
        
        #输入应还款日期
        repay_data = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/input')
        repay_data.send_keys('2019-01-10')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        time.sleep(1)
        #选择上次负责人
        old_charge = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        Select(old_charge).select_by_visible_text('请选择')
        time.sleep(1)
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/button')
        search_button.click()
        time.sleep(1)
        #点击单选按钮
        radio = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[1]/img[1]')
        radio.click()
        time.sleep(1)
        #点击派单按钮
        distribute_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/h1/div[1]/button')
        distribute_button.click()
        time.sleep(1)
        #选择派单负责人
        new_charge = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select')
        Select(new_charge).select_by_visible_text('贷后一')
        time.sleep(1)
        #点击确定进行派单
        sure_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button') 
        sure_button.click()
        time.sleep(1)
        print("案件管理——案件分配测试通过")
        
        #点击催回总览
        paid_list = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[3]')
        paid_list.click()
        time.sleep(5)
        print('案件管理——催回总览测试通过')
         
        #点击委外案件
        weiwai_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[4]')
        weiwai_case.click()
        time.sleep(2)
#         #在用户有身份证及运营商记录时，点击查看按钮
#         view_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[9]/span[1]')
#         view_button.click()
#         time.sleep(1)

        #点击改派按钮
        change_charge_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[9]/span[2]')
        change_charge_button.click()
        time.sleep(1)
        #选择改派负责人
        change_charge = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select')
        Select(change_charge).select_by_visible_text('贷后二')
        #点击确定按钮
        sure_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button')
        sure_button.click()
        time.sleep(1)
        
        #点击委外按钮
        weiwai_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[9]/span[3]')
        weiwai_button.click()
        time.sleep(1)
        #选择委外机构
        weiwai_organ = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select')
        Select(weiwai_organ).select_by_visible_text('秒借委外')
        time.sleep(1)
        #点击确定按钮
        sure_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button')
        sure_button.click()
        time.sleep(1)
        #输入放款日期
        loan_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/input')
        loan_data1.send_keys('2018-12-10')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        loan_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
        loan_data2.send_keys('2019-01-10')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        time.sleep(1)
        #输入应还款日期
        repay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/input')
        repay_data1.send_keys('2019-01-09')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        repay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/input')
        repay_data2.send_keys('2019-01-10')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]').click()
        time.sleep(1)
        #选择还款状态
        loan_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        Select(loan_status).select_by_visible_text('逾期')
        time.sleep(1)
        #选择负责人
        charge = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        Select(charge).select_by_visible_text('聚信达委外')
        time.sleep(1)
        #关键字搜索
        kw_search = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw_search.send_keys('张37')
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button')
        search_button.click()
        time.sleep(1)
        print('案件管理——委外案件测试成功')
        
        #点击批量委外
        batch_weiwai = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[5]')
        batch_weiwai.click()
        time.sleep(1)
        #输入应还款日期
        repay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/input')
        repay_data1.send_keys('2019-01-09')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[6]').click()
        repay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
        repay_data2.send_keys('2019-01-10')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[6]').click()
        time.sleep(1)
        #选择负责人
        charge = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        Select(charge).select_by_visible_text('贷后二')
        time.sleep(1)
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/button')
        search_button.click()
        time.sleep(1)
        #选择案件委外
        choose_weiwai = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[1]/img[1]')
        choose_weiwai.click()
        time.sleep(1)
        #点击委外按钮
        weiwai_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/h1/div/button')
        weiwai_button.click()
        time.sleep(1)
        #选择委外负责人
        charger = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select')
        Select(charger).select_by_visible_text('秒借委外')
        time.sleep(1)
        #点击确定按钮
        sure_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button')
        sure_button.click()
        time.sleep(1)
        print('案件管理——批量委外测试通过')
        print('超级管理员——案件管理测试通过')
         
        #点击用户管理
        user_control = element('//*[@id="app"]/div/div[1]/div[2]/ul/li[3]')
        user_control.click()
        time.sleep(1)
        #点击新建用户按钮
        add_user_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div/button')
        add_user_button.click()
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
        
        #点击新建用户按钮
        add_user_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div/button')
        add_user_button.click()
        time.sleep(1)
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
        
        #点击新建用户按钮
        add_user_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div/button')
        add_user_button.click()
        time.sleep(1)
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
        
        #点击新建用户按钮
        add_user_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div/button')
        add_user_button.click()
        time.sleep(1)
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