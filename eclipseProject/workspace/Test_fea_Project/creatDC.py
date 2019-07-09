#-*-  coding:utf-8 -*-
import pdb
import unittest
import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.alert import Alert
import time
import os
from selenium import webdriver


class dcCreat(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 
        
    def test_creatUser(self): 
        d = self.driver
        self.driver.get("https://fea.juxinda360.com/cn/#/")
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
        userManage = element('//*[@id="app"]/div/div[1]/ul/li[6]')
        userManage.click()
        time.sleep(2)
        #点击贷超用户
        daichaoU = element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]')
        daichaoU.click()
        #点击创建用户
        creatU = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/button')
        creatU.click()
        time.sleep(3)
        #选择落地页为超享借
        loadP = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div/input')
        loadP.click()
        time.sleep(1)
        element('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)
        #输入账号名称
        account = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input')
        account.send_keys('a11')
        #输入平台名称
        plat = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input')
        plat.send_keys('孙悟空')
        #输入初始额度
        amount = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input')
        amount.send_keys('100')
        #输入联系电话
        tel = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input')
        tel.send_keys('13333333333')
        #输入初始密码
        pw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input')
        pw.send_keys('a111111')
        #输入确认密码
        cpw = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input')
        cpw.send_keys('a111111')
        #点击创建按钮
        creatB = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/button[1]')
        creatB.click()
        time.sleep(2)
        #切换至alert
        dig_alert = self.driver.switch_to_alert()
        print(dig_alert)
        time.sleep(1)
        dig_alert.accept()
        
        pdb.set_trace()
        #关闭浏览器
        d.quit()
        
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    '''
                    引用HTMLTestRunner生成测试报告
        python3和python的HTMLTestRunner有不同，需要修改
                    且运行时需要在if语句中，编辑器默认只运行if以上内容
    '''
    #将测试用例加入到测试容器中——class下def方法
    test_suite.addTest(dcCreat("test_creatUser"))
    # 定义个报告存放路径，支持相对路径
    filename = 'C:\\Users\\22648\\Desktop\\test\\creatDaiChao.html'
    #打开一个文件，将result写入此file中
    fp = open(filename,'wb')
    # 定义测试报告，打开方式、标题、描述
    runner = HTMLTestRunner(
        stream = fp, title='数据平台创建贷超用户测试报告', description='用例执行情况：')
    # 运行测试用例
    runner.run(test_suite)
    # 写完之后必须将fp关闭，否则报告是空的
    fp.close()
    
        
        
        
        
        
        
        
        
        