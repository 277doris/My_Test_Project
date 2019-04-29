#  -*-  coding:utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome()
element = driver.find_element_by_xpath
#测试环境
driver.get("https://h5.juxinda360.com/login")
#请输入手机号
element("//*[@id='tab1']/div/div[1]/div[2]/p/input").send_keys("13070123277")
#逾期用户账号
#element.send_keys("15310020993")
# #请输入密码
element("//*[@id='tab1']/div/div[2]/div[2]/p/input").send_keys("abc123")
#逾期用户密码
#element.send_keys("a673336")
#点击登录按钮
element("//*[@id='showModel']").click()
time.sleep(5)
driver.maximize_window()
#点击还款按钮
element("/html/body/div/div/div/div[2]/div/ul/li[2]/a/span").click()
time.sleep(2)
#点击我要还款按钮
element("/html/body/div/div/div/div[1]/div[2]/div/a[1]/div").click()
time.sleep(3)
#点击我要还款按钮中的——还款按钮
element("/html/body/div/div/button").click()
time.sleep(15)
#点击我要还款按钮中的——返回按钮
element("/html/body/div/div/header/img").click()
time.sleep(2)
#点击我要展期按钮
element("/html/body/div/div/div/div[1]/div[2]/div/a[2]/div/p").click()
time.sleep(1)
#点击我要展期中的——我要展期按钮
element("/html/body/div/div/button").click()
time.sleep(1)
#点击我要展期中的——返回按钮
element("/html/body/div/div/header/img").click()
time.sleep(2)
#点击我的还款计划
element("/html/body/div/div/div/div[1]/div[2]/div/a[3]/div/p").click()
time.sleep(2)
#点击我的还款计划中的——返回按钮
element("/html/body/div/div/header/img").click()
time.sleep(2)
 
#点击签约按钮
element("/html/body/div/div/div/div[2]/div/ul/li[3]/a/span").click()
time.sleep(2)
#点击签约按钮中的返回按钮
element("/html/body/div/div/header/img").click()
time.sleep(2)
 
#点击我的按钮
element("/html/body/div/div/div/div[2]/div/ul/li[4]/a").click()
time.sleep(2)
#点击我的——修改密码
element("/html/body/div/div/div/div[1]/div[2]/a[1]/div").click()
time.sleep(1)
#点击我的——修改密码——请输入原密码
element("/html/body/div/div/div[1]/div[1]/div[2]/p/input")
element.send_keys("abc123")
#点击我的——修改密码——请输入新密码
element("/html/body/div/div/div[1]/div[2]/div[2]/p/input")
element.send_keys("abc123")
#点击我的——修改密码——请再次输入新密码
element("/html/body/div/div/div[1]/div[3]/div[2]/p/input")
element.send_keys("abc123")
#点击我的——修改密码——确定
element("/html/body/div/div/button").click()
time.sleep(1)
#点击我的——修改密码——修改密码成功的退出按钮
element("/html/body/div/div/div[2]/div/img").click()
time.sleep(2)
#点击我的——更改绑定银行卡
element("/html/body/div/div/div/div[1]/div[2]/a[3]/div").click()
time.sleep(2)
#点击我的——更改绑定银行卡——新银行卡号
element("/html/body/div/div/div[2]/div[1]/div[2]/input").clear()
element.send_keys("6228480018865092375")
time.sleep(2)
#点击我的——更改绑定银行卡——绑定银行卡按钮
element("/html/body/div/div/div[2]/p/button").click()
time.sleep(5)

#点击首页
element("/html/body/div/div/div/div[2]/div/ul/li[1]/a").click()
time.sleep(2)
#点击首页的借钱按钮
element("/html/body/div/div/div/div[1]/div/a").click()
time.sleep(2)

#点击上传身份证正面
element("/html/body/div/div/div[1]/div/div/div/div/label[1]").click()
element.send_keys("C:\\Users\\22648\\Desktop\\IDcard\\1.jpg")

time.sleep(10)


#点击产品审批系统
#退出浏览器
driver.quit()
