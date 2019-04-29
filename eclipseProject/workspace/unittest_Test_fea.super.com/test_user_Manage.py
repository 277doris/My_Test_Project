#-*-  coding:utf-8 -*-
import unittest
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.alert import Alert
import time
from selenium import webdriver

class test_user_Manage(unittest.TestCase):
    
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

        #点击用户管理
        user_manage = element("/html/body/div/div/div[1]/ul/li[6]")
        user_manage.click()
        time.sleep(2)
        #点击贷超用户
        daichao_user = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]")
        daichao_user.click()
        #点击解除冻结按钮
        unfreeze_button2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[1]")
        unfreeze_button2.click()
        time.sleep(2)
        #点击编辑按钮
        edit_button2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[2]/span")
        edit_button2.click()
        #重置密码
        reset_pw = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input")
        reset_pw.send_keys("a111111")
        #确认密码
        conf_pw2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div[1]/input")
        conf_pw2.send_keys("a111111")
        #点击修改按钮
        modifier_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/button[1]")
        modifier_button.click()
        # 直接实例化Alert对象
        a3 = Alert(self.driver)  
        time.sleep(1)
        #接受弹框信息并关闭
        a3.accept()
        time.sleep(3)
        #点击创建用户按钮
        new_user = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button")
        new_user.click()
        time.sleep(2)
        #选择落地页
        choose_page = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div[1]/input")
        choose_page.click()
        time.sleep(1)
        #选择超享借
        choose_chaoxiangjie = element("/html/body/div[2]/div[1]/div[1]/ul/li[1]").click()
        time.sleep(2)
        #输入账号名称
        account = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input")
        account.send_keys("chaoxiangjie")
        #输入平台名称
        platform_name4 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input")
        platform_name4.send_keys("随你花")
        #输入初始额度
        init_amount = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input")
        init_amount.send_keys("10")
        #输入联系电话
        tel = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input")
        tel.send_keys("13313331333")
        #输入初始密码
        init_pw = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input")
        init_pw.send_keys("a111111")
        #输入确认密码
        conf_pw = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input")
        conf_pw.send_keys("a111111")
        #点击创建按钮
        creat_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/button[1]")
        creat_button.click()
        time.sleep(2)
        # 直接实例化Alert对象
        a3 = Alert(self.driver)  
        time.sleep(1)
        #接受弹框信息并关闭
        a3.accept()
        time.sleep(3)
        
        #点击平台用户
        platform_user = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]")
        platform_user.click()
        time.sleep(2)
        #d点击充值按钮
        recharge_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[1]/span[1]")
        recharge_button.click()
        #输入充值金额
        recharge_amount = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/p[4]/input")
        recharge_amount.send_keys("100")
        #点击充值按钮
        recharge_button1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[3]/button[1]")
        time.sleep(2)
        recharge_button1.click()
        time.sleep(2)
        #点击分配按钮
        distribution_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[1]/span[2]")
        distribution_button.click()
        #分配基本案件——10
        basic_case_num = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/p[7]/input[2]")
        basic_case_num.clear()
        basic_case_num.send_keys("2")
        #分配高级案件——20
        advance_case_num = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/p[8]/input[2]")
        advance_case_num.clear()
        advance_case_num.send_keys("2")
        #点击分配按钮
        distribution_button1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[3]/button[1]")
        time.sleep(2)
        distribution_button1.click()
        time.sleep(2)
        #点击第二个平台的冻结按钮
        freeze_button2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[3]/td[7]/span[2]")
        freeze_button2.click()
        time.sleep(2)
        #点击解除冻结按钮
        unfreeze_button3 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[3]/td[7]/span")
        unfreeze_button3.click()
        time.sleep(2)
        #点击创建用户按钮
        creat_user = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button")
        creat_user.click()
        time.sleep(2)
        #选择角色
        role = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div[1]/input")
        role.click()
        time.sleep(2)
        #选择角色为贷超统计管理员角色
        role_manage4 = element("/html/body/div[2]/div[1]/div[1]/ul/li[4]").click()
        time.sleep(2)
        #输入账号名称
        uesr_name = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input")
        uesr_name.send_keys("dctj")
        #输入合作方名称
        partner_name = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input")
        partner_name.send_keys("百度")
        #输入白名单
        white_name = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input")
        white_name.send_keys("111.202.41.75")
        #输入手机号
        tel1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input")
        tel1.send_keys("13313331333")
        #输入初始密码
        init_pw1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input")
        init_pw1.send_keys("a111111")
        #输入确认密码
        conf_pw1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input")
        conf_pw1.send_keys("a111111")
        #输入充值金额
        recharge = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/div/input")
        recharge.send_keys("100")
        #输入基础数据
        basic_data = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/div/input")
        basic_data.send_keys("100")
        #输入高级数据
        advance_data = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[10]/div/div/input")
        advance_data.send_keys("10")
        #点击创建按钮
        creat_button1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[11]/div/button[1]")
        creat_button1.click()
        # #点击返回按钮
        back_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[11]/div/button[2]")
        back_button.click()
        time.sleep(2)
    
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()