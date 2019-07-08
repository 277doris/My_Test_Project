#-*-  coding:utf-8 -*-
import pdb
import unittest
import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
import time
import os
from selenium import webdriver
from fea_UserManage.login_master import Lgin


class PT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://fea.super.com/cn/#/")
        self.driver.maximize_window()

    # @unittest.skip('贷超用户模块)
    def test_PingTai(self):
        Lgin.test_login(self)  # 调用登录模块
        time.sleep(1)
        driver = self.driver
        element = driver.find_element_by_xpath
        # 点击用户管理
        userManage = element('//*[@id="app"]/div/div[1]/ul/li[6]')
        userManage.click()
        time.sleep(2)
        # 点击平台用户
        pingtaiU = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]')
        pingtaiU.click()
        time.sleep(1)

        # 创建用户——>修改账号名称
        creat_user = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[4]/div/button')
        creat_user.click()
        time.sleep(1)
        # 选择角色
        role = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div[1]/input')
        role.click()
        time.sleep(1)
        element('/html/body/div[2]/div[1]/div[1]/ul/li[3]').click()
        account = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input')
        account.send_keys('bear')
        partner = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input')
        partner.send_keys('熊大')
        white = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input')
        white.send_keys('192.168.1.166')
        tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input')
        tel.send_keys('133133313333')
        origin_pwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input')
        origin_pwd.send_keys('a111111')
        confirm_pwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input')
        confirm_pwd.send_keys('a111111')
        amount = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/div/input')
        amount.send_keys('100')
        basic_data = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/div/input')
        basic_data.send_keys('1')
        advance_data = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[10]/div/div/input')
        advance_data.send_keys('2')
        creat_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[11]/div/button[1]')
        ActionChains(driver).drag_and_drop(origin_pwd, creat_btn).perform()
        creat_btn.click()
        time.sleep(2)
        dig_alert = driver.switch_to_alert()
        dig_alert.accept()
        time.sleep(2)

        # 充值: 1、点击充值按钮，2、输入充值金额，3、点击充值确定
        recharge_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[1]/span[1]')
        recharge_btn.click()
        time.sleep(1)
        recharge_amount = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[4]/input')
        recharge_amount.send_keys('1000')
        recharge = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button[1]')
        recharge.click()
        time.sleep(1)
        '''
        # 分配：1、点击分配按钮，2、输入基础案件/高级案件，3、点击分配确定
        distribution_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[1]/span[2]')
        distribution_btn.click()
        time.sleep(1)
        basic_case = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[7]/input[2]')
        basic_case.clear()
        basic_case.send_keys('2')
        high_case = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[8]/input[2]')
        high_case.clear()
        high_case.send_keys('2')
        distribution = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button[1]')
        distribution.click()
        time.sleep(1)
        '''
        # 冻结
        freeze_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[2]')
        freeze_btn.click()
        time.sleep(2)
        unfreeze = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span')
        unfreeze.click()
        time.sleep(1)
        # 当前状态+关键字的搜索
        present_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/select')
        Select(present_status).select_by_visible_text('未冻结')
        account = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/input')
        account.send_keys('bird')
        search_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/button[1]')
        search_btn.click()
        time.sleep(1)
        # 清空
        clear_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/button[2]')
        clear_btn.click()
        time.sleep(2)
        print("平台用户：新建、充值、分配、冻结及筛选完成")

        # 关闭浏览器
        driver.quit()

    if __name__ == "__main__":
        test_suite = unittest.TestSuite()
        '''
        引用HTMLTestRunner生成测试报告
        python3和python的HTMLTestRunner有不同，需要修改
        且运行时需要在if语句中，编辑器默认只运行if以上内容
        '''
        # 将测试用例加入到测试容器中——class下def方
        test_suite.addTest(PT("test_PingTai"))
        # 定义个报告存放路径，支持相对路径
        filename = 'C:\\Users\\22648\\Desktop\\test\\PT_User.html'
        # 打开一个文件，将result写入此file中
        fp = open(filename, 'wb')
        # 定义测试报告，打开方式、标题、描述
        runner = HTMLTestRunner(stream=fp, title=u'数据平台平台用户测试报告', description='用例执行情况：')
        # 运行测试用例
        runner.run(test_suite)
        # 写完之后必须将fp关闭，否则报告是空的
        fp.close()
















