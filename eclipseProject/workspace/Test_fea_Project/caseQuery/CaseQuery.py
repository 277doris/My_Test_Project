#  -*-  coding:utf-8 -*-
import unittest
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver
from fea_UserManage.login_master import Lgin

class CaseQuery(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://fea.super.com/cn/#/")
        self.driver.maximize_window()

    def test_caseQuery(self):
        Lgin.test_login(self)  # 调用登录模块
        time.sleep(1)
        driver = self.driver
        element = driver.find_element_by_xpath

        #案件查询页面
        case_query = element("/html/body/div/div/div[1]/ul/li[2]")
        case_query.click()
        #点击基础案件查询
        basic_case = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span")
        basic_case.click()
        #点击关键字搜索，输入姓名
        keyword_query1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/input")
        keyword_query1.send_keys("候云飞")
        #点击搜索按钮
        search_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/button")
        search_button1.click()
        time.sleep(2)
        #点击查看按钮
        view_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[4]/span")
        view_button.click()
        time.sleep(2)

        #点击高级案件查询
        advance_case = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]")
        advance_case.click()
        #点击关键字搜索，输入姓名
        keyword_query2 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/input")
        keyword_query2.send_keys("张三")
        #点击搜索按钮
        search_button2 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/button")
        search_button2.click()
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    test_suite = unittest.TestCase()
