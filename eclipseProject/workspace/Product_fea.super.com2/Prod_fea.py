#  -*-  coding:utf-8 -*-
#用selenium打开谷歌浏览器
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from select import select
from platform import platform
driver = webdriver.Chrome()
element = driver.find_element_by_xpath
#数据平台
driver.get("https://fea.juxinda360.com/cn/#/")
driver.maximize_window()
#输入用户名
element("/html/body/div/div/div[2]/div/div/div/form/div[1]/div/div/input").send_keys("master")
#输入密码
element("/html/body/div/div/div[2]/div/div/div/form/div[2]/div/div/input").send_keys("111111")
#点击登录按钮
element("/html/body/div/div/div[2]/div/div/div/form/div[3]/div/button").click()

time.sleep(2)


##########名单导入页面
#点击导入按钮
# element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button").click()
# # #点击导入模板下载
# # element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[3]/span[2]").click()
# time.sleep(10)


##########案件查询页面
element("/html/body/div/div/div[1]/ul/li[2]").click()
#点击基础案件查询
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span").click()
time.sleep(2)
#点击关键字搜索，输入姓名
element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/input").send_keys("候云飞")
#点击搜索按钮
element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/button").click()
time.sleep(2)

#####点击高级案件查询
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]").click()
time.sleep(2)
#点击关键字搜索，输入姓名
element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/input").send_keys("张三")
#点击搜索按钮
element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/button").click()
time.sleep(5)


##########贷超报表
#点击贷超报表
element("/html/body/div/div/div[1]/ul/li[3]").click()
time.sleep(3)
#点击CPA机构报表
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span").click()
time.sleep(3)
# #平台名称筛选框
# platform = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/span')
# select = Select(platform)
#点击平台名称——哈哈
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[2]').click()
time.sleep(5)
#点击CPC机构报表
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/span").click()
time.sleep(5)
#点击平台名称
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[2]').click()
time.sleep(3)

#点击CPS机构报表
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[3]").click()
time.sleep(5)
#点击平台名称——阿里巴巴
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[4]').click()
time.sleep(3)


#########点击用户管理
element("/html/body/div/div/div[1]/ul/li[4]").click()
time.sleep(5)
#点击贷超用户
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]").click()
time.sleep(3)
#点击创建用户按钮
element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button").click()
time.sleep(1)
#选择落地页
element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div[1]/input").click()
#选择超享借
element("/html/body/div[2]/div[1]/div[1]/ul/li[1]").click()
#输入账号名称
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input").send_keys("chaoxiangjie")
#输入平台名称
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input").send_keys("随你花")
#输入初始额度
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input").send_keys("10")
#输入联系电话
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input").send_keys("13313331333")
#输入初始密码
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input").send_keys("111111")
#输入确认密码
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input").send_keys("111111")
#点击创建按钮
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/button[1]").click()
# #点击返回按钮
# element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/button[2]").click()
time.sleep(2)

#####点击平台用户
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]").click()
time.sleep(2)
#点击创建用户按钮
element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button").click()
time.sleep(1)
#选择角色
element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div[1]/input").click()
#选择角色为贷超统计管理员角色
element("/html/body/div[2]/div[1]/div[1]/ul/li[4]").click()
#输入账号名称
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input").send_keys("dctj")
#输入合作方名称
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input").send_keys("百度")
#输入白名单
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input").send_keys("111.202.41.75")
#输入手机号
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input").send_keys("13313331333")
#输入初始密码
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input").send_keys("111111")
#输入确认密码
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input").send_keys("111111")
#输入充值金额
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/div/input").send_keys("100")
#输入基础数据
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/div/input").send_keys("100")
#输入高级数据
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[10]/div/div/input").send_keys("10")
#点击创建按钮
element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[11]/div/button[1]").click()
# #点击返回按钮
# element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[11]/div/button[2]").click()
time.sleep(2)


#####点击贷超管理
element("/html/body/div/div/div[1]/ul/li[5]").click()
time.sleep(2)
#点击CPA机构按钮
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]").click()
time.sleep(2)
#点击添加机构按钮
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/button/span').click()
#在机构名称中输入机构名——聚划算
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/input').send_keys("天猫")
#点击添加机构中的添加按钮
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button/span').click()
#手动点击确定按钮
time.sleep(3)
#点击冻结按钮
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[5]/span[1]').click()
#点击编辑按钮
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[3]/td[5]/span[2]').click()
#在编辑界面点击“增/减平台”
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/button').click()
#在未分配平台中，选择添加平台
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[1]/div/ul/li[1]').click()
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[2]/button[1]').click()
#点击保存按钮
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button').click()
time.sleep(3)
#点击增/减平台中的编辑按钮
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]/span[1]').click()
#输入系数为0.28
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[4]/input').send_keys("0.28")
#输入价格
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[5]/input').send_keys("10")
#点击保存按钮
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button[1]/span').click()
time.sleep(3)
#点击增/减平台中的冻结按钮
element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]/span[2]').click()
time.sleep(2)
#点击贷超管理页面
element("/html/body/div/div/div[1]/ul/li[5]").click()
time.sleep(10)

#点击CPC机构
element('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]').click()
time.sleep(10)

#点击CPS机构
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[3]/span").click()
time.sleep(2)
time.sleep(10)

#点击退出按钮
element("/html/body/div/div/div[1]/div").click()
driver.quit()