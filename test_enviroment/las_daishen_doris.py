#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

class DaiShen(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_daishen(self):
        self.driver.get("http://las.super.com/view/login.html")
        self.driver.maximize_window()
        element = self.driver.find_element_by_xpath
 
        #输入用户名
        username = element("/html/body/div[2]/div/form/label[1]/div/input")
        username.send_keys("doris")
        #输入密码
        password = element("/html/body/div[2]/div/form/label[2]/div/input")
        password.send_keys("111111")
        #输入验证码
        check_code = element("/html/body/div[2]/div/form/label[3]/div/input")
        check_code.send_keys("spxt")
        #点击登录按钮
        login = element("/html/body/div[2]/div/form/button")
        login.click()
        time.sleep(2)

        #产品审批
        #点击产品审批模块
        prod_appro = element("/html/body/div[1]/div[1]/div/ul/li[4]/a")
        prod_appro.click()
        time.sleep(1)
        #点击待审模块
        wait_appro = element("/html/body/div[2]/div[1]/div/ul/li[1]/a")
        wait_appro.click()
        time.sleep(1)
        #筛选产品
        product_name = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select")
        #选择产品为聚信达产品
        Select(product_name).select_by_visible_text("聚信达产品")
        #筛选处理状态
        deal_statu = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/select")
        #筛选处理状态为审核中
        Select(deal_statu).select_by_visible_text("审核中")
        #点击来源
        source = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/select")
        #来源选择为其他
        Select(source).select_by_visible_text("其他")
        #在关键字中输入姓名
        key_word = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[5]/td[2]/input")
        key_word.send_keys("汤文钦")
        #点击查询按钮
        query = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[6]/td[2]/div[1]")
        query.click()
        time.sleep(3)
        #点击接单/处理按钮
        accept = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[11]/a')
        accept.click()
        time.sleep(1)
        current_handle1 = self.driver.current_window_handle
        print(current_handle1)
        #如果是点击接单按钮，则需启动64-74行的代码
        # # 获取alert对话框
        # dig_alert = self.driver.switch_to.alert
        # time.sleep(1)
        # # 打印警告对话框内容
        # print(dig_alert.text)
        # # alert对话框属于警告对话框，我们这里只能接受弹窗
        # dig_alert.accept()
        time.sleep(1)

        #切换至第三个窗口
        view_page = self.driver.window_handles[2]
        self.driver.switch_to_window(view_page)
        time.sleep(5)
        apply_table = element('//*[@id="showLookTables"]/table[1]/th')
        check_result = element('//*[@id="checkResult"]/tbody/tr[1]/td')
        ActionChains(self.driver).drag_and_drop(apply_table, check_result).perform()
        time.sleep(2)
        #查看证明材料
        showAll_button = element('//*[@id="report-template"]/div[2]/div[1]/div[2]/a')
        showAll_button.click()
        time.sleep(2)
        #再次点击显示全部按钮进行收起
        showAll_button.click()
        time.sleep(1)
        #鼠标从显示全部滑动至审核结果
        check_result = element('//*[@id="checkResult"]/tbody/tr[1]/td')
        ActionChains(self.driver).drag_and_drop(showAll_button, check_result).perform()
        time.sleep(2)
        #点击系统审核信息
        sys_info = element('//*[@id="newPerNav"]/li[1]')
        sys_info.click()
        time.sleep(2)
        #关闭系统审核信息的显示
        closeSys_btn = element('//*[@id="report-template"]/div[2]/div[4]/div/div[1]/span')
        closeSys_btn.click()
        '''
        #如果审批信息多：从系统审核信息——滑动至关闭按钮
        # sys_info = element('//*[@id="report-template"]/ul/li[2]')
        # close_button = element('//*[@id="report-template"]/div[2]/div[2]/div/div[4]/a')
        # ActionChains(driver).drag_and_drop(sys_info, close_button).perform()
        # time.sleep(2)
        # #鼠标上滑，从关闭按钮开始
        # close_button = element('//*[@id="report-template"]/div[2]/div[2]/div/div[4]/a')
        # #上滑至系统审核信息
        # sys_info = element('//*[@id="report-template"]/ul/li[2]')
        # ActionChains(driver).drag_and_drop(close_button, sys_info).perform()
        # time.sleep(2)
        '''
        #点击运营商数据
        ISP = element('//*[@id="newPerNav"]/li[2]')
        ISP.click()
        #1、运营商数据-紧急联系人分析
        emerge_analyse = element('//*[@id="report-template"]/div[2]/div[4]/div/div[2]/ul[1]/li[1]')
        emerge_analyse.click()
        time.sleep(2)
        #2、有效号码分析
        valid_num = element('//*[@id="report-template"]/div[2]/div[4]/div/div[2]/ul[1]/li[2]')
        valid_num.click()
        time.sleep(1)
        #3、运营商总览
        ISP_review = element('//*[@id="report-template"]/div[2]/div[4]/div/div[2]/ul[1]/li[3]')
        ISP_review.click()
        time.sleep(1)
        #4、呼入呼出top10
        call_top = element('//*[@id="report-template"]/div[2]/div[4]/div/div[2]/ul[1]/li[4]')
        call_top.click()
        time.sleep(1)
        #5、通讯录
        phoneBook = element('//*[@id="report-template"]/div[2]/div[4]/div/div[2]/ul[1]/li[5]')
        phoneBook.click()
        time.sleep(1)
        #关闭运营商数据页面
        close_ISP = element('//*[@id="report-template"]/div[2]/div[4]/div/div[1]/span')
        close_ISP.click()
        #点击位置信息
        address_info = element('//*[@id="newPerNav"]/li[3]')
        address_info.click()
        time.sleep(1)
        address_close = element('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/header[1]/img[1]')
        address_close.click()
        time.sleep(1)
        '''——若无位置信息，则需对alert弹框进行操作
        # # 获取alert对话框
        # dig_alert = self.driver.switch_to.alert
        # time.sleep(1)
        # # 打印警告对话框内容
        # print(dig_alert.text)
        # # alert对话框属于警告对话框，我们这里只能接受弹窗
        # dig_alert.accept()
        '''
        #从审核结果滑动至关闭按钮
        close_button = element('//*[@id="report-template"]/div[2]/div[1]/div[5]/button')
        ActionChains(self.driver).drag_and_drop(check_result, close_button).perform()
        time.sleep(2)
        #编辑借款人备注信息并保存
        edit_mark = element('//li[1]//textarea[1]')
        edit_mark.clear()
        edit_mark.send_keys('这是一条自动添加的信息')
        element('//li[1]//button[1]').click()
        time.sleep(1)
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        dig_alert.accept()
        time.sleep(2)
        '''
        #审批通过
        pass_button = element("//input[@id='passThrough']")
        pass_button.click()
        time.sleep(1)
        #选择建议期数
        date_num = element('//*[@id="checkInfo"]/div[2]/select')
        Select(date_num).select_by_visible_text('1期')
        time.sleep(1)
        #编辑备注并保存
        remarks = element('//*[@id="textAreaBlank"]')
        remarks.clear()
        remarks.send_keys('通过——自动添加审批备注信息！')
        time.sleep(1)
        element("//button[@class='remarkButton'][contains(text(),'保存')]").click()
        time.sleep(1)
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        dig_alert.accept()
        time.sleep(2)
        '''
        '''
        #审批拒绝
        refuse = element('//*[@id="unPassThrough"]')
        refuse.click()
        #选择拒绝原因
        refuse_reason = element('//*[@id="checkInfo"]/div[5]/ul/li/select')
        Select(refuse_reason).select_by_visible_text('D9----本人放弃类')
        time.sleep(1)
        #编辑备注并保存
        remarks = element('//*[@id="textAreaBlank"]')
        remarks.clear()
        remarks.send_keys('拒绝——自动添加审批备注信息！')
        time.sleep(1)
        element("//button[@class='remarkButton'][contains(text(),'保存')]").click()
        time.sleep(1)
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        dig_alert.accept()
        time.sleep(2)
        #审批拒绝并加入黑名单
        add_black = element('//*[@id="joinBlack"]')
        add_black.click()
        time.sleep(1)
        comfirm = element("//a[contains(text(),'是')]")
        comfirm.click()
        time.sleep(2)
        '''
        #点击提交按钮
        submit_btn = element("//button[contains(text(),'提 交')]")
        submit_btn.click()
        time.sleep(2)
        



        # #从关闭按钮上滑至证明资料
        # close_button = element('//*[@id="report-template"]/div[2]/div[3]/div/div/a')
        # certifi_info = element("/html/body/div[2]/div[2]/div/div/operate-dir/div/ul/li[3]")
        # ActionChains(self.driver).drag_and_drop(close_button, certifi_info).perform()
        # time.sleep(1)
        #
        # #点击运营商数据
        # phone_data = element('//*[@id="report-template"]/ul/li[5]')
        # phone_data.click()
        # time.sleep(2)
        # #点击月份选择
        # mouth_select = element('//*[@id="types"]')
        # Select(mouth_select).select_by_visible_text("2018-10")
        # time.sleep(2)
        # # #如果本月有通话记录：从呼入呼出top10滑动至电话列表
        # # top_num = element('//*[@id="report-template"]/div[2]/span/div/div/div[2]/h2')
        # # phone_list = element('//*[@id="report-template"]/div[2]/span/div/div/div[3]/div[2]/div[1]/table/tbody/tr[7]/td[1]')
        # # ActionChains(driver).drag_and_drop(top_num, phone_list).perform()
        # # time.sleep(1)
        # #从呼入呼出top10滑动至通话详单
        # top_num = element('//*[@id="report-template"]/div[2]/span/div/div/div[2]/h2')
        # tel_detail = element('//*[@id="report-template"]/div[2]/span/div/div/div[5]/div[2]/div[1]/span')
        # ActionChains(self.driver).drag_and_drop(top_num, tel_detail).perform()
        # time.sleep(1)
        # #点击月份选择
        # mouth_select = element('//*[@id="type"]')
        # Select(mouth_select).select_by_visible_text("2018-10")
        # time.sleep(2)
        # #点击通讯录按钮
        # phone_address = element('//*[@id="cellBook"]/h2')
        # phone_address.click()
        # time.sleep(2)
        # #从通讯录滑动至呼入呼出top10
        # phone_address = element('//*[@id="cellBook"]/h2')
        # top_num = element('//*[@id="report-template"]/div[2]/span/div/div/div[2]/h2')
        # ActionChains(self.driver).drag_and_drop(phone_address, top_num).perform()
        # time.sleep(1)
        #
        # #点击审核处理
        # deal_with = element('//*[@id="report-template"]/ul/li[4]')
        # deal_with.click()
        # time.sleep(2)
        # #从审核处理滑动至提交按钮
        # deal_with = element('//*[@id="report-template"]/ul/li[4]')
        # submit_button = element('//*[@id="report-template"]/div[2]/div[4]/div/div[4]/a[1]')
        # ActionChains(self.driver).drag_and_drop(deal_with, submit_button).perform()
        # time.sleep(3)
        # # #点击通过按钮
        # # pass_button = element('//*[@id="passThrough"]')
        # #点击拒绝按钮
        # refuse_button = element('//*[@id="unPassThrough"]')
        # refuse_button.click()
        # time.sleep(1)
        # # #点击加入黑名单
        # # add_black = element('//*[@id="joinBlack"]')
        # # add_black.click()
        # # time.sleep(1)
        # # #点击“是”
        # # yes_button = element('//*[@id="report-template"]/div[3]/div/form/div[2]/a[1]')
        # # yes_button.click()
        # # time.sleep(1)
        # # #点击否
        # # no_button = element('//*[@id="report-template"]/div[3]/div/form/div[2]/a[2]')
        # # no_button.click()
        # # time.sleep(1)
        # #拒绝原因选择
        # refuse_reason = element('//*[@id="checkInfo"]/div[5]/ul/li/select')
        # Select(refuse_reason).select_by_visible_text("D9----本人放弃类")
        # time.sleep(1)
        # #填写备注信息
        # remark_info = element('//*[@id="textAreaBlank"]')
        # remark_info.send_keys("自动测试本人放弃")
        # #点击提交按钮
        # sumbit_button = element('//*[@id="report-template"]/div[2]/div[4]/div/div[4]/a[1]')
        # sumbit_button.click()
        # time.sleep(1)
        # #对alert弹框进行处理
        # # 获取alert对话框
        # dig_alert = self.driver.switch_to.alert
        # time.sleep(1)
        # # 打印警告对话框内容
        # print(dig_alert.text)
        # # alert对话框属于警告对话框，我们这里只能接受弹窗
        # dig_alert.accept()
        # time.sleep(2)
        # #切换至审批页面
        # self.driver.back()
        # time.sleep(2)
        #
        # #点击进件查询
        # case_query = element('//*[@id="slideBar"]/ul/li[2]/a')
        # case_query.click()
        # time.sleep(1)
        # #选择产品
        # select_pro = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select[1]')
        # Select(select_pro).select_by_visible_text("超享贷")
        # #选择进件方式
        # case_meth = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select[2]')
        # Select(case_meth).select_by_visible_text("H5")
        # #选择处理状态
        # deal_status = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/select')
        # Select(deal_status).select_by_visible_text("审核中")
        # #选择来源
        # source = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/select')
        # Select(source).select_by_visible_text("其他")
        # #搜索关键词
        # kw = element('//*[@id="search"]')
        # kw.send_keys("汤文钦")
        # #点击查询按钮
        # query_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[6]/td[2]/div[1]')
        # query_button.click()
        # time.sleep(2)
        # print("搜索案件成功！")
        # #点击案件的查看按钮
        # view_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[12]')
        # view_button.click()
        # time.sleep(2)
        # #点击用户上传信息
        # user_info = element('//*[@id="report-template"]/ul/li[1]')
        # user_info.click()
        # time.sleep(2)
        # #点击系统审核信息
        # sys_info = element('//*[@id="report-template"]/ul/li[2]')
        # sys_info.click()
        # time.sleep(2)
        # #点击证明材料
        # comfirm_info = element('//*[@id="report-template"]/ul/li[3]')
        # comfirm_info.click()
        # time.sleep(2)
        # #点击审核处理
        # case_deal = element('//*[@id="report-template"]/ul/li[4]')
        # case_deal.click()
        # time.sleep(2)
        # #点击运营数据
        # tel_data = element('//*[@id="report-template"]/ul/li[5]')
        # tel_data.click()
        # time.sleep(2)
        # #从运营数据滑动至关闭按钮
        # tel_data = element('//*[@id="report-template"]/ul/li[5]')
        # close_button = element('//*[@id="report-template"]/div[2]/span/div/div/div[6]/a')
        # ActionChains(self.driver).drag_and_drop(tel_data, close_button).perform()
        # time.sleep(1)
        # #点击关闭按钮
        # close_button = element('//*[@id="report-template"]/div[2]/span/div/div/div[6]/a')
        # close_button.click()
        # time.sleep(2)
        # print("查看案件成功")
        #
        # #点击审核结果
        # case_result = element('//*[@id="slideBar"]/ul/li[3]/a')
        # case_result.click()
        # time.sleep(1)
        # #选择产品
        # product = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select')
        # Select(product).select_by_visible_text("聚信达产品")
        # time.sleep(2)
        # #选择审核结果
        # case_result = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/select')
        # Select(case_result).select_by_visible_text("审核通过")
        # time.sleep(1)
        # #选择来源
        # source = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[5]/td[2]/select')
        # Select(source).select_by_visible_text("助力钱包")
        # time.sleep(1)
        # #关键字搜索
        # kw = element('//*[@id="search"]')
        # kw.send_keys("李骢")
        # time.sleep(1)
        # #点击查询按钮
        # query_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[7]/td[2]/div[1]')
        # query_button.click()
        # time.sleep(2)
        # print("搜素案件成功")
        # #点击查看按钮
        # view_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[10]')
        # view_button.click()
        # time.sleep(1)
        # #从详细信息滑动至返回按钮
        # detail_info = element('//*[@id="detailInfo2"]/div')
        # back_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/a')
        # ActionChains(self.driver).drag_and_drop(detail_info, back_button).perform()
        # time.sleep(1)
        # #点击返回按钮
        # back_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/a')
        # back_button.click()
        # print("查看成功")
        # #点击全量导出按钮
        # all_export = element('//*[@id="tableHD"]/button')
        # all_export.click()
        # time.sleep(3)
        # print("全量导出成功")
        #
        # #点击配置中心
        # config_center = element('//*[@id="menu"]/div/ul/li[3]/a')
        # config_center.click()
        # time.sleep(1)
        # #点击产品配置
        # product_config = element('//*[@id="slideBar"]/ul/li[1]/a')
        # product_config.click()
        # time.sleep(2)
        # #点击机构配置
        # organization_config = element('//*[@id="slideBar"]/ul/li[2]/a')
        # organization_config.click()
        # time.sleep(2)
        # #点击流程配置
        # process_config = element('//*[@id="slideBar"]/ul/li[3]/a')
        # process_config.click()
        # time.sleep(2)
        # #点击数据配置
        # data_config = element('//*[@id="slideBar"]/ul/li[4]/a')
        # data_config.click()
        # time.sleep(2)
        #
        # #用户管理
        # user_control = element('//*[@id="menu"]/div/ul/li[2]/a')
        # user_control.click()
        # time.sleep(1)
        # #点击用户管理
        # user_cont = element('//*[@id="slideBar"]/ul/li[1]/a')
        # user_cont.click()
        # time.sleep(2)
        # current_window = self.driver.current_window_handle
        # print(current_window)
        # #新建用户
        # add_user = element('//*[@id="main"]/div[2]/div/div[1]/div[1]/div[2]/a')
        # add_user.click()
        # time.sleep(2)
        # #选择角色
        # role_select = element('//*[@id="roleid"]/div[2]')
        # role_select.click()
        # role_sp = element('//*[@id="roleid"]/div[1]/label[1]/input')
        # role_sp.click()
        # #输入账号
        # account = element('//*[@id="username1"]')
        # account.send_keys("testSp")
        # #输入姓名
        # name = element('//*[@id="realName"]')
        # name.send_keys("自动一条添加")
        # #输入邮箱
        # mail = element('//*[@id="userMail"]')
        # mail.send_keys('tangwenqin@juxinda360.com')
        # #点击保存按钮
        # save_button = element('//*[@id="save"]')
        # save_button.click()
        # time.sleep(2)
        # #获取alert对话框
        # dig_alert = self.driver.switch_to.alert
        # time.sleep(1)
        # # 打印警告对话框内容
        # print(dig_alert.text)
        # # alert对话框属于警告对话框，我们这里只能接受弹窗
        # dig_alert.accept()
        # time.sleep(2)
        # #切换至原来页面
        # self.driver.switch_to_window(current_window)
        # time.sleep(2)
        # self.driver.refresh()
        # time.sleep(1)
        # print("新建账号成功")
        #
        # #点击角色管理
        # user_cont = element('//*[@id="slideBar"]/ul/li[2]/a')
        # user_cont.click()
        # time.sleep(3)
        # #点击新建角色按钮
        # add_role = element('//*[@id="main"]/div[2]/div/div/div/div[1]/div[2]/a')
        # add_role.click()
        # time.sleep(2)
        # #角色ID
        # role_id = element('//*[@id="roleId"]')
        # role_id.send_keys("TSPAA")
        # #角色昵称
        # role_name = element('//*[@id="roleName"]')
        # role_name.send_keys("自动添加审批的")
        # #点击保存按钮
        # save_button = element('//*[@id="btnSave"]')
        # save_button.click()
        # time.sleep(3)
        # print("新建角色成功")
        #
        # #点击黑名单管理
        # black_us = element('//*[@id="menu"]/div/ul/li[1]/a')
        # black_us.click()
        # time.sleep(1)
        # #点击黑名单管理
        # black_uss = element('//*[@id="slideBar"]/ul/li/a')
        # black_uss.click()
        # time.sleep(1)
        # current_window = self.driver.current_window_handle
        # #点击新建名单
        # add_user = element('//*[@id="main"]/div[2]/div/div[1]/div[1]/div[2]/a')
        # add_user.click()
        # time.sleep(1)
        # #输入姓名
        # user_name = element('//*[@id="realName"]')
        # user_name.send_keys("这是测试黑名单")
        # #输入电话
        # tel = element('//*[@id="userTel"]')
        # tel.send_keys("13993339278")
        # #输入备注信息
        # other_info = element('//*[@id="remark"]')
        # other_info.send_keys("自动添加备注信息；自动添加备注信息；自动添加备注信息；自动添加备注信息；")
        # #点击保存按钮
        # save_button = element('//*[@id="save"]')
        # save_button.click()
        # time.sleep(1)
        # #点击dialog中的按钮确定
        # yes = element('//*[@id="main"]/div[2]/div/div/div[4]/div/form/div[2]/a[1]')
        # yes.click()
        # time.sleep(1)
        # #获取alert对话框
        # dig_alert = self.driver.switch_to.alert
        # time.sleep(1)
        # # 打印警告对话框内容
        # print(dig_alert.text)
        # # alert对话框属于警告对话框，我们这里只能接受弹窗
        # dig_alert.accept()
        # time.sleep(2)
        # print("新建黑名单成功！")
        # self.driver.switch_to_window(current_window)
        # time.sleep(1)
        # self.driver.refresh()
        # time.sleep(2)
        #
        # #点击待移入按钮
        # wait_add = element('//*[@id="buttonLists"]/button[3]')
        # wait_add.click()
        # time.sleep(1)
        # #点击第一个案件的备注信息
        # other_info = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[5]/span')
        # other_info.click()
        # time.sleep(2)
        # #点击备注信息中的关闭按钮
        # close_button = element('//*[@id="main"]/div[2]/div/div[1]/div[4]/div/form/div[1]/div')
        # close_button.click()
        # #点击第一个案件的编辑按钮
        # edit_button = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/a[1]')
        # edit_button.click()
        # #修改姓名
        # edit_name = element('//*[@id="realName"]')
        # edit_name.clear()
        # time.sleep(1)
        # edit_name.send_keys("自动更改姓名")
        # #修改电话
        # edit_tel = element('//*[@id="userTel"]')
        # edit_tel.clear()
        # time.sleep(1)
        # edit_tel.send_keys("13666666666")
        # #修改备注信息
        # edit_other_info = element('//*[@id="remark"]')
        # edit_other_info.clear()
        # time.sleep(1)
        # edit_other_info.send_keys("自动测试修改信息！自动测试修改信息！自动测试修改信息！")
        # #点击保存按钮
        # save_button = element('//*[@id="save"]')
        # save_button.click()
        # #点击dialog中的按钮确定
        # yes = element('//*[@id="main"]/div[2]/div/div/div[4]/div/form/div[2]/a[1]')
        # yes.click()
        # time.sleep(1)
        # #获取alert对话框
        # dig_alert = self.driver.switch_to.alert
        # time.sleep(1)
        # # 打印警告对话框内容
        # print(dig_alert.text)
        # # alert对话框属于警告对话框，我们这里只能接受弹窗
        # dig_alert.accept()
        # time.sleep(2)
        # print("修改黑名单成功！")
        # #返回黑名单管理页
        # self.driver.switch_to_window(current_window)
        # time.sleep(1)
        # #点击第一案件的移入按钮
        # delete_button = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/a[2]')
        # delete_button.click()
        # time.sleep(1)
        # #获取alert对话框
        # dig_alert = self.driver.switch_to.alert
        # time.sleep(1)
        # # 打印警告对话框内容
        # print(dig_alert.text)
        # # alert对话框属于警告对话框，我们这里只能接受弹窗
        # dig_alert.accept()
        # time.sleep(3)
        # print('移入黑名单成功！')
        # #在关键字中搜索姓名
        # kw = element('//*[@id="search"]')
        # kw.send_keys('假测')
        # #点击搜索按钮
        # query_button = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]')
        # query_button.click()
        # time.sleep(2)
        # print("搜索成功")

        #关闭浏览器

        self.driver.quit()

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    '''
    引用HTMLTestRunner生成测试报告
    python3和python的HTMLTestRunner有不同，需要修改
    且运行时需要在if语句中，编辑器默认只运行if以上内容
    '''
    # 将测试用例加入到测试容器中——class下def方法
    test_suite.addTest(DaiShen("test_daishen"))
    # 定义个报告存放路径，支持相对路径
    filename = 'C:\\Users\\22648\\Desktop\\las_DaiShen.html'
    # 打开一个文件，将result写入此file中
    fp = open(filename, 'wb')
    # 定义测试报告，打开方式、标题、描述
    runner = HTMLTestRunner(stream=fp, title='审批——待审页面', description='用例执行情况：')
    # 运行测试用例
    runner.run(test_suite)
    # 写完之后必须将fp关闭，否则报告是空的
    fp.close()