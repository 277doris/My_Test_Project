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

class DCMan(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://fea.super.com/cn/#/")
        self.driver.maximize_window()

    # 方法名一定要以test开头
    def test_up_manage(self):
        Lgin.test_login(self)  # 调用登录模块
        time.sleep(2)
        driver = self.driver
        element = driver.find_element_by_xpath

        # 点击贷超管理
        dc_mana = element('//*[@id="app"]/div/div[1]/ul/li[4]')
        dc_mana.click()
        time.sleep(2)

        # 点击产品上架管理
        putaway = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        putaway.click()
        time.sleep(2)
        # 点击添加海报
        add_banner = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/button')
        add_banner.click()
        time.sleep(1)
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div/ul/li[3]/div/div').click()
        time.sleep(1)
        # 调用上传banner.exe上传程序
        os.system("C:\\Users\\22648\\Desktop\\test\\自动化上传文件\\数据平台添加产品海报.exe")
        time.sleep(1)
        link = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div/ul/li[3]/input')
        link.clear()
        time.sleep(1)
        link.send_keys('http://h5.super.com/')
        time.sleep(1)
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/div/button[1]').click()
        time.sleep(1)
        dig_alert = self.driver.switch_to_alert()
        dig_alert.accept()
        time.sleep(1)
        dig_alert.accept()
        add_banner = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/button')
        add_banner.click()
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[1]/button/span').click()
        time.sleep(1)

        # 添加产品：修改产品名称+产品链接
        add_pro = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/button')
        add_pro.click()
        time.sleep(1)
        pro_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[1]/div/div/input')
        pro_name.send_keys('京东')
        pro_rate = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[2]/div/div[1]/input')
        pro_rate.send_keys('1%')
        pro_date = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[3]/div/div[1]/input')
        pro_date.send_keys('7')
        pro_amount = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[4]/div/div[1]/input')
        pro_amount.send_keys('1000')
        pro_targe1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[5]/div/div[1]/label[1]/span[1]/span')
        pro_targe1.click()
        pro_targe2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[5]/div/div[1]/label[2]/span[1]/span')
        pro_targe2.click()
        pro_type1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[6]/div/div[1]/label[1]/span[1]/span')
        pro_type1.click()
        pro_type2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[6]/div/div[1]/label[6]/span[1]/span')
        pro_type2.click()
        pro_introduce = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[7]/div/div[1]/textarea')
        pro_introduce.send_keys('自动添加产品的测试简介')
        loan_time = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[8]/div/div[1]/textarea')
        loan_time.send_keys('自动测试')
        element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[9]/div/div[1]/div/div/i').click()
        time.sleep(1)
        # 调用上传banner.exe上传程序
        os.system("C:\\Users\\22648\\Desktop\\test\\自动化上传文件\\数据平台添加产品海报.exe")
        time.sleep(5)
        apply_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[10]/div/div[1]/textarea')
        apply_status.send_keys('自动测试')
        save_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button')
        ActionChains(self.driver).move_to_element(save_btn).perform()
        time.sleep(1)
        apply_condition = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[11]/div/div/textarea')
        apply_condition.send_keys('你好，自动化测试')
        need_info = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[12]/div/div/textarea')
        need_info.send_keys('你好，自动化测试')
        back_link = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[13]/div/div/input')
        back_link.send_keys('https://fanyi.baidu.com/translate?')
        back_account = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[14]/div/div/input')
        back_account.send_keys('test')
        back_pwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[15]/div/div/input')
        back_pwd.send_keys('abc123')
        pro_link = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[16]/div/div/input')
        pro_link.send_keys('https://miaosha.jd.com/pinpailist.html')
        save_btn.click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(5)

        # 点击上架按钮
        upload = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[9]/button[1]/span')
        upload.click()
        time.sleep(2)
        comfirm = element('/html/body/div[2]/div/div[3]/button[2]')
        comfirm.click()
        time.sleep(5)

        # 点击产品短链
        short_link = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[8]/a')
        short_link.click()
        time.sleep(1)
        # 切换窗口至新开的页面
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)
        # 切换窗口回原来的页面，根据索引进行切换
        self.driver.switch_to_window(driver.window_handles[0])
        time.sleep(5)

        # 编辑——编辑短链
        edit_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[9]/button[2]/span')
        edit_btn.click()
        time.sleep(1)
        save_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button')
        ActionChains(self.driver).move_to_element(save_btn).perform()
        time.sleep(1)
        pro_link = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/form/div[16]/div/div/input')
        pro_link.clear()
        time.sleep(1)
        pro_link.send_keys('https://miaosha.jd.com/')
        save_btn.click()
        time.sleep(1)
        dig_alert.accept()
        time.sleep(5)

        # 移除
        remove = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[5]/td[9]/button[3]/span')
        remove.click()
        time.sleep(1)
        comfirm = element('/html/body/div[2]/div/div[3]/button[2]')
        comfirm.click()
        time.sleep(5)

        # 筛选状态+产品名称
        present_status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/select')
        Select(present_status).select_by_visible_text('已上架')
        kwd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div/input')
        kwd.send_keys('京东')
        search_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/button[1]')
        search_btn.click()
        time.sleep(1)
        clear_btn = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/button[2]')
        clear_btn.click()
        time.sleep(5)

        print('产品上架管理：添加产品海报、添加产品、编辑、移除、上架、状态+名称搜索成功！')

        # 关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    test_suite = unittest.TestSuite()