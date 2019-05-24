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