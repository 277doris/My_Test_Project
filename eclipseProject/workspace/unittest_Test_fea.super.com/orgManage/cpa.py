# -*-  coding:utf-8 -*-
import pdb
import unittest
import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from fea_UserManage.login_master import Lgin


class OrgMan(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://fea.super.com/cn/#/")
        self.driver.maximize_window()

    def test_cpa(self):
        Lgin.test_login(self)  # 调用登录模块
        time.sleep(1)
        driver = self.driver
        element = driver.find_element_by_xpath
        # -*-点击机构管理
        org_manage = element("/html/body/div/div/div[1]/ul/li[5]")
        org_manage.click()

        # -*-CPA新增/编辑流量用户
        cpa_org = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        cpa_org.click()
        time.sleep(2)
        # 点击添加流量机构
        add_org = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/button')
        add_org.click()
        time.sleep(1)
        # 输入机构名称
        org_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/input')
        org_name.send_keys('屈层氏')
        time.sleep(1)
        # 选择机构属性
        org_att = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[3]/select')
        Select(org_att).select_by_visible_text('流量用户')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[4]/button').click()
        time.sleep(1)
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        dig_alert.accept()
        time.sleep(2)
        # 筛选机构属性
        org_select = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/select')
        Select(org_select).select_by_visible_text('流量用户')
        time.sleep(1)
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/button[1]').click()
        time.sleep(2)
        # 点击编辑按钮
        edit_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[6]/span[2]')
        edit_btn.click()
        time.sleep(1)
        # 点击增减平台按钮
        add_plat = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/button')
        add_plat.click()
        time.sleep(1)
        # 选择新建的平台
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[1]/div/ul/li').click()
        rig_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[2]/button[1]')
        rig_btn.click()
        save_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button')
        save_btn.click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(1)
        # 编辑流量用户的系数
        editp_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[8]/span[2]')
        editp_btn.click()
        # 注册系数
        log_rate = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[4]/input')
        log_rate.clear()
        log_rate.send_keys('0.45')
        # 放款系数
        loan_rate = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[5]/input')
        loan_rate.clear()
        loan_rate.send_keys('0.45')
        # 单价
        price = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[6]/input')
        price.clear()
        price.send_keys('10')
        time.sleep(1)
        # 生效时间
        effect_time = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[7]/select')
        Select(effect_time).select_by_visible_text('立即生效')
        time.sleep(2)
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button[1]').click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(3)

        # -*-CPA新增/编辑贷超用户
        cpa_org = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        cpa_org.click()
        time.sleep(2)
        # 点击添加贷超机构
        add_org = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/button')
        add_org.click()
        time.sleep(1)
        # 输入机构名称
        org_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/input')
        org_name.send_keys('伊朗')
        time.sleep(1)
        # 选择机构属性
        org_att = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[3]/select')
        Select(org_att).select_by_visible_text('贷超用户')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[4]/button').click()
        time.sleep(1)
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        dig_alert.accept()
        time.sleep(2)
        # 筛选机构属性
        org_select = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/select')
        Select(org_select).select_by_visible_text('贷超用户')
        time.sleep(1)
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/button[1]').click()
        time.sleep(2)
        # 点击编辑按钮
        edit_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[6]/span[2]')
        edit_btn.click()
        # 点击增减平台按钮
        add_plat = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/button')
        add_plat.click()
        time.sleep(1)
        # 选择新建的平台
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[1]/div/ul/li[1]').click()
        rig_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[2]/button[1]')
        rig_btn.click()
        save_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button')
        save_btn.click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(1)
        # 编辑贷超用户的系数
        editp_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[8]/span[2]')
        editp_btn.click()
        # 注册系数
        log_rate = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[4]/input')
        log_rate.clear()
        log_rate.send_keys('0.45')
        # 点击系数
        click_rate = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[5]/input')
        click_rate.clear()
        click_rate.send_keys('0.45')
        # 单价
        price = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[6]/input')
        price.clear()
        price.send_keys('10')
        time.sleep(1)
        # 生效时间
        effect_time = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[7]/select')
        Select(effect_time).select_by_visible_text('立即生效')
        time.sleep(2)
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button[1]').click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(1)

        # -*-CPA新增/编辑贷超及流量用户完成
        cpa_org = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        cpa_org.click()
        time.sleep(2)
        print('CPA新增/编辑贷超及流量用户完成')

    def test_tearDown(self):
        # 关闭浏览器
        self.driver.quit()


if __name__ == "__main__":
    test_suite = unittest.TestSuite()