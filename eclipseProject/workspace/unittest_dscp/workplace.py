'''
Created on 2019年1月16日

@author: 汤文钦
'''
#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
#下拉框操作
from selenium.webdriver.support.select import Select
#模拟鼠标操作
from selenium.webdriver.common.action_chains import ActionChains 
#测试贷后专员/贷后客服/委外催收   账号：dingone   密码：111111（操作按钮一样）

class my_workplace(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://dscp.super.com/#/")
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #测试委外/贷后专员账号：dingone   111111
        #输入用户名      
        username = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input")
        username.send_keys("yy")
        #输入密码
        pw = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/input")
        pw.send_keys("111111")
        #输入验证码
        check_code = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/input")
        check_code.send_keys("dscp")
        #点击登录
        login = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[4]/div/button")
        login.click()
        time.sleep(3)
        print("登录成功")
        
        #点击全部案件
        all_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        all_case.click()
        time.sleep(1)
        #输入应还款日期
        repay_data1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/input')
        repay_data1.send_keys('2019-04-20')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        repay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
        repay_data2.send_keys('2019-05-1')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        time.sleep(1)
        #选择还款状态
        pay_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select[1]')
        Select(pay_status).select_by_visible_text('待还款')
        time.sleep(1)
        #选择还款方式
        pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        Select(pay_method).select_by_visible_text('请选择')
        time.sleep(1)
#         #选择电话状态
#         cell_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
#         Select(cell_status).select_by_visible_text('正常接听')
#         time.sleep(1)
#         #选择案件跟进状态
#         case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/select')
#         Select(case_follow).select_by_visible_text('承诺还款')
#         time.sleep(1)
        #关键字搜索
        kw_search = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[6]/div/input')
        kw_search.send_keys('汤文钦')
        time.sleep(1)
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[7]/button[1]')
        search_button.click()
        time.sleep(1)
        print('全部案件搜索完毕')
        #获取当前窗口的句柄
        current_handle = self.driver.current_window_handle
        print(current_handle)
        #点击查看按钮
        view_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[3]/td[11]/span[1]')
        view_button.click()
        all_handles = self.driver.window_handles
        print(all_handles)
        #切换至第三个窗口
        view_page = self.driver.window_handles[2]
        self.driver.switch_to_window(view_page)
        #点击审批备注信息
        approval_mark = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/ul/li[24]/span')
        approval_mark.click()
        time.sleep(2)
        #关闭审批备注信息
        close_img = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/button/i')
        close_img.click()
        time.sleep(3)
        #滑动鼠标至呼入呼出top10——查看身份证信息
        approval_mark = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/ul/li[20]/span')
        top10 = element('//*[@id="tab-first"]')
        ActionChains(self.driver).drag_and_drop(approval_mark, top10).perform()
        time.sleep(1)
        #筛选呼入呼出top10的月份
        top_mouth = element('//*[@id="tellOutMonth"]')
        Select(top_mouth).select_by_visible_text('2019-01')
        time.sleep(2)
        #点击通话记录
        call_record = element('//*[@id="tab-second"]')
        call_record.click()
        time.sleep(2)
        #筛选通话记录的月份
        record_mouth = element('//*[@id="tellMonth"]')
        Select(record_mouth).select_by_visible_text('2019-01')
        time.sleep(2)
        #点击通讯录
        call_list = element('//*[@id="tab-third"]')
        call_list.click()
        time.sleep(2)
        #鼠标从通讯录滑动至催记第三条——查看案件详情信息
        call_list = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[8]/div[1]/input')
        record3 = element('//*[@id="pane-one"]/div/div/div/table/tr[4]/td[1]')
        ActionChains(self.driver).drag_and_drop(call_list, record3).perform()
        time.sleep(1)
        #点击全部按钮——查看全部催记
        all_button = element('//*[@id="pane-one"]/div/div/button')
        all_button.click()
        time.sleep(2)
        #将窗口切换回我的工作台中
        self.driver.switch_to_window(current_handle)
        time.sleep(3)
        print('全部案件查看完毕')
        
        #点击全部案件——编辑按钮
        edit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[3]/td[11]/span[2]')
        edit_button.click()
        time.sleep(1)
        all_handles = self.driver.window_handles
        print(all_handles)
        #切换至第四个窗口
        edit_page = self.driver.window_handles[3]
        self.driver.switch_to_window(edit_page)
        
        
        #选择电话状态
        call_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[8]/div[1]/select')
        Select(call_status).select_by_visible_text('正常接听')
        time.sleep(1)
        #选择案件跟进状态
        case_follow_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[8]/div[2]/select')
        Select(case_follow_status).select_by_visible_text('承诺还款')
        time.sleep(1)
        #选择下次跟进时间
        next_time = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[8]/div[3]/div/input')
        next_time.send_keys('2019-01-21 00:00:00')
        element('/html/body/div[2]/div[2]/button[1]/span').click()
        time.sleep(1)
        #鼠标从电话状态移动至保存按钮
        call_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[8]/div[1]/select')
        submit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[10]/div[2]/button')
        ActionChains(self.driver).drag_and_drop(call_status, submit_button).perform()
        time.sleep(1)
        #输入备注信息
        case_mark = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[10]/div[1]/textarea')
        case_mark.send_keys('自动化测试编写！！！！')
        #点击提交按钮
        submit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[10]/div[2]/button')
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
        print('我的工作台——全部案件——编辑测试通过')
        #将窗口切换回我的工作台中
        self.driver.switch_to_window(current_handle)
        time.sleep(3)
        
        #点击全部案件——还款按钮
        pay_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[11]/span[3]')
        pay_button.click()
        time.sleep(1)
        #输入还款金额
        payMoney = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/input')
        payMoney.send_keys('200')
        #提现时间
        payTime = element('//*[@id="time"]')
        payTime.send_keys('2019-04-17 14:58:06')
        time.sleep(1)
        #还款类型
        payType = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[3]/select')
        Select(payType).select_by_visible_text('展期还款')
        
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
        today_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/divy[2]/select')
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
        repay_data1.send_keys('2019-01-10')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        repay_data2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
        repay_data2.send_keys('2019-01-12')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr/th[1]').click()
        time.sleep(1)
        #逾期案件——还款状态
        overdue_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        #选择还款状态——逾期
        Select(overdue_pay_sta).select_by_visible_text("逾期")
        #逾期案件——电话状态
        overdue_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择电话状态——无人接听
        Select(overdue_pho_sta).select_by_visible_text("请选择")
        #逾期案件——案件跟进状态
        overdue_case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #选择案件跟进状态为——已提醒未回复
        Select(overdue_case_follow).select_by_visible_text("请选择")
        #在关键字中输入——汤文钦
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw.send_keys("张4")
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button').click()
        time.sleep(2)
        print('逾期案件搜索完毕')
        print('贷后专员——我的工作台测试通过')
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()