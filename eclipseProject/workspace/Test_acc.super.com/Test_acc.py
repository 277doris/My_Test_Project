#  -*-  coding:utf-8 -*-
#用selenium打开谷歌浏览器
from selenium import webdriver
import time
driver = webdriver.Chrome()
element = driver.find_element_by_xpath
#打开账务系统
driver.get("http://acc.super.com/login.html")
driver.maximize_window()
#输入账号、密码进行登录
#账号
element("//*[@id='uesrname']").send_keys("admin")
#密码
element("//*[@id='password']").send_keys("111111")
#验证码
element("//*[@id='yzm']").send_keys("spxt")
#点击登录按钮
element("//*[@id='loginBtn']").click()
time.sleep(2)

#点击账务信息
element("//*[@id='bar1']/ul/li[3]/a").click()
time.sleep(5)

#在“关键字”搜索中输入姓名——汤文钦
element("//*[@id='search']").send_keys("汤文钦")
time.sleep(2)
#点击“查询"按钮
element("//*[@id='main']/div[2]/div/div/div[2]/div[2]/table/tbody/tr[5]/td[2]/div[1]").click()
time.sleep(5)
#点击“清空”按钮
element("//*[@id='main']/div[2]/div/div/div[2]/div[2]/table/tbody/tr[5]/td[2]/div[2]").click()
time.sleep(2)
#点击借款人账务信息中的查看按钮
element("//*[@id='main']/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[3]/td[11]/a").click()
time.sleep(10)
#点击借款人账务信息中的查看页面的“返回”按钮
element("//*[@id='main']/div[2]/div/div/div[1]/div[5]/a[3]").click()
time.sleep(5)

#点击借款人账务信息中的“全量导出”按钮
element("//*[@id='tableHD']/span[1]/download-btn").click()
time.sleep(5)

#退出浏览器
driver.quit()

