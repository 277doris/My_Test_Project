#  -*-  coding:utf-8 -*-
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.alert import Alert
from selenium import webdriver

class test_NameImport(unittest.TestCase): 
    
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

        #点击名单导入按钮
        ipmort_file = element("/html/body/div/div/div[1]/ul/li[1]")
        ipmort_file.click()
        #点击导入按钮
        import_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button")
        import_button.click()
        #点击导入模板下载
        import_demo = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[3]")
        import_demo.click()
        time.sleep(2)
        #点击导入模块的X
        import_close = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[1]/button")
        import_close.click()
        #点击导出按钮
        export_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]")
        export_button.click()
        time.sleep(2)
        #从排序位置开始
        source = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[1]/th[1]")
        # 结束位置：定位到元素要移动到的目标位置
        target = element("/html/body/div/div/div[2]/div[2]/div/div/div[3]/div/div/span[1]")
        # 执行元素的拖放操作
        ActionChains(self.driver).drag_and_drop(source,target).perform()
        time.sleep(1)
        #进行翻页
        page2 = element("/html/body/div/div/div[2]/div[2]/div/div/div[3]/div/div/ul/li[2]")
        page2.click()
        time.sleep(3)
   
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()  
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()