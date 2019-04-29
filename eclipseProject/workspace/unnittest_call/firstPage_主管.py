#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from HTMLTestRunner import HTMLTestRunner


class Source(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        
    def test_first_page(self):
        self.driver.get("http://call.super.com/#/")  
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
#         #1、输入管理员——账号和密码进行登录，用户名      
#         element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input').send_keys("admin")
#         element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input').send_keys("111111")
        #2、输入机构管理员——账号和密码进行登录，用户名      
        element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input').send_keys("m1")
        element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input').send_keys("111111")
#         #3、输入外呼主管——账号和密码进行登录，用户名      
#         element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input').send_keys("mm1")
#         element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input').send_keys("111111")
        #点击登录按钮
        
        login_button = element('//*[@id="app"]/div/div[2]/div/div/div/form/div[3]/div/button')
        login_button.click()
        time.sleep(1)    
        
        #点击工作台——首页
        first_page = element('//*[@id="app"]/div/section/section/div/aside/ul/li[1]/ul/li/ul/li')
        first_page.click()
        time.sleep(2)
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[1]/select')
        Select(loan_product).select_by_visible_text("酸酸乳")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[1]')
        query_button.click()
        time.sleep(2)
        
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[1]/select')
        Select(loan_product).select_by_visible_text("酸酸乳")
        #操作时间控件
        date1 = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/input')
        date1.send_keys("2019-02-25")
        date2 = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input')
        date2.send_keys("2019-02-25")
        #输入任务名称
        task_name = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[1]/div[3]/input')
        task_name.send_keys("蒙牛任务2")
        #点击查询按钮
        query_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[1]')
        query_button.click()
        time.sleep(2)
        #点击清空按钮
        clear_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[2]')
        clear_button.click()
        time.sleep(2)
        
        #筛选饼图数据
        pic_date = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[1]/div[1]/input')
        pic_date.clear()
        pic_date.send_keys('2018-12-26')
        #点击空白处消失
        element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[2]/table/tr[1]/th[3]').click()
        time.sleep(5)
        
        #点击申请名单按钮
        apply_name = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[3]')
        apply_name.click()
        time.sleep(2)
        
        print("首页测试通过")
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    #引入HTMLtestrunner生成测试报告，python3与2有不同，需要修改代码，且运行时需要放在if语句中，编辑器默认只运行if以上的内容
    #将测试用例加入到测试容器中
    test_suite.addTest(Source("test_first_page"))
    #定义个报告存放路径，支持相对路径
    filename = 'C:\\Users\\22648\\Desktop\\test\\FirstPage.html'
    #打开一个文件，将result写入此file中
    fp = open(filename, 'wb')
    #定义测试报告的打开方式、标题、描述
    runner = HTMLTestRunner(
        stream = fp, title = '首页测试报告', description = '用例执行情况:' )
    #运行测试用例
    runner.run(test_suite)
    #写完之后必须将fp关闭，否则报告是空的
    fp.close()
    
    
    