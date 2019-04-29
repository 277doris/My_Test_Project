#  -*-  coding:utf-8 -*-
import unittest
import time
from selenium import webdriver

class test_Produce_Query(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_Change_card(self):
        #����H5��¼
        #self.driver.get("http://h5.super.com/login")
        self.driver.get("http://h5follow.super.cn/login")
        self.driver.set_window_size(480, 800)
        #���˺š�������е�¼
        element = self.driver.find_element_by_xpath
        phone_numb = element("//*[@id='tab1']/div/div[1]/div[2]/p/input")
        phone_numb.send_keys("13070123277")
        #����������
        user_password = element("//*[@id='tab1']/div/div[2]/div[2]/p/input")
        user_password.send_keys("abc123")
        #�����¼��ť
        element("//*[@id='showModel']").click()
        time.sleep(2)
        #����ҵİ�ť
        my = element("/html/body/div/div/div/div[2]/div/ul/li[4]/a").click()
        time.sleep(2)
        #������Ȳ�ѯ
        produce_query = element("/html/body/div/div/div/div[1]/div[2]/a[2]/div").click()
        time.sleep(2)
 
    def test_tearDown(self):
         #�˳������
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()