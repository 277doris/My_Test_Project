# -*- coding: UTF-8 -*-
# 打开谷歌浏览器
from selenium import webdriver
import time
time.sleep(3)
driver = webdriver.Chrome()
driver.get('http://fea.super.com/#/')
ele = driver.find_element_by_xpath
# 账号
ele('//*[@id="app"]/div/div[2]/div/div[2]/div/form/div[1]/div/div/input').send_keys('master')
#密码
ele('//*[@id="app"]/div/div[2]/div/div[2]/div/form/div[2]/div/div/input').send_keys('111111')
#点击登录按钮
ele('//*[@id="app"]/div/div[2]/div/div[2]/div/form/div[3]/div/button').click()
#点击用户管理按钮
ele('//div[@id="app"]/div/div/ul/li[3]').click()
#点击创建用户按钮
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/button/span').click()
#点击选择角色按钮
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div/span/span/i').click()
#点击导入角色按钮
ele('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
#创建账号名称
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input').send_keys('da')
#创建合作方名称
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input').send_keys('1')
#创建白名单
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input').send_keys('118.186.229.73')
#输入手机号
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input').send_keys('13313331333')
#输入初始密码
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input').send_keys('abc123')
#确认密码
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input').send_keys('abc123')
#输入充值金额
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/div/input').send_keys('100')
#输入基础数据价格
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/div/input').send_keys('1')
#输入高级数据价格
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[10]/div/div/input').send_keys('2')
#点击创建按钮
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/form/div[11]/div/button[1]').click()
#判断用户是否创建成果
ele('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[27]/td[2]').is_displayed()
True

