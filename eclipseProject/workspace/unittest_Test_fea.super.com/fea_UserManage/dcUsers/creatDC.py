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


class DC(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://fea.super.com/cn/#/")
        self.driver.maximize_window()

    # @unittest.skip('贷超用户模块)
    def test_DaiChao(self):
        Lgin.test_login(self)  # 调用登录模块
        time.sleep(1)
        driver = self.driver
        element = driver.find_element_by_xpath
        #点击用户管理
        userManage = element('//*[@id="app"]/div/div[1]/ul/li[6]')
        userManage.click()
        time.sleep(2)
        #点击贷超用户
        daichaoU = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        daichaoU.click()
        time.sleep(1)

        # 创建流量用户-》修改账号及平台名称
        creatLL = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[5]/div/button')
        creatLL.click()
        time.sleep(2)
        # 选择落地页
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div[1]/input').click()
        time.sleep(1)
        element('/html/body/div[2]/div[1]/div[1]/ul/li[3]').click()
        time.sleep(1)
        account = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input')
        account.send_keys('mali')
        platform = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input')
        platform.send_keys('玛丽')
        origin_amount = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div[1]/input')
        origin_amount.send_keys('100')
        tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div[1]/input')
        tel.send_keys('13313331333')
        origin_pwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div[1]/input')
        origin_pwd.send_keys('a111111')
        confirm_pwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div[1]/input')
        confirm_pwd.send_keys('a111111')
        creat_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/button[1]')
        creat_btn.click()
        time.sleep(1)
        # 切换至alert并打印、接受alert
        dig_alert = driver.switch_to_alert()
        print(dig_alert.text)
        dig_alert.accept()
        time.sleep(3)
        print('新建流量用户成功！')

        # 创建贷超用户——>修改账号及平台名称
        creatDC = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[6]/div/button')
        creatDC.click()
        time.sleep(1)
        # 选择平台类型
        plat = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div[1]/input')
        plat.click()
        time.sleep(1)
        element('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)
        account = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input')
        account.send_keys('dog')
        platform = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input')
        platform.send_keys('小黑')
        tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div[1]/input')
        tel.send_keys('13313331333')
        opwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div[1]/input')
        opwd.send_keys('a111111')
        cpwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div[1]/input')
        cpwd.send_keys('a111111')
        creat_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/button[1]')
        # 模拟鼠标滑动至创建按钮处
        ActionChains(driver).move_to_element(creat_btn).perform()
        time.sleep(1)
        creat_btn.click()
        time.sleep(2)
        dig_alert.accept()
        time.sleep(5)
        print('新建贷超用户成功！')
        
        # 搜索当前状态+角色名称+关键字搜索改为新建的流量用户
        status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/select')
        Select(status).select_by_visible_text('未冻结')
        uname = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/select')
        Select(uname).select_by_visible_text('流量用户')
        kwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div/input')
        kwd.send_keys('玛丽')
        search_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[4]/button[1]')
        search_btn.click()
        time.sleep(2)
        clear_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[4]/button[2]')
        clear_btn.click()
        uname = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/select')
        Select(uname).select_by_visible_text('贷超用户')
        search_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[4]/button[1]')
        search_btn.click()
        time.sleep(2)
        clear_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div[4]/button[2]')
        clear_btn.click()
        print('搜索成功！')

        # 编辑用户信息
        edit = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[9]/span[2]/span')
        edit.click()
        time.sleep(1)
        edit_opd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input')
        edit_opd.send_keys('a111111')
        edit_npd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input')
        edit_npd.send_keys('a111111')
        edit_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/button[1]')
        edit_btn.click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(3)
        print('编辑用户成功')

        # 冻结用户
        # 1、点击冻结按钮，选择立即冻结，接受弹框
        freeze = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[9]/span[1]')
        freeze.click()
        time.sleep(1)
        now_freeze = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]')
        now_freeze.click()
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button').click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(3)
        # 2、点击解除按钮，选择立即冻结，接受弹框
        unfreeze = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[9]/span[1]')
        unfreeze.click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(3)
        # 3、点击冻结按钮，选择7天后冻结，接受弹框
        freeze = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[9]/span[1]')
        freeze.click()
        time.sleep(1)
        seven_freeze = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[2]')
        seven_freeze.click()
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button').click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(3)
        print('冻结及解冻用户成功')

        #关闭浏览器
        driver.quit()
        
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    '''
    引用HTMLTestRunner生成测试报告
    python3和python的HTMLTestRunner有不同，需要修改
    且运行时需要在if语句中，编辑器默认只运行if以上内容
    '''
    #将测试用例加入到测试容器中——class下def方
    test_suite.addTest(DC("DaiChao"))
    # 定义个报告存放路径，支持相对路径
    filename = 'C:\\Users\\22648\\Desktop\\test\\DC_User.html'
    #打开一个文件，将result写入此file中
    fp = open(filename, 'wb')
    # 定义测试报告，打开方式、标题、描述
    runner = HTMLTestRunner(stream=fp, title=u'数据平台创建贷超用户测试报告', description='用例执行情况：')
    # 运行测试用例
    runner.run(test_suite)
    # 写完之后必须将fp关闭，否则报告是空的
    fp.close()
