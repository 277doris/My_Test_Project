'''
Created on 2018年11月28日

@author: 汤文钦
'''
#-*-  coding:utf-8 -*-
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
#弹框操作
from selenium.webdriver.common.alert import Alert
#下拉框操作
from selenium.webdriver.support.select import Select
#模拟鼠标操作
from selenium.webdriver.common.action_chains import ActionChains 

class Workplace(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
    
    def test_myworkplace(self):
        self.driver.get("http://dscp.super.com/#/")
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #测试委外/贷后专员账号：dingone   111111
        #输入用户名      
        username = element("/html/body/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input")
        username.send_keys("dingtwo")
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
        
        #点击今日案件
        today_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]')
        today_case.click()
        time.sleep(2)
        #今日案件——还款状态
        today_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select[1]')
        #选择还款状态——待还款
        Select(today_pay_sta).select_by_visible_text("待还款")
        #今日案件——还款方式
        today_pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        #选择还款方式——系统操作
        Select(today_pay_method).select_by_visible_text("系统操作")
        #今日案件——电话状态
        today_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择电话状态——正常接听
        Select(today_pho_sta).select_by_visible_text("正常接听")
        #今日案件——案件跟进状态
        today_case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #选择案件跟进状态为——已提醒未回复
        Select(today_case_follow).select_by_visible_text("已提醒未回复")
        #在关键字中输入
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw.send_keys("张23")
        search_button1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[6]/button[1]')
        search_button1.click()
        time.sleep(2)
        print('我的工作台——今日案件：搜索成功')
        
        #点击明日提醒案件
        tomorrow_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[3]')
        tomorrow_case.click()
        time.sleep(2)
        #明日案件——还款状态
        today_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select[1]')
        #选择还款状态——待还款
        Select(today_pay_sta).select_by_visible_text("待还款")
        #今日案件——还款方式
        today_pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        #选择还款方式——系统操作
        Select(today_pay_method).select_by_visible_text("系统操作")
        #今日案件——电话状态
        today_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
        #选择电话状态——正常接听
        Select(today_pho_sta).select_by_visible_text("正常接听")
        #今日案件——案件跟进状态
        today_case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #选择案件跟进状态为——已提醒未回复
        Select(today_case_follow).select_by_visible_text("已提醒未回复")
        #在关键字中输入
        kw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input')
        kw.send_keys("张23")
        search_button2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[6]/button[1]')
        search_button2.click()
        time.sleep(2)
        print('我的工作台——明日案件：搜索成功')
        
        #点击逾期案件
        overdue = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[4]')
        overdue.click()
        time.sleep(2)
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
        search_button3 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[6]/button[1]')
        search_button3.click()
        time.sleep(2)
        
        #点击全部案件
        all_case = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        all_case.click()
        time.sleep(2)
        #全部案件——选择应还款日期的开始及结束时间
        should_pay_date1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/input')
        should_pay_date1.send_keys('2019-01-01')
        time.sleep(1)
        should_pay_date2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
#         should_pay_date2.click()
        should_pay_date2.send_keys('2019-04-10')
        #全部案件——还款状态
        all_case_pay_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select')
        #选择还款状态——展期
        Select(all_case_pay_sta).select_by_visible_text("展期")
#         #全部案件——还款方式
#         all_case_pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select')
#         #选择还款方式为系统操作
#         Select(all_case_pay_method).select_by_visible_text("人工操作")
        #全部案件——电话状态
        all_case_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select')
        #选择还款方式为系统操作
        Select( all_case_pho_sta).select_by_visible_text("正常接听")
        #全部案件——案件跟进状态
        all_case_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/select')
        Select( all_case_pho_sta).select_by_visible_text("承诺还款")
        #关键字搜索
        kw_search = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[6]/div/input')
        kw_search.send_keys("汤文钦")
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[7]/button[1]')
        search_button.click()
        time.sleep(3)
        #获取当前窗口的句柄
        current_handle = self.driver.current_window_handle
        print(current_handle)
        #点击查看按钮
        view_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[10]/span[1]')
        view_button.click()
        all_handles = self.driver.window_handles
        print(all_handles)
        #切换至第三个窗口
        view_page = self.driver.window_handles[2]
        self.driver.switch_to_window(view_page)
        time.sleep(5)
        #鼠标拖动，从基本资料开始
        source = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/h1')
        #拖动至运营商资料
        target = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[5]/h1')
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        time.sleep(3)
        #查看运营商数据
        source1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[5]/h1')
        #拖动至案件详情
        target1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[7]/h1')
        ActionChains(self.driver).drag_and_drop(source1, target1).perform()
        #点击呼入呼出top10
        top_10 = element('//*[@id="tab-first"]')
        top_10.click()
        time.sleep(2)
        #点击通话详单
        phone_detail = element('//*[@id="tab-second"]')
        phone_detail.click()
        time.sleep(2)
        #选择月份
        select_mouth = element('//*[@id="tellMonth"]')
        select_mouth.click()
        #选择为1月份
        select_date = element('//*[@id="tellMonth"]/option[3]')
        select_date.click()
        time.sleep(5)
        #点击通讯录
        phone_address = element('//*[@id="tab-third"]')
        phone_address.click()
        time.sleep(2)
        #将鼠标从通讯录
        source2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[5]/h1')
        #拖动至案件详情
        target2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[7]/h1')
        ActionChains(self.driver).drag_and_drop(source2, target2).perform()
        time.sleep(3)
        print('查看操作成功')
        #将窗口切换回我的工作台中
        self.driver.switch_to_window(current_handle)
        time.sleep(3)
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[7]/button[2]')
        clear_button.click()
        time.sleep(1)
        
        #点击还款按钮
        pay_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[10]/span[3]')
        pay_button.click()
        time.sleep(1)
        #还款金额
        account = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[1]/input')
        account.send_keys('200')
        #选择还款类型
        pay_type = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[1]/select')
        Select(pay_type).select_by_visible_text('部分还款')
        #选择还款方式
        pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/select')
        Select(pay_method).select_by_visible_text('微信转账')
        #输入提现银行卡
        bank_cd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/input')
        bank_cd.send_keys('ICBC1234567890')
        #输入备注
        marked = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[3]/textarea')
        marked.send_keys('这是一条自动输入的备注信息')
        #点击上传图片按钮
        upload = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[3]/div/ul/li[1]/div/div/div')
        upload.click()
        #调用上传分机.exe上传程序
        os.system("C:\\Users\\22648\\Desktop\\自动化上传文件\\贷后上传还款图片.exe")
        time.sleep(2)
        #模拟鼠标滑动
        target1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[3]/div/ul/li[1]/div/div/div')
        target2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[4]/button[2]')
        ActionChains(self.driver).drag_and_drop(target1, target2).perform()
        time.sleep(1)
        #点击提交按钮
        submit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[4]/button[2]')
        submit_button.click()
        time.sleep(3)
        #对弹框进行操作
        dig_alert = self.driver.switch_to_alert()
        print(dig_alert)
        time.sleep(1)
        dig_alert.accept()
        time.sleep(1)
        dig_alert.accept()
        print('还款操作成功')
        time.sleep(5)
        
        #点击编辑按钮
        edit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[10]/span[2]')
        edit_button.click()
        #切换至第三个窗口
        edit_page = self.driver.window_handles[3]
        self.driver.switch_to_window(edit_page)
        time.sleep(5)
        #从基本资料开始滑动鼠标
        basic_info = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/h1')
        #滑动至下次跟进时间
        next_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[8]/div[3]/span')
        ActionChains(self.driver).drag_and_drop(basic_info, next_follow).perform()
        time.sleep(2)
        #选择电话状态
        edit_pho_sta = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[8]/div[1]/select')
        #选择电话状态为正常接听
        Select(edit_pho_sta).select_by_visible_text("正常接听")
        #选择案件跟进状态
        edit_case_follow = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[8]/div[2]/select')
        #选择案件跟进状态为承诺还款
        Select(edit_case_follow).select_by_visible_text("承诺还款")
        #选择下次跟进时间
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[8]/div[3]/div/input').click()
        time.sleep(1)
        element('/html/body/div[2]/div[2]/button[1]/span').click()
        time.sleep(2)
        #从案件详情开始鼠标滑动
        case_detail = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[7]/h1')
        #滑动至文字处
        submit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[10]/div[1]/span')
        ActionChains(self.driver).drag_and_drop(case_detail, submit_button).perform() 
        time.sleep(2)
        #查看还款记录
        pay_list = element('//*[@id="tab-two"]')
        pay_list.click()
        #点击全部按钮
        all_button = element('//*[@id="pane-two"]/div/div/button')
        all_button.click()
        time.sleep(2)
        #查看还款提交记录
        submit_pay_list = element('//*[@id="tab-three"]')
        submit_pay_list.click()
        time.sleep(2)
        
        #点击还款记录中的撤回按钮
        sub_back_button = element('//*[@id="pane-three"]/div/div/div/table/tr[2]/td[9]/span[2]')
        sub_back_button.click()
        #切换至alert
        dig_alert = self.driver.switch_to_alert()
        time.sleep(1)
        print(dig_alert)
        dig_alert.accept()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(1)
        #点击还款提交记录中的编辑按钮
        sub_edit_button = element('//*[@id="pane-three"]/div/div/div/table/tr[2/td[9]/span[1]')
        sub_edit_button.click()
        time.sleep(1)
        #修改还款金额
        edit_account = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/input')
        edit_account.clear()
        edit_account.send_keys('300')
        #修改还款类型
        sub_pay_type = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/select')
        Select(sub_pay_type).select_by_visible_text('展期还款')
        #填写下次还款时间
        next_time = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/input')
        next_time.send_keys('2019-04-04')
        #修改还款方式
        sub_pay_method = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/select')
        Select(sub_pay_method).select_by_visible_text('银行卡转账')
        #修改提现银行卡
        sub_bank_cd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/input')
        sub_bank_cd.clear()
        sub_bank_cd.send_keys('ICBC777888')
        #修改备注信息
        sub_marked = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/textarea')
        sub_marked.clear()
        sub_marked.send_keys('自动化测试编辑备注信息')
        #鼠标从备注信息滑动至提交按钮
        target3 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/textarea')
        target4 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[4]/button[2]')
        ActionChains(self.driver).drag_and_drop(target3, target4).perform()
        time.sleep(1)
        #点击提交按钮
        submit_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[4]/button[2]')
        submit_button.click()
        #切换至alert
        dig_alert = self.driver.switch_to_alert()
        time.sleep(1)
        print(dig_alert)
        dig_alert.accept()
        
        #查看催记记录
        record_list = element('//*[@id="tab-one"]')
        record_list.click()
        time.sleep(1)
        #填写催记记录
        record = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[10]/div[1]/textarea')
        record.send_keys("这是一条自动添加的催收记录")
        #点击提交按钮
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[10]/div[2]/button').click()
        time.sleep(5)
        #将窗口切换到alert中并接受
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        print(dig_alert)
        dig_alert.accept()
        time.sleep(1)
        print('编辑操作成功')
        #将窗口切换回我的工作台中
        self.driver.switch_to_window(current_handle)
        time.sleep(5)
        
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()


if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    '''
                    引用HTMLTestRunner生成测试报告
        python3和python的HTMLTestRunner有不同，需要修改
                    且运行时需要在if语句中，编辑器默认只运行if以上内容
    '''
    #将测试用例加入到测试容器中——class下def方法
    test_suite.addTest(Workplace("test_myworkplace"))
    # 定义个报告存放路径，支持相对路径
    filename = 'C:\\Users\\22648\\Desktop\\test\\desc_Workplace.html'
    #打开一个文件，将result写入此file中
    fp = open(filename,'wb')
    # 定义测试报告，打开方式、标题、描述
    runner = HTMLTestRunner(
        stream = fp, title='贷后——我的工作台', description='用例执行情况：')
    # 运行测试用例
    runner.run(test_suite)
    # 写完之后必须将fp关闭，否则报告是空的
    fp.close()