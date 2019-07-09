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


class LDY(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://fea.super.com/cn/#/")
        self.driver.maximize_window()

    # @unittest.skip('贷超用户模块)
    def test_luopage(self):
        Lgin.test_login(self)  # 调用登录模块
        time.sleep(1)
        driver = self.driver
        element = driver.find_element_by_xpath
        # 点击用户管理
        userManage = element('//*[@id="app"]/div/div[1]/ul/li[6]')
        userManage.click()
        time.sleep(2)
        # 点击落地页
        page = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[3]')
        page.click()
        time.sleep(1)
        # 点击新建按钮
        new_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/div/button')
        new_btn.click()
        time.sleep(1)
        # 1、输入落地页名称，2、选择产品名称，3、选择额度，4、产品名称关联落地页链接，5、保存
        ldy_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[1]/div/div/input')
        ldy_name.send_keys('我享花随便花')
        pro_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[2]/div/div/div[1]/input')
        pro_name.click()
        time.sleep(1)
        element('/html/body/div[2]/div[1]/div[1]/ul/li[4]').click()
        time.sleep(1)
        amount = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[3]/div/div/div[1]/input')
        amount.click()
        time.sleep(1)
        element('/html/body/div[3]/div[1]/div[1]/ul/li[6]').click()
        time.sleep(1)
        save_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[5]/div/button[1]')
        save_btn.click()
        time.sleep(1)
        dig_alert = self.driver.switch_to_alert()
        dig_alert.accept()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(2)

        # 编辑:1、编辑产品名称，2、编辑额度，3、保存
        edit_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[6]/button[2]/span')
        edit_btn.click()
        edit_pro = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[2]/div/div/div[1]/input')
        edit_pro.click()
        time.sleep(1)
        element('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
        time.sleep(1)
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[3]/div/div/div[1]/input').click()
        time.sleep(1)
        element('/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()
        time.sleep(1)
        save_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/form/div[5]/div/button[1]')
        save_btn.click()
        dig_alert = self.driver.switch_to_alert()
        dig_alert.accept()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(2)

        # 冻结+解冻
        freeze_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[6]/button[1]/span')
        freeze_btn.click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(1)
        unfreeze = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[6]/button[1]/span')
        unfreeze.click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(1)

        # 产品名称+关键字筛选
        pro_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/select')
        Select(pro_name).select_by_visible_text('我要花')
        kwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/input')
        kwd.send_keys('哈哈哈')
        search_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/button[1]')
        search_btn.click()
        time.sleep(1)
        clear_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/button[2]')
        clear_btn.click()
        time.sleep(1)
        print("落地页：新建、编辑、冻结及筛选完成")

        # 关闭浏览器
        driver.quit()

    if __name__ == "__main__":
        test_suite = unittest.TestSuite()



