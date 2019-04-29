#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 


class test_product_approval(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
        self.driver.get("http://las.super.com/view/login.html")
        self.driver.maximize_window()        
        element = self.driver.find_element_by_xpath
 
        #输入用户名
        username = element("/html/body/div[2]/div/form/label[1]/div/input") 
        username.send_keys("doris")
        #输入密码
        password = element("/html/body/div[2]/div/form/label[2]/div/input")
        password.send_keys("222222")
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
        accept = element("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[10]")
        accept.click()
        time.sleep(1)
        current_handle1 = self.driver.current_window_handle
        print(current_handle1)
        #如果是点击接单按钮，则需启动64-74行的代码
#         # 获取alert对话框
#         dig_alert = self.driver.switch_to.alert
#         time.sleep(1)
#         # 打印警告对话框内容
#         print(dig_alert.text)
#         # alert对话框属于警告对话框，我们这里只能接受弹窗
#         dig_alert.accept()
#         time.sleep(3)
#         #获取当前页面的handle
#         current_handle2 = self.driver.current_window_handle
#         print(current_handle2)
        #点击用户上传信息
        user_sc_info = element("/html/body/div[2]/div[2]/div/div/operate-dir/div/ul/li[1]")
        user_sc_info.click()
        time.sleep(2)
        #模拟鼠标操作——申请表开始
        approval_table = element('//*[@id="report-template"]/div[2]/div[1]/div/table[1]/th')
        #鼠标拖动至关闭按钮
        close_button = element('//*[@id="report-template"]/div[2]/div[1]/div/div')
        ActionChains(self.driver).drag_and_drop(approval_table, close_button).perform()
        time.sleep(2)
        #鼠标上滑，从关闭按钮开始
        close_button = element('//*[@id="report-template"]/div[2]/div[1]/div/div')
        #上滑至用户上传信息
        user_sc_info = element("/html/body/div[2]/div[2]/div/div/operate-dir/div/ul/li[1]")
        ActionChains(self.driver).drag_and_drop(close_button, user_sc_info).perform()
        time.sleep(2)
        
        #点击系统审核信息
        sys_info = element('//*[@id="report-template"]/ul/li[2]')
        sys_info.click()
        time.sleep(2)
#         #如果审批信息多：从系统审核信息——滑动至关闭按钮
#         sys_info = element('//*[@id="report-template"]/ul/li[2]')
#         close_button = element('//*[@id="report-template"]/div[2]/div[2]/div/div[4]/a')
#         ActionChains(self.driver).drag_and_drop(sys_info, close_button).perform()
#         time.sleep(2)
#         #鼠标上滑，从关闭按钮开始
#         close_button = element('//*[@id="report-template"]/div[2]/div[2]/div/div[4]/a')
#         #上滑至系统审核信息
#         sys_info = element('//*[@id="report-template"]/ul/li[2]')
#         ActionChains(self.driver).drag_and_drop(close_button, sys_info).perform()
#         time.sleep(2)
        
        #点击证明材料
        certifi_info = element("/html/body/div[2]/div[2]/div/div/operate-dir/div/ul/li[3]")
        certifi_info.click()
        time.sleep(2)
        #查看附件信息
        card_info = element('//*[@id="report-template"]/div[2]/div[3]/div/a')
        card_info.click()
        time.sleep(2)
        #从附件信息拖动至关闭按钮
        card_info = element('//*[@id="report-template"]/div[2]/div[3]/div/a')
        #关闭按钮
        close_button = element('//*[@id="report-template"]/div[2]/div[3]/div/div/a')
        ActionChains(self.driver).drag_and_drop(card_info, close_button).perform()
        time.sleep(2)
        #从关闭按钮上滑至证明资料
        close_button = element('//*[@id="report-template"]/div[2]/div[3]/div/div/a')
        certifi_info = element("/html/body/div[2]/div[2]/div/div/operate-dir/div/ul/li[3]")
        ActionChains(self.driver).drag_and_drop(close_button, certifi_info).perform()
        time.sleep(1)
        
        #点击运营商数据
        phone_data = element('//*[@id="report-template"]/ul/li[5]')
        phone_data.click()
        time.sleep(2)
        #点击月份选择
        mouth_select = element('//*[@id="types"]')
        Select(mouth_select).select_by_visible_text("2018-10")
        time.sleep(2)
#         #如果本月有通话记录：从呼入呼出top10滑动至电话列表
#         top_num = element('//*[@id="report-template"]/div[2]/span/div/div/div[2]/h2')
#         phone_list = element('//*[@id="report-template"]/div[2]/span/div/div/div[3]/div[2]/div[1]/table/tbody/tr[7]/td[1]')
#         ActionChains(self.driver).drag_and_drop(top_num, phone_list).perform()
#         time.sleep(1)
        #从呼入呼出top10滑动至通话详单
        top_num = element('//*[@id="report-template"]/div[2]/span/div/div/div[2]/h2')
        tel_detail = element('//*[@id="report-template"]/div[2]/span/div/div/div[5]/div[2]/div[1]/span')
        ActionChains(self.driver).drag_and_drop(top_num, tel_detail).perform()
        time.sleep(1)
        #点击月份选择
        mouth_select = element('//*[@id="type"]')
        Select(mouth_select).select_by_visible_text("2018-10")
        time.sleep(2)
        #点击通讯录按钮
        phone_address = element('//*[@id="cellBook"]/h2')
        phone_address.click()
        time.sleep(2)
        #从通讯录滑动至呼入呼出top10
        phone_address = element('//*[@id="cellBook"]/h2')
        top_num = element('//*[@id="report-template"]/div[2]/span/div/div/div[2]/h2')
        ActionChains(self.driver).drag_and_drop(phone_address, top_num).perform()
        time.sleep(1)
  
        #点击审核处理
        deal_with = element('//*[@id="report-template"]/ul/li[4]')
        deal_with.click()
        time.sleep(2)
        #从审核处理滑动至提交按钮
        deal_with = element('//*[@id="report-template"]/ul/li[4]')
        submit_button = element('//*[@id="report-template"]/div[2]/div[4]/div/div[4]/a[1]')
        ActionChains(self.driver).drag_and_drop(deal_with, submit_button).perform()
        time.sleep(3)
#         #点击通过按钮
#         pass_button = element('//*[@id="passThrough"]')
        #点击拒绝按钮
        refuse_button = element('//*[@id="unPassThrough"]')
        refuse_button.click()
        time.sleep(1)
        #点击加入黑名单
        add_black = element('//*[@id="joinBlack"]')
        add_black.click()
        time.sleep(1)
#         #对dialog弹框进行处理
#         dialog = element('//*[@id="report-template"]/div[3]/div')
#         self.driver.switch_to_window(dialog)
        #点击“是”
        yes_button = element('//*[@id="report-template"]/div[3]/div/form/div[2]/a[1]')
        yes_button.click()
        time.sleep(1)
#         #点击否
#         no_button = element('//*[@id="report-template"]/div[3]/div/form/div[2]/a[2]')
#         no_button.click()
#         time.sleep(1)
        #拒绝原因选择
        refuse_reason = element('//*[@id="checkInfo"]/div[5]/ul/li/select')
        Select(refuse_reason).select_by_visible_text("D9----本人放弃类")
        time.sleep(1)
        #填写备注信息
        remark_info = element('//*[@id="textAreaBlank"]')
        remark_info.send_keys("自动测试本人放弃")
        #点击提交按钮
        sumbit_button = element('//*[@id="report-template"]/div[2]/div[4]/div/div[4]/a[1]')
        sumbit_button.click()
        time.sleep(1)
        #对alert弹框进行处理
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(2)

    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()