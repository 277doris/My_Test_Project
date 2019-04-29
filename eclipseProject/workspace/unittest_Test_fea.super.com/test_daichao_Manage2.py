#-*-  coding:utf-8 -*-
import unittest
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver

class test_daichao_Manage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  
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

        #点击贷超管理
        manage_daichao = element("/html/body/div/div/div[1]/ul/li[4]")
        manage_daichao.click()
        time.sleep(2)
        #点击CPA机构按钮
        click_CPA = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span")
        click_CPA.click()
        time.sleep(2)
        #点击冻结按钮
        freeze_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[5]/span[1]")
        freeze_button.click()
        time.sleep(2)
        #点击解除冻结按钮
        unfreeze_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[5]/span")
        unfreeze_button.click()
        time.sleep(2)
        #点击编辑按钮
        edit_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[5]/span[2]")
        edit_button.click()
        time.sleep(2)
        #点击增减平台按钮
        manage_platform = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button")
        manage_platform.click()
        time.sleep(2)
        #选择添加第一个平台
        add_platform1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[1]/div/ul/li[1]")
        add_platform1.click()
        add_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[2]/button[1]")
        add_button.click()
        #点击保存按钮，获取alter弹框
        save_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button")
        save_button.click()
        # 直接实例化Alert对象
        a1 = Alert(self.driver)  
        time.sleep(1)
        #接受弹框信息并关闭
        a1.accept()
        time.sleep(1)
        #点击平台中冻结按钮
        freeze_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]/span[1]")
        freeze_button1.click()
        time.sleep(2)
        #点击平台中解除冻结按钮
        unfreeze_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]/span")
        unfreeze_button1.click()
        time.sleep(2)
        #点击编辑按钮
        edit_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]/span[2]")
        edit_button1.click()
        time.sleep(2)
        #设置编辑页面的系数
        edit_num = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[4]/input")
        edit_num.send_keys("1")
        #设置编辑页面的价格
        edit_price = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[5]/input")
        edit_price.send_keys("2")
        #点击保存按钮
        save_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button[1]")
        save_button1.click()
        # 直接实例化Alert对象
        a2 = Alert(self.driver)  
        time.sleep(1)
        #接受弹框信息并关闭
        a2.accept()
        time.sleep(1)
        
        #点击CPC机构
        CPC_statement1 = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/span")
        CPC_statement1.click()
        time.sleep(3)
        #点击CPS机构
        CPS_statement1 = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[3]/span")
        CPS_statement1.click()
        time.sleep(2)

    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()