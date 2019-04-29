#-*-  coding:utf-8 -*-
import time
import unittest
import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 

class Source(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        
    def test_black_user(self):    
        self.driver.get("http://call.super.com/#/")  
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #输入用户名      
        username = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input')
        username.send_keys("admin")
        #输入密码
        pw = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input')
        pw.send_keys("111111")
        #点击登录按钮
        login_button = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[3]/div/button')
        login_button.click()
        time.sleep(1)
        
        #点击客户管理
        custom_manage = element('//*[@id="app"]/div/section/section/div/aside/ul/li[4]/div')
        custom_manage.click()
        time.sleep(1)
        #点击黑名单
        black_list = element('//*[@id="app"]/div/section/section/div/aside/ul/li[4]/ul/li/ul/li[1]')
        black_list.click()
        time.sleep(1)
        #关键字搜索
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("汤")
        #输入增加人姓名
        add_name = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[2]/input')
        add_name.send_keys("外呼专员")
        #输入添加时间
        add_time1 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div[1]/input')
        add_time1.send_keys('2019-01-08 17:15')
        add_time2 = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[3]/div[2]/input')
        add_time2.send_keys('2019-03-18 17:15')
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(2)
        print("客户管理——黑名单——查询黑名单成功")
        
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[2]')
        clear_button.click()
        time.sleep(2)
        
        #听黑名单中的录音并删除黑名单用户
        #1、在关键字中输入汤   
        key_word = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[1]/div[1]/input')
        key_word.send_keys("汤")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[1]')
        query_button.click()
        time.sleep(1)
        #2、听录音
        tape_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[6]/img[2]')
        tape_button.click()
        time.sleep(2)
        #点击关闭录音页面
        close_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[3]/div/div/div[1]/div[2]/img')
        close_button.click()
        time.sleep(2)
        #3、单选用户
        radio_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[2]/table/tr[2]/td[1]/img[1]')
        radio_button.click()
        #4、删除已选用户
        delete_button = element('//*[@id="app"]/div/section/section/main/div/div/div/div/div[1]/div[2]/div/button[3]')
        delete_button.click()
        time.sleep(2)
        #获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        # 打印警告对话框内容
        print(dig_alert.text)
        # alert对话框属于警告对话框，我们这里只能接受弹窗
        dig_alert.accept()
        time.sleep(2)
        print("客户管理——黑名单——删除黑名单成功")
        
        print("客户管理——黑名单测试通过")
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    '''
                    引用HTMLTestRunner生成测试报告
        python3和python的HTMLTestRunner有不同，需要修改
                    且运行时需要在if语句中，编辑器默认只运行if以上内容
    '''
    #将测试用例加入到测试容器中——class下def方法
    test_suite.addTest(Source("test_black_user"))
    # 定义个报告存放路径，支持相对路径
    filename = 'C:\\Users\\22648\\Desktop\\test\\BlackUser.html'
    #打开一个文件，将result写入此file中
    fp = open(filename,'wb')
    # 定义测试报告，打开方式、标题、描述
    runner = HTMLTestRunner(
        stream = fp, title='黑名单测试报告', description='用例执行情况：')
    # 运行测试用例
    runner.run(test_suite)
    # 写完之后必须将fp关闭，否则报告是空的
    fp.close()
    
