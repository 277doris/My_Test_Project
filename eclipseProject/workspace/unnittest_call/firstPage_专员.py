#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select



class test_firstPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://call.super.com/#/")  
        self.driver.maximize_window()  
        element = self.driver.find_element_by_xpath
        #输入外呼专员——账号和密码进行登录，用户名       
        element('//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/input').send_keys("mz")
        element('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/input').send_keys("111111")
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
        #专员输入申请名单的信息，输入提取个数
        element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[3]/div/div/div[2]/input').send_keys(6)
        #点击提交任务按钮
        element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[3]/div/div/div[2]/div/button').click()
        time.sleep(2)
        
        print("首页测试通过")
        
        #点击工作台
        workplace = element('//*[@id="app"]/div/section/section/div/aside/ul/li[1]/ul/li/ul/li[2]')
        workplace.click()
        time.sleep(1)
        #点击拨打电话按钮
        call_button = element('//*[@id="app"]/div/section/section/main/div/div/div[2]/div/div[2]/table/tr[5]/td[6]/img[1]')
        call_button.click()
        time.sleep(2)
        #修改左侧对应客户的外呼详情
        #外呼状态
        call_status = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/select')
        Select(call_status).select_by_visible_text('有意向')
        #微信状态
        chat_status = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/select')
        Select(chat_status).select_by_visible_text('已添加')
        #外呼备注
        new_marked = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[3]/textarea')
        new_marked.send_keys('自动插入一条外呼备注')
        #查看历史外呼备注
        history_marked = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[3]/span[2]/img')
        history_marked.click()
        #选择话术
        product_introduce = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[4]/div/select')
        Select(product_introduce).select_by_visible_text('酸酸乳')
        #选择放款产品
        loan_product = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[5]/div[2]/ul/li/div/div[1]/select')
        Select(loan_product).select_by_visible_text('酸酸乳')
        #上传放款截图
        upload_img = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[5]/div[2]/ul/li/div/div[2]/div/div/button')
        upload_img.click()
        
        #点击保存按钮
        save_button = element('//*[@id="app"]/div/section/section/main/div/div/div[1]/div/div[2]/div[5]/div[3]/button')
        save_button.click()
        time.sleep(2)
        
        
        
        
    def test_tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()