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

class AddProduct(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 
        
    def test_app_manage(self): 
        d = self.driver
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
        
        #点击添加产品
        add_prod = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/button')
        add_prod.click()
        time.sleep(1)
        #输入产品名称
        prod_name = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[1]/div/div/input')
        prod_name.send_keys('猪八戒')
        #产品利率
        prod_rate = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[2]/div/div/input')
        prod_rate.send_keys('0.33%')
        #产品期限
        prod_term = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[3]/div/div[1]/input')
        prod_term.send_keys('7天-1个月')
        #产品额度
        prod_limit = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[4]/div/div[1]/input')
        prod_limit.send_keys('700-2000')
        #产品标签
        prod_lable = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[5]/div/div[1]/label[1]/span[1]/span')
        prod_lable.click()
        #产品类型
        prod_type = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[6]/div/div[1]/label[1]/span[1]/span')
        prod_type.click()
        #产品简介
        prod_introd = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[7]/div/div[1]/textarea')
        prod_introd.send_keys('零门槛，极易秒下')
        #放款时间
        loan_time = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[8]/div/div[1]/textarea')
        loan_time.send_keys('5分钟到账')
        #产品图片
        prod_img = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[9]/div/div/div/div/i')
        prod_img.click()
        #调用上传分机.exe上传程序
        os.system("C:\\Users\\22648\\Desktop\\自动化上传文件\\贷后上传还款图片.exe")
        time.sleep(2)
        #办理流程
        apply_process = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[10]/div/div/textarea')
        apply_process.send_keys('身份证、手机号、银行卡、芝麻分')
        #申请条件
        apply_require = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[11]/div/div/textarea')
        apply_require.send_keys('18周岁以上实名注册手机号')
        #所需材料
        require_info = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[12]/div/div[1]/textarea')
        require_info.send_keys('实名认证，银行卡，通讯录上传')
        #后台链接
        user_link = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[13]/div/div/input')
        user_link.send_keys('https://h5.juxinda360.com/landingPage?sourceid=qoj11dgy')
        #产品链接
        prod_link = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[2]/form/div[16]/div/div[1]/input')
        prod_link.send_keys('https://qiye.aliyun.com/?')
        #点击保存按钮
        save_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div/div/div[3]/button/span')
        save_button.click()
        time.sleep(2)
        #切换至alert并接受
        dig_alert = self.driver.switch_to_alert()
        time.sleep(1)
        print(dig_alert)
#         pdb.set_trace()
        dig_alert.accept()
        time.sleep(2)
#         pdb.set_trace()
        #搜索添加的产品
        search_prod = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/input')
        search_prod.clear()
        search_prod.send_keys('借你花')
        #点击搜索按钮
        search_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/button')
        search_button.click()
        time.sleep(2)
        
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
    test_suite.addTest(AddProduct("test_app_manage"))
    # 定义个报告存放路径，支持相对路径
    filename = 'C:\\Users\\22648\\Desktop\\test\\addProduct.html'
    #打开一个文件，将result写入此file中
    fp = open(filename,'wb')
    # 定义测试报告，打开方式、标题、描述
    runner = HTMLTestRunner(
        stream = fp, title='数据平台添加产品测试报告', description='用例执行情况：')
    # 运行测试用例
    runner.run(test_suite)
    # 写完之后必须将fp关闭，否则报告是空的
    fp.close()
    
        
        
        
        
        
        
        
        
        