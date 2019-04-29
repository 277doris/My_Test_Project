#  -*-  coding:utf-8 -*-
#用selenium打开谷歌浏览器
from selenium import webdriver
#导入鼠标事件包
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
element = driver.find_element_by_xpath
#数据平台
driver.implicitly_wait(10)  
driver.get("http://fea.super.com/#/")
driver.maximize_window()


####数据平台登录模块
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


#########名单导入页面
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
print("导入模块下载成功")
#点击导入模块的X
import_close = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[1]/button")
import_close.click()
#点击导出按钮
export_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]")
export_button.click()
time.sleep(2)
print("导出单个案件模块成功")

##########案件查询页面
case_query = element("/html/body/div/div/div[1]/ul/li[2]")
case_query.click()
#点击基础案件查询
basic_case = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span")
basic_case.click()
#点击关键字搜索，输入姓名
keyword_query1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/input")
keyword_query1.send_keys("候云飞")
#点击搜索按钮
search_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/button")
search_button1.click()
time.sleep(2)
#点击查看按钮
view_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[4]/span")
view_button.click()
time.sleep(2)

#####点击高级案件查询
advance_case = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]")
advance_case.click()
#点击关键字搜索，输入姓名
keyword_query2 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/input")
keyword_query2.send_keys("张三")
#点击搜索按钮
search_button2 = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/button")
search_button2.click()
time.sleep(2)
print("查询案件成功")

##########贷超报表
#点击贷超报表
statement_daichao = element("/html/body/div/div/div[1]/ul/li[3]")
statement_daichao.click()
#点击CPA机构报表
CPA_statement = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span")
CPA_statement.click()
time.sleep(2)
#点击平台名称——哈哈
platform_name1 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[1]')
platform_name1.click()
time.sleep(5)
#滑动页面：从实时日期滑动至历史日期
now_date = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/table/tr[1]/th[1]') 
his_date = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/table/tr[2]/td[1]')
ActionChains(driver).drag_and_drop(now_date, his_date).perform()
time.sleep(2)
#点击CPC机构报表
CPC_statement = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/span")
CPC_statement.click()
time.sleep(2)
#点击平台名称
platform_name2 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[1]')
platform_name2.click()
time.sleep(3)

#点击CPS机构报表
CPS_statement = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[3]")
CPS_statement.click()
time.sleep(2)
#点击平台名称——阿里巴巴
platform_name3 = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[4]')
platform_name3.click()
time.sleep(3)

#####点击贷超管理
manage_daichao = element("/html/body/div/div/div[1]/ul/li[4]")
manage_daichao.click()
time.sleep(2)
#点击CPA机构按钮
click_CPA = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span")
click_CPA.click()
time.sleep(2)
#点击冻结按钮
freeze_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[5]/span[1]")
freeze_button.click()
time.sleep(2)
#点击解除冻结按钮
unfreeze_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[5]/span")
unfreeze_button.click()
time.sleep(2)
#点击编辑按钮
edit_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[5]/span[2]")
edit_button.click()
time.sleep(2)
#点击增减平台按钮
manage_platform = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button")
manage_platform.click()
time.sleep(2)
#选择添加第一个平台
add_platform1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[1]/div/ul/li[1]")
add_platform1.click()
add_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div/div[2]/button[1]")
add_button.click()
#点击保存按钮，获取alter弹框
save_button = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button")
save_button.click()
# 直接实例化Alert对象
a1 = Alert(driver)  
time.sleep(1)
#接受弹框信息并关闭
a1.accept()
time.sleep(1)
#点击平台中冻结按钮
freeze_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]/span[1]")
freeze_button1.click()
time.sleep(2)
#点击平台中解除冻结按钮
unfreeze_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]/span")
unfreeze_button1.click()
time.sleep(2)
#点击编辑按钮
edit_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[6]/span[2]")
edit_button1.click()
time.sleep(2)
#设置编辑页面的系数
edit_num = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[4]/input")
edit_num.send_keys("1")
#设置编辑页面的价格
edit_price = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/p[5]/input")
edit_price.send_keys("2")
#点击保存按钮
save_button1 = element("/html/body/div/div/div[2]/div[2]/div/div/div[4]/div/div/div[3]/button[1]")
save_button1.click()
# 直接实例化Alert对象
a2 = Alert(driver)  
time.sleep(1)
#接受弹框信息并关闭
a2.accept()
time.sleep(1)

#点击CPC机构
CPC_statement1 = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/span")
CPC_statement1.click()
time.sleep(3)
#点击CPS机构
CPS_statement1 = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[3]/span")
CPS_statement1.click()
time.sleep(2)


####点击APP管理
manage_APP = element("/html/body/div/div/div[1]/ul/li[5]")
manage_APP.click()
#点击产品上架管理
putaway = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]/span")
putaway.click()
time.sleep(2)
#点击确定下架按钮
down_conf = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[8]/button[1]')
down_conf.click()
time.sleep(2)
#点击确定下架按钮
element('/html/body/div[2]/div/div[3]/button[2]').click()
time.sleep(2)
print('产品下架成功')
#点击上架按钮
putaway_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/table/tr[2]/td[8]/button[1]")
putaway_button.click()
time.sleep(1)
#点击确定上架按钮
element('/html/body/div[2]/div/div[3]/button[2]').click()
time.sleep(2)
print('产品上架成功')
#选择状态
status = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/select')
#选择状态为已上架
Select(status).select_by_visible_text("已上架")
time.sleep(1)
#在产品名称中输入“测试的”
product_name = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/input")
product_name.send_keys("测试的")
#点击搜索按钮
search_button3 = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[2]/button")
search_button3.click()
time.sleep(3)
print("产品搜索成功")

#点击产品数据监控
element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]").click()
time.sleep(2)
#选择产品名称
sele_product = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/select')
#选择产品名称为哈哈哈
Select(sele_product).select_by_visible_text("哈哈哈")
time.sleep(1)
#点击查询按钮
qurey_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/button')
qurey_button.click()
time.sleep(1)
#鼠标从查询按钮滑动至日期
qurey_button = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/button')
date_his = element('//*[@id="app"]/div/div[2]/div[2]/div/div/div[4]/table/tr[2]/td[1]')
ActionChains(driver).drag_and_drop(qurey_button, date_his).perform()
time.sleep(2)

#点击产品排名
product_sequence = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[3]/span")
product_sequence.click()
#点击调整按钮
change_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div")
change_button.click()
#调整第一第二排名
num_2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/label[2]/span[1]/span")
num_2.click()
#点击上移按钮
up_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/div[1]")
up_button.click()
#点击保存按钮
save_button2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[3]/button")
save_button2.click()
# 直接实例化Alert对象
a3 = Alert(driver)  
time.sleep(1)
#接受弹框信息并关闭
a3.accept()
time.sleep(3)


#########点击用户管理
user_manage = element("/html/body/div/div/div[1]/ul/li[6]")
user_manage.click()
time.sleep(2)
#点击贷超用户
daichao_user = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[1]")
daichao_user.click()
#点击解除冻结按钮
unfreeze_button2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[1]")
unfreeze_button2.click()
time.sleep(2)
#点击编辑按钮
edit_button2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[2]/span")
edit_button2.click()
#重置密码
reset_pw = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input")
reset_pw.send_keys("a111111")
#确认密码
conf_pw2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div[1]/input")
conf_pw2.send_keys("a111111")
#点击修改按钮
modifier_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/button[1]")
modifier_button.click()
# 直接实例化Alert对象
a3 = Alert(driver)  
time.sleep(1)
#接受弹框信息并关闭
a3.accept()
time.sleep(3)
#点击创建用户按钮
new_user = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button")
new_user.click()
time.sleep(2)
#选择落地页
choose_page = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div/input")
time.sleep(1)
choose_page.click()
time.sleep(1)
#选择超享借
choose_chaoxiangjie = element("/html/body/div[3]/div[1]/div[1]/ul/li[1]")
choose_chaoxiangjie.click()
time.sleep(2)
#输入账号名称
account = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input")
account.send_keys("chaoxiangjie")
#输入平台名称
platform_name4 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input")
platform_name4.send_keys("随你花")
#输入初始额度
init_amount = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input")
init_amount.send_keys("10")
#输入联系电话
tel = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input")
tel.send_keys("13313331333")
#输入初始密码
init_pw = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input")
init_pw.send_keys("111111")
#输入确认密码
conf_pw = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input")
conf_pw.send_keys("111111")
#点击创建按钮
creat_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/button[1]")
creat_button.click()
# #点击返回按钮
# element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/button[2]").click()
time.sleep(2)

#点击平台用户
platform_user = element("/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]")
platform_user.click()
time.sleep(2)
#d点击充值按钮
recharge_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[1]/span[1]")
recharge_button.click()
#输入充值金额
recharge_amount = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/p[4]/input")
recharge_amount.send_keys("100")
#点击充值按钮
recharge_button1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[3]/button[1]")
time.sleep(2)
recharge_button1.click()
time.sleep(2)
#点击分配按钮
distribution_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[2]/td[7]/span[1]/span[2]")
distribution_button.click()
#分配基本案件——10
basic_case_num = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/p[7]/input[2]")
basic_case_num.clear()
basic_case_num.send_keys("2")
#分配高级案件——20
advance_case_num = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/p[8]/input[2]")
advance_case_num.clear()
advance_case_num.send_keys("2")
#点击分配按钮
distribution_button1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[3]/button[1]")
time.sleep(2)
distribution_button1.click()
time.sleep(2)
#点击第二个平台的冻结按钮
freeze_button2 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[3]/td[7]/span[2]")
freeze_button2.click()
time.sleep(2)
#点击解除冻结按钮
unfreeze_button3 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tr[3]/td[7]/span")
unfreeze_button3.click()
time.sleep(2)
#点击创建用户按钮
creat_user = element("/html/body/div/div/div[2]/div[2]/div/div/div[1]/div/div/button")
creat_user.click()
time.sleep(2)
#选择角色
role = element("/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div[1]/input")
role.click()
time.sleep(2)
#选择角色为贷超统计管理员角色
role_manage = element("/html/body/div[3]/div[1]/div[1]/ul/li[4]")
role_manage.click()
time.sleep(2)
#输入账号名称
uesr_name = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input")
uesr_name.send_keys("dctj")
#输入合作方名称
partner_name = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/div/input")
partner_name.send_keys("百度")
#输入白名单
white_name = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/div/input")
white_name.send_keys("111.202.41.75")
#输入手机号
tel1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/div/input")
tel1.send_keys("13313331333")
#输入初始密码
init_pw1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[6]/div/div/input")
init_pw1.send_keys("111111")
#输入确认密码
conf_pw1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[7]/div/div/input")
conf_pw1.send_keys("111111")
#输入充值金额
recharge = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[8]/div/div/input")
recharge.send_keys("100")
#输入基础数据
basic_data = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/div/input")
basic_data.send_keys("100")
#输入高级数据
advance_data = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[10]/div/div/input")
advance_data.send_keys("10")
#点击创建按钮
creat_button1 = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[11]/div/button[1]")
creat_button1.click()
# #点击返回按钮
back_button = element("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/div[11]/div/button[2]")
back_button.click()
time.sleep(2)

#点击退出按钮
exit_button = element("/html/body/div/div/div[1]/div")
exit_button.click()
driver.quit()
