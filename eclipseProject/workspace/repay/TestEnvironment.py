#  -*-  coding:utf-8 -*-
#用selenium打开谷歌浏览器
from selenium import webdriver
import time
driver = webdriver.Chrome()
# #用浏览器打开H5网页——有借款状态——还款、展期、修改密码、更改绑定银行卡

#测试环境
driver.get("http://h5.super.com/login")
#请输入手机号
element = driver.find_element_by_xpath("//*[@id='tab1']/div/div[1]/div[2]/p/input")
element.send_keys("13070123277")
#请输入密码
element = driver.find_element_by_xpath("//*[@id='tab1']/div/div[2]/div[2]/p/input")
element.send_keys("abc123")
#点击登录按钮
element = driver.find_element_by_xpath("//*[@id='showModel']")
element.click()
time.sleep(2)

#点击还款按钮
element = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/ul/li[2]/a/span")
element.click()
time.sleep(2)
#点击我要还款按钮
element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/a[1]/div")
element.click()
time.sleep(2)
#点击我要还款按钮中的——还款按钮
element = driver.find_element_by_xpath("/html/body/div/div/button")
element.click()
time.sleep(15)
#点击我要还款按钮中的——返回按钮
element = driver.find_element_by_xpath("/html/body/div/div/header/img")
element.click()
time.sleep(2)
#点击我要展期按钮
element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/a[2]/div/p")
element.click()
time.sleep(1)
#点击我要展期中的——我要展期按钮
element = driver.find_element_by_xpath("/html/body/div/div/button")
element.click()
time.sleep(1)
#点击我要展期中的——返回按钮
element = driver.find_element_by_xpath("/html/body/div/div/header/img")
element.click()
time.sleep(2)
#点击我的还款计划
element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/a[3]/div/p")
element.click()
time.sleep(2)
#点击我的还款计划中的——返回按钮
element = driver.find_element_by_xpath("/html/body/div/div/header/img")
element.click()
time.sleep(2)

#点击签约按钮
element = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/ul/li[3]/a/span")
element.click()
time.sleep(2)
#点击签约按钮中的返回按钮
element = driver.find_element_by_xpath("/html/body/div/div/header/img")
element.click()
time.sleep(2)

#点击我的按钮
element = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/ul/li[4]/a")
element.click()
time.sleep(2)
#点击我的——修改密码
element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/a[1]/div")
element.click()
time.sleep(1)
#点击我的——修改密码——请输入原密码
element = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/p/input")
element.send_keys("abc123")
#点击我的——修改密码——请输入新密码
element = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[2]/p/input")
element.send_keys("abc123")
#点击我的——修改密码——请再次输入新密码
element = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/div[2]/p/input")
element.send_keys("abc123")
#点击我的——修改密码——确定
element = driver.find_element_by_xpath("/html/body/div/div/button")
element.click()
time.sleep(1)
#点击我的——修改密码——修改密码成功的退出按钮
element = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/img")
element.click()
time.sleep(2)
#点击我的——更改绑定银行卡
element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/a[3]/div")
element.click()
time.sleep(2)
#点击我的——更改绑定银行卡——新银行卡号
element = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/input")
element.clear()
element.send_keys("6228480018865092375")
time.sleep(2)
#点击我的——更改绑定银行卡——绑定银行卡按钮
element = driver.find_element_by_xpath("/html/body/div/div/div[2]/p/button")
element.click()
time.sleep(3)

#点击首页
element = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/ul/li[1]/a")
element.click()
time.sleep(2)
#点击首页的借钱按钮
element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/a")
element.click()
time.sleep(2)
#退出浏览器
driver.quit()
