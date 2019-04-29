'''
Created on 2019年1月10日

@author: 汤文钦
'''
#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
#操作下拉框
from selenium.webdriver.support.select import Select
#模拟键盘操作
from selenium.webdriver.common.keys import Keys
#模拟鼠标操作
from selenium.webdriver.common.action_chains import ActionChains 


class case_manage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://dscp.super.com/#/")  
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        
        #测试贷后主管账号：threeDG   111111
        #输入用户名        
        username = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input")
        username.send_keys("threeDG")
        #输入密码
        pw = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/input")
        pw.send_keys("111111")
        #输入验证码
        check_code = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/input")
        check_code.send_keys("dscp")
        #点击登录按钮
        login = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[4]/div/button")
        login.click()
        time.sleep(3)
        print("登录测试通过")

        #点击所有案件
        all_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        all_case.click()
        time.sleep(2)
        
        #点击今日案件
        today_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]')
        today_case.click()
        time.sleep(2)
        
        #点击明日提醒案件
        tomorrow_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[3]')
        tomorrow_case.click()
        time.sleep(2)
        
        #点击逾期案件 
        overdue = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[4]')
        overdue.click()
        time.sleep(2)
       
        #点击案件管理
        Case_Manage = element('//*[@id="app"]/div/div[1]/div[2]/ul/li[2]')
        Case_Manage.click()
        time.sleep(2)
        #点击所有案件
        both_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        both_case.click()
        time.sleep(2)
        #案件管理——选择还款状态
        case_manage_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择还款状态
        Select(case_manage_pay_sta).select_by_visible_text("待还款")
        #案件管理——选择负责人
        case_manage_leader = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #案件管理——选择负责人
        Select(case_manage_leader).select_by_visible_text("三个产品贷管")
        #关键字搜索中输入用户姓名
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw.send_keys('汤文钦')
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button')
        search_button.click()
        time.sleep(2)
        #打印当前页面
        current_handle = self.driver.current_window_handle
        print(current_handle)
        #点击查看按钮
        view_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[10]/span')
        view_button.click()
        #查看所有打开的页面
        all_handles = self.driver.window_handles
        print(all_handles)
        #切换至查看页面
        view_page = self.driver.window_handles[2]
        self.driver.switch_to_window(view_page)
        time.sleep(5)
        #鼠标从基本资料开始滑动
        basic_info = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/h1') 
        #滑动至运营商资料
        phone_info = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[5]/h1')
        #模拟鼠标操作
        ActionChains(self.driver).drag_and_drop(basic_info, phone_info).perform()
        time.sleep(2)
        #鼠标从运营商开始滑动
        phone_info = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[5]/h1')
        #鼠标滑动至电话号码处
        tel_num = element('//*[@id="pane-first"]/div/div[1]/div/table/tr[5]/td[1]')
        ActionChains(self.driver).drag_and_drop(phone_info, tel_num).perform()
        time.sleep(2)
        #点击呼入呼出top10
        phone_top = element('//*[@id="tab-first"]')
        phone_top.click()
        time.sleep(2)
        #点击通话详单
        phone_detail = element('//*[@id="tab-second"]')
        phone_detail.click()
        time.sleep(2)
        #选择通话月份
        phone_mouth = element('//*[@id="tellMonth"]')
        #选择通话月份为2018年9月
        Select(phone_mouth).select_by_visible_text("2018-09")
        time.sleep(2)
        #点击通讯录
        tel_address = element('//*[@id="tab-third"]')
        tel_address.click()
        time.sleep(2)
        #模拟鼠标操作——滑动至底部
        #鼠标从运营商开始滑动
        phone_info = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[5]/h1')
        #将鼠标滑至全部
        bottom = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[9]/div[2]/table/tr[3]/td[1]')
        ActionChains(self.driver).drag_and_drop(phone_info, bottom).perform()
        time.sleep(2)
        #点击全部按钮查看催记记录
        all_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[9]/div[1]/button')
        all_button.click()
        time.sleep(2)
        print("所有案件——查看案件测试通过")
        
        #页面切换回案件管理页
        self.driver.switch_to_window(current_handle)
        time.sleep(2)
        #案件管理——选择还款状态
        case_manage_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择还款状态为请选择
        Select(case_manage_pay_sta).select_by_visible_text("请选择")
        #案件管理——选择负责人
        case_manage_leader = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #案件管理——选择负责人——请选择
        Select(case_manage_leader).select_by_visible_text("请选择")
        #关键字搜索
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw.clear()
        kw.send_keys('张21')
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button')
        search_button.click()
        time.sleep(2)
        #点击改派按钮
        both_case_change_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[10]/span[2]')
        both_case_change_button.click()
        time.sleep(2)
        #选择委外案件中——改派负责人
        weiwai_case_change_leader = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select')
        Select(weiwai_case_change_leader).select_by_visible_text("三个产品贷管")
        #点击确定按钮
        ensure = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button')
        ensure.click()
        time.sleep(1)
        #再次刷新页面
        self.driver.refresh()
        time.sleep(3)
        print("所有案件——改派测试通过")
        
        #所有案件——生成按钮
        make_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[10]/span[3]')
        make_button.click()
        time.sleep(2)
        #从失信记录滑动至返回按钮
        credit_record = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/h1')
        back_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[5]/button')
        ActionChains(self.driver).drag_and_drop(credit_record, back_button).perform()
        time.sleep(2)
        #点击返回按钮
        back_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[5]/button')
        back_button.click()
        time.sleep(2)
        print("所有案件——生成页面测试通过")
        
        #点击案件分配（派单）
        distribute = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]')
        distribute.click()
        time.sleep(2)
        #案件分配——上次负责人
        dis_leader = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        Select(dis_leader).select_by_visible_text("客服三")
        time.sleep(2)
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/button')
        search_button.click()
        time.sleep(2)
        #进行全选操作
        all_select = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[1]/th[1]/img[1]')
        all_select.click()
        #点击派单按钮
        dis_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/h1/div/button')
        dis_button.click()
        time.sleep(2)
        #选择派单页面的负责人
        dis_new_leader = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select')
        Select(dis_new_leader).select_by_visible_text("贷后三")
        #点击确定按钮
        ensure = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button')
        ensure.click()
        time.sleep(5)
        print("案件分配——派单测试通过")
        
        #点击催回总览
        paid_list = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[3]')
        paid_list.click()
        time.sleep(5)
        print("催回总览——查看催回总览")
        
        #点击委外案件
        weiwai_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[4]')
        weiwai_case.click()
        time.sleep(2)
        #委外案件——选择还款状态
        weiwai_case_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #还款状态选择为逾期
        Select(weiwai_case_pay_sta).select_by_visible_text("逾期")
        #委外案件——选择负责人
        weiwai_case_leader = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #负责人选择
        Select(weiwai_case_leader).select_by_visible_text("秒借催收专员")
        #关键字搜索
        kw_search = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw_search.send_keys("张20")
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button')
        search_button.click()
        time.sleep(2)
        #点击改派按钮
        weiwai_case_change_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[9]/span[2]')
        weiwai_case_change_button.click()
        time.sleep(2)
        #选择委外案件中——改派负责人
        weiwai_case_change_leader = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select')
        Select(weiwai_case_change_leader).select_by_visible_text("三个产品贷管")
        #点击确定按钮
        ensure = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button')
        ensure.click()
        time.sleep(1)
        #再次刷新页面
        self.driver.refresh()
        time.sleep(3)
        print("委外案件——改派测试通过")
        
        #选择第二条案件的委外按钮
        weiwai_case_weiwai_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[3]/td[9]/span[3]')
        weiwai_case_weiwai_button.click()
        #选择委外机构名称
        weiwai_case_weiwai_org = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select')
        Select(weiwai_case_weiwai_org).select_by_visible_text("秒借催收专员")
        time.sleep(1)
        #点击确定按钮
        ensure = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button')
        ensure.click()
        time.sleep(2)
        #刷新页面
        self.driver.refresh()
        time.sleep(3)
        print("委外案件——委外测试通过")
        
        #批量委外
        #1、进入批量委外界面
        batch_outsourcing = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[5]/span')
        batch_outsourcing.click()
        time.sleep(2)
        #案件管理——选择负责人
        case_manage_leader = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #案件管理——选择负责人
        Select(case_manage_leader).select_by_visible_text("三个产品贷管")
        #2、选择第一个、第二个案件进行批量委外
        case1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[1]/img[1]').click()
        case2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[3]/td[1]/img[1]').click()
        #3、点击委外按钮
        batch_out =  element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/h1/div/button')
        batch_out.click()
        #4、选择负责人
        case_manage_leader = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select')
        Select(case_manage_leader).select_by_visible_text("秒借委外")
        #5、点击确定按钮
        ensure = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button')
        ensure.click()
        time.sleep(2)
        print("批量测试委外通过")
        print("案件管理测试通过")
        
        
        
        
        
        

        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()