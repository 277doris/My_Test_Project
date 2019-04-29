#  -*-  coding:utf-8 -*-
#用selenium打开谷歌浏览器
from selenium import webdriver
import time
driver = webdriver.Chrome()
##########打开贷后系统
driver.get("http://dscp.juxinda360.com/#/")
driver.maximize_window()

#输入账号、密码、验证码进行登录操作
#输入账号
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div[2]/form/div[1]/div/div/input").send_keys("zhengyufei")
#输入密码
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div[2]/form/div[2]/div/div/input").send_keys("111111")
#输入验证码
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div[2]/form/div[3]/div/div/input").send_keys("dscp")
#点击登录按钮
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div[2]/form/div[4]/div/button/span").click()
time.sleep(2)

##########进入我的工作台，进入全部案件
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div/ul/li[1]/span").click()
time.sleep(2)
#点击应还款日期
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input").click()
time.sleep(3)
#选择还款状态
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select").click()
# #选择还款状态为“已结清”
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select/option[3]').click()
# time.sleep(1)

# #选择电话状态
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select").click()
# #选择电话状态为来电提醒
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select/option[6]").click()
# time.sleep(1) 
# #选择案件跟进状态
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select").click()
# #选择案件跟进状态为已提醒未回复
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select/option[8]").click()
# time.sleep(1) 

#在关键字搜索中输入姓名——汤文钦\冯亚晶
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input").send_keys("汤文钦")
#driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input").send_keys("冯亚晶")
time.sleep(1)
#点击“搜索”按钮
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button").click()
time.sleep(3)
#点击查看按钮
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[10]/span[1]').click()

time.sleep(2)

##########进入我的工作台，点击今日案件
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div/ul/li[2]/span").click()
time.sleep(2)
#点击还款状态
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select").click()
#选择还款状态为已结清
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select/option[3]").click()
#选择电话状态
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/span").click()
#选择电话状态为正常接听
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select/option[7]").click()
time.sleep(1) 
#选择案件跟进状态
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select").click()
#选择案件跟进状态为承诺还款
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select/option[2]").click()
time.sleep(1) 
#在关键字搜索中输入姓名
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[4]/div/input").send_keys("汤文钦")
time.sleep(1)
#点击“搜索”按钮
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[4]/button").click()
time.sleep(2)

##########进入我的工作台，点击明日提醒案件
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div/ul/li[3]/span").click()
time.sleep(2)
#点击还款状态
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select").click()
#选择还款状态为展期
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/select/option[4]").click()
#选择电话状态
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/span").click()
#选择电话状态为设置拉黑
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select/option[9]").click()
time.sleep(1) 
#选择案件跟进状态
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select").click()
#选择案件跟进状态为拒绝还款
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select/option[4]").click()
time.sleep(1) 
#在关键字搜索中输入姓名
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[4]/div/input").send_keys("张三")
time.sleep(1)
#点击“搜索”按钮
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[4]/button").click()
time.sleep(3)

##########进入我的工作台，点击逾期案件
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div/div/ul/li[4]/span").click()
time.sleep(2)
#点击应还款日期
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input").click()
time.sleep(3)
#选择还款状态
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select").click()
#选择还款状态为“逾期”
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select/option[2]").click()
time.sleep(1)
#选择电话状态
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select").click()
#选择电话状态为来电提醒
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select/option[6]").click()
time.sleep(1) 
#选择案件跟进状态
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select").click()
#选择案件跟进状态为已提醒未回复
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select/option[8]").click()
time.sleep(1) 
#在关键字搜索中输入姓名
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input").send_keys("张银萍")
time.sleep(1)
#点击“搜索”按钮
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button").click()
time.sleep(3)


# ##########点击案件管理
# driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/ul/li[2]").click()
# time.sleep(2)
# ##########点击所有案件
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span").click()
# time.sleep(2)
# #选择放款日期
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input").click()
# time.sleep(2)
# # #选择应回款日期
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/input").click()
# # time.sleep(2)
# #选择还款状态
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select").click()
# #在还款状态中选择“逾期”
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select/option[2]").click()
# time.sleep(1)
# #选择负责人
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select").click()
# #选择负责人为超享贷主管
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select/option[3]").click()
# time.sleep(1)
# #在关键字搜索中输入姓名
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input").send_keys("汤文钦")
# time.sleep(2)
# #点击搜索按钮
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button").click()
# time.sleep(3)
# 
# ###########点击案件管理中的案件分配
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/span").click()
# time.sleep(2)
# # #选择应还款日期
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/input").click()
# # time.sleep(5)
# #选择上次负责人
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select").click()
# time.sleep(2)
# #选择上次负责人为聚信达贷后主管
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/select/option[2]").click()
# time.sleep(2)
# #点击“搜素”按钮
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/button").click()
# time.sleep(2)
# # #选择搜素出的案件
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/table/tr[2]/td[1]/img[1]").click()
# # time.sleep(2)
# # #点击派单按钮
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/h1/div/button").click()
# # #进入派单界面，选择负责人
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select").click()
# # #选择负责人为超享贷贷后主管
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/select/option[3]").click()
# # #点击派单界面的“确定”按钮
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/button").click()
# # time.sleep(3)
# 
# ###########点击案件管理中的催回总览
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/ul/li[3]/span").click()
# time.sleep(2)
# 
# ##########点击案件管理中的委外案件
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/ul/li[4]/span").click()
# time.sleep(2)
# #选择放款日期
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input").click()
# time.sleep(2)
# # #选择应回款日期
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/input").click()
# # time.sleep(2)
# #选择还款状态
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select").click()
# #在还款状态中选择“逾期”
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/select/option[2]").click()
# time.sleep(1)
# #选择负责人
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select").click()
# #选择负责人为超享贷委外
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div[4]/select/option[2]").click()
# time.sleep(1)
# #在关键字搜索中输入姓名
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/input").send_keys("汤文钦")
# time.sleep(1)
# #点击搜索按钮
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button").click()
# time.sleep(3)
# 
# 
# ##########点击用户管理界面
# driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/ul/li[3]").click()
# time.sleep(2)
# #点击新建用户
# driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/button").click()
# time.sleep(2)
# # #####新建贷后专员
# # #选择所属产品——聚信达产品
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/select").click()
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[1]/div/select/option[2]").click()
# # time.sleep(1)
# # #输入账号
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/input").send_keys("juxindajuxinda")
# # #输入姓名
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/input").send_keys("聚信达贷后专员")
# # #输入手机号
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/input").send_keys("13313331333")
# # #输入密码
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div/div/input").send_keys("111111")
# # #确认密码
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[6]/div/div/input").send_keys("111111")
# # #选择岗位
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/select").click()
# # #选择岗位为贷后专员
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[7]/div/select/option[2]").click()
# # #选择直属领导
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/select").click()
# # #选择直属领导为聚信达贷后主管
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/select/option[2]").click()
# # #点击创建按钮
# # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[9]/div/button[1]").click()
# # # #点击返回按钮
# # # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[9]/div/button[2]").click()
# # time.sleep(5)
