#-*-  coding:utf-8 -*-
import unittest
import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.alert import Alert
import time
import sys
from selenium import webdriver
from distutils.tests import test_suite
from unittest import runner



class test_APP_Manage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 
        
    def test_app_manage(self): 
        self.driver.get("http://fea.super.com/#/")
        self.driver.maximize_window()        
        element = self.driver.find_element_by_xpath
 
        #输入用户名
        username = element("/html/body/div/div/div[2]/div/div/div/form/div[1]/div/div/input") 
        username.send_keys("master")
        #输入密码
        password = element("/html/body/div/div/div[2]/div/div/div/form/div[2]/div/div/input")
        password.send_keys("111111")
        #点击登录按钮
        login = element("/html/body/div/div/div[2]/div/div/div/form/div[3]/div/button")
        login.click()
        time.sleep(2)       

        #点击APP管理
        manage_APP = element("/html/body/div/div/div[1]/ul/li[5]")
        manage_APP.click()
        #点击产品上架管理
        putaway = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span")
        putaway.click()
        time.sleep(2)
        #点击下架按钮
        down_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[8]/button[1]")
        down_button.click()
        #点击确定下架按钮
        down_conf = element("/html/body/div[2]/div/div[3]/button[2]")
        down_conf.click()
        time.sleep(2)
        #点击上架按钮
        putaway_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[8]/button[1]")
        putaway_button.click()
        #点击确认上架按钮
        putaway_conf = element("/html/body/div[2]/div/div[3]/button[2]")
        putaway_conf.click()
        time.sleep(2)
        #获取当前页面的handle
        current_handle = self.driver.current_window_handle
        print(current_handle)
        #点击编辑按钮
        edit_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[8]/button[2]")
        edit_button.click()
        #修改利率
        rate = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[2]/div/div/input")
        rate.clear()
        rate.send_keys("0.2%")
        #修改产品简介
        product_introduce = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[6]/div/div/textarea")
        product_introduce.clear()
        product_introduce.send_keys("这是一个很好很好很好的产品，哈哈哈哈哈哈哈哈哈哈")
        time.sleep(2)
        #拖动鼠标开始位置_产品详情
        source = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[7]/div/div/textarea")
        #将鼠标拖动至保存按钮处
        target = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/div/div/div[3]/button")
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        #修改后台链接
        link = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[12]/div/div/input")
        link.clear()
        link.send_keys("http://baidu.com/")
        #修改后台账号
        username = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[13]/div/div/input")
        username.clear()
        username.send_keys("admin")
        #修改后台密码
        pw = element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[14]/div/div/input")
        pw.clear()
        pw.send_keys("admin")
        #所有页面的句柄
        all_handles = self.driver.window_handles
        print(all_handles)
        #点击保存按钮
        element("/html/body/div/div/div[2]/div[2]/div/div/div[5]/div/div/div[3]/button").click() 
        time.sleep(3)
        #点击短链链接进行跳转
        cli_link = element("/html/body/div/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[7]/a")
        cli_link.click()
        time.sleep(2)
        #跳转回当前句柄
        self.driver.switch_to_window(current_handle)
        time.sleep(2)
        #选择状态
        choose_status = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[1]/select")
        choose_status.click()
        #选择状态为已上架
        status_putaway = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[1]/select/option[2]")
        status_putaway.click()
        #在产品名称中输入“测试的”
        product_name = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/input")
        product_name.send_keys("测试的")
        #点击搜索按钮
        search_button3 = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[2]/button")
        search_button3.click()
        time.sleep(3)
        
        #点击产品数据监控
        element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]").click()
        time.sleep(2)
        #产品名称框
        product_box = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[1]/select")
        product_box.click()
#         #选择产品名称
#         product_name1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[1]/select/option[3]")
#         product_name1.click()
        #点击查询按钮
        element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/button").click()
        time.sleep(2)
        #将鼠标拖动的起始位置
        source = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/button")
        #将鼠标拖动至目标位置
        target = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[4]/table/tr[2]/td[1]")
        #执行拖放操作，显示表格数据
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        time.sleep(5)
        
        #点击产品排名
        product_sequence = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[3]/span")
        product_sequence.click()
        #点击调整按钮
        change_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div")
        change_button.click()
#         #调整第一第二排名
#         num_2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/label[2]/span[1]/span")
#         num_2.click()
#         #点击上移按钮
#         up_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/div[1]")
#         up_button.click()
#         #点击保存按钮
#         save_button2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[3]/button")
#         save_button2.click()
#         # Alert弹框对象
#         a3 = Alert(self.driver)  
#         time.sleep(1)
#         #接受弹框信息并关闭
#         a3.accept()
#         time.sleep(3)
    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    #将测试用例加入到测试容器中
    test_suite.addTest(test_APP_Manage("test_app_manage"))
    #当做报告文件的名称
    filename = 'C:\\result'
    #打开一个文件，将result写入此file中
    fp = open(filename+'.html','wb')
    runner = HTMLTestRunner(stream = fp, title = u"Web UI自动化测试报告", description = u"result:")
    runner.run(test_suite)
    fp.close()