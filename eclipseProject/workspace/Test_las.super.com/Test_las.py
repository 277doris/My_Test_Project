#  -*-  coding:utf-8 -*-
#用selenium打开谷歌浏览器
from selenium import webdriver
import time
driver = webdriver.Chrome()
#打开审批系统
driver.get("http://las.super.com/view/login.html")
driver.maximize_window()
#点击登录系统的进行登录操作
#账号
element = driver.find_element_by_xpath
element("/html/body/div[2]/div/form/label[1]/div/input").send_keys("doris")
#密码
element("/html/body/div[2]/div/form/label[2]/div/input").send_keys("222222")
#验证码
element("/html/body/div[2]/div/form/label[3]/div/input").send_keys("spxt")
#点击登录按钮
element("/html/body/div[2]/div/form/button").click()
time.sleep(5)

#点击产品审批
element("//*[@id='menu']/div/ul/li[3]/a").click()

#点击待审
element("//*[@id='slideBar']/ul/li[1]/a").click()
time.sleep(5)

#点击进件查询
element("//*[@id='slideBar']/ul/li[2]/a").click()
time.sleep(5)

#点击进件查询中的“查看”按钮，进入用户上传信息页面
element("//*[@id='main']/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[11]/a").click()
time.sleep(5)
#进入查看页面，点击系统审核信息
element("//*[@id='report-template']/ul/li[2]").click()
time.sleep(5)
#进入查看页面，点击证明材料
element("//*[@id='report-template']/ul/li[3]").click()
time.sleep(5)
#点击证明材料中的“查看附件”按钮
element("//*[@id='report-template']/div[2]/div[3]/div/a").click()
time.sleep(10)

#进入查看页面，点击审核处理
element("//*[@id='report-template']/ul/li[4]").click()
time.sleep(10)
#进入查看页面，点击运营商数据
element("//*[@id='report-template']/ul/li[5]").click()
time.sleep(5)
#点击运营商数据中的“关闭”按钮
element("//*[@id='report-template']/div[2]/span/div/div/div[6]/a[2]").click()
time.sleep(5)

#点击审核结果
element("//*[@id='slideBar']/ul/li[3]/a").click()
time.sleep(10)

driver.quit()
