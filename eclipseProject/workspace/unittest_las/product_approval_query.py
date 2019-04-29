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
        
        #点击进件查询
        case_query = element('//*[@id="slideBar"]/ul/li[2]/a')
        case_query.click()
        time.sleep(1)
        #选择产品
        select_pro = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select[1]')
        Select(select_pro).select_by_visible_text("超享贷")
        #选择进件方式
        case_meth = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select[2]')
        Select(case_meth).select_by_visible_text("H5")
        #选择处理状态
        deal_status = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/select')
        Select(deal_status).select_by_visible_text("审核中")
        #选择来源
        source = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/select')
        Select(source).select_by_visible_text("其他")
        #搜索关键词
        kw = element('//*[@id="search"]')
        kw.send_keys("汤文钦")
        #点击查询按钮
        query_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[6]/td[2]/div[1]')
        query_button.click()
        time.sleep(2)
        print("搜索案件成功！")
        #点击案件的查看按钮
        view_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[12]')
        view_button.click()
        time.sleep(2)
        #点击用户上传信息
        user_info = element('//*[@id="report-template"]/ul/li[1]')
        user_info.click()
        time.sleep(2)
        #点击系统审核信息
        sys_info = element('//*[@id="report-template"]/ul/li[2]')
        sys_info.click()
        time.sleep(2)
        #点击证明材料
        comfirm_info = element('//*[@id="report-template"]/ul/li[3]')
        comfirm_info.click()
        time.sleep(2)
        #点击审核处理
        case_deal = element('//*[@id="report-template"]/ul/li[4]')
        case_deal.click()
        time.sleep(2)
        #点击运营数据
        tel_data = element('//*[@id="report-template"]/ul/li[5]')
        tel_data.click()
        time.sleep(2)
        #从运营数据滑动至关闭按钮
        tel_data = element('//*[@id="report-template"]/ul/li[5]')
        close_button = element('//*[@id="report-template"]/div[2]/span/div/div/div[6]/a')
        ActionChains(self.driver).drag_and_drop(tel_data, close_button).perform()
        time.sleep(1)
        #点击关闭按钮
        close_button = element('//*[@id="report-template"]/div[2]/span/div/div/div[6]/a')
        close_button.click()
        time.sleep(2)
        print("查看案件成功")
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()