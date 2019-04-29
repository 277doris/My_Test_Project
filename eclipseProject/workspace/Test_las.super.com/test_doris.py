#-*-  coding:utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains 

driver = webdriver.Chrome()
driver.implicitly_wait(10)  
driver.get("http://las.super.com/view/login.html")
driver.maximize_window()
element = driver.find_element_by_xpath
 
#输入用户名
username = element("/html/body/div[2]/div/form/label[1]/div/input") 
username.send_keys("doris")
#输入密码
password = element("/html/body/div[2]/div/form/label[2]/div/input")
password.send_keys("222222")
#输入验证码
check_code = element("/html/body/div[2]/div/form/label[3]/div/input")
check_code.send_keys("spxt")
#点击登录按钮
login = element("/html/body/div[2]/div/form/button")
login.click()
time.sleep(2)       

#产品审批
#点击产品审批模块
prod_appro = element("/html/body/div[1]/div[1]/div/ul/li[4]/a")
prod_appro.click()
time.sleep(1) 
#点击待审模块
wait_appro = element("/html/body/div[2]/div[1]/div/ul/li[1]/a")
wait_appro.click()
time.sleep(1) 
#筛选产品
product_name = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select")
#选择产品为聚信达产品
Select(product_name).select_by_visible_text("聚信达产品")
#筛选处理状态
deal_statu = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/select")
#筛选处理状态为审核中
Select(deal_statu).select_by_visible_text("审核中")
#点击来源
source = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/select")
#来源选择为其他
Select(source).select_by_visible_text("其他")
#在关键字中输入姓名
key_word = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[5]/td[2]/input")
key_word.send_keys("汤文钦")
#点击查询按钮
query = element("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[6]/td[2]/div[1]")
query.click()
time.sleep(3)
#点击接单/处理按钮
accept = element("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[10]")
accept.click()
time.sleep(1)
current_handle1 = driver.current_window_handle
print(current_handle1)
#如果是点击接单按钮，则需启动64-74行的代码
# # 获取alert对话框
# dig_alert = driver.switch_to.alert
# time.sleep(1)
# # 打印警告对话框内容
# print(dig_alert.text)
# # alert对话框属于警告对话框，我们这里只能接受弹窗
# dig_alert.accept()
# time.sleep(3)
#点击用户上传信息
user_sc_info = element("/html/body/div[2]/div[2]/div/div/operate-dir/div/ul/li[1]")
user_sc_info.click()
time.sleep(2)
#模拟鼠标操作——申请表开始
approval_table = element('//*[@id="report-template"]/div[2]/div[1]/div/table[1]/th')
#鼠标拖动至关闭按钮
close_button = element('//*[@id="report-template"]/div[2]/div[1]/div/div')
ActionChains(driver).drag_and_drop(approval_table, close_button).perform()
time.sleep(2)
#鼠标上滑，从关闭按钮开始
close_button = element('//*[@id="report-template"]/div[2]/div[1]/div/div')
#上滑至用户上传信息
user_sc_info = element("/html/body/div[2]/div[2]/div/div/operate-dir/div/ul/li[1]")
ActionChains(driver).drag_and_drop(close_button, user_sc_info).perform()
time.sleep(2)

#点击系统审核信息
sys_info = element('//*[@id="report-template"]/ul/li[2]')
sys_info.click()
time.sleep(2)
# #如果审批信息多：从系统审核信息——滑动至关闭按钮
# sys_info = element('//*[@id="report-template"]/ul/li[2]')
# close_button = element('//*[@id="report-template"]/div[2]/div[2]/div/div[4]/a')
# ActionChains(driver).drag_and_drop(sys_info, close_button).perform()
# time.sleep(2)
# #鼠标上滑，从关闭按钮开始
# close_button = element('//*[@id="report-template"]/div[2]/div[2]/div/div[4]/a')
# #上滑至系统审核信息
# sys_info = element('//*[@id="report-template"]/ul/li[2]')
# ActionChains(driver).drag_and_drop(close_button, sys_info).perform()
# time.sleep(2)

#点击证明材料
certifi_info = element("/html/body/div[2]/div[2]/div/div/operate-dir/div/ul/li[3]")
certifi_info.click()
time.sleep(2)
#查看附件信息
card_info = element('//*[@id="report-template"]/div[2]/div[3]/div/a')
card_info.click()
time.sleep(2)
#从附件信息拖动至关闭按钮
card_info = element('//*[@id="report-template"]/div[2]/div[3]/div/a')
#关闭按钮
close_button = element('//*[@id="report-template"]/div[2]/div[3]/div/div/a')
ActionChains(driver).drag_and_drop(card_info, close_button).perform()
time.sleep(2)
#从关闭按钮上滑至证明资料
close_button = element('//*[@id="report-template"]/div[2]/div[3]/div/div/a')
certifi_info = element("/html/body/div[2]/div[2]/div/div/operate-dir/div/ul/li[3]")
ActionChains(driver).drag_and_drop(close_button, certifi_info).perform()
time.sleep(1)

#点击运营商数据
phone_data = element('//*[@id="report-template"]/ul/li[5]')
phone_data.click()
time.sleep(2)
#点击月份选择
mouth_select = element('//*[@id="types"]')
Select(mouth_select).select_by_visible_text("2018-10")
time.sleep(2)
# #如果本月有通话记录：从呼入呼出top10滑动至电话列表
# top_num = element('//*[@id="report-template"]/div[2]/span/div/div/div[2]/h2')
# phone_list = element('//*[@id="report-template"]/div[2]/span/div/div/div[3]/div[2]/div[1]/table/tbody/tr[7]/td[1]')
# ActionChains(driver).drag_and_drop(top_num, phone_list).perform()
# time.sleep(1)
#从呼入呼出top10滑动至通话详单
top_num = element('//*[@id="report-template"]/div[2]/span/div/div/div[2]/h2')
tel_detail = element('//*[@id="report-template"]/div[2]/span/div/div/div[5]/div[2]/div[1]/span')
ActionChains(driver).drag_and_drop(top_num, tel_detail).perform()
time.sleep(1)
#点击月份选择
mouth_select = element('//*[@id="type"]')
Select(mouth_select).select_by_visible_text("2018-10")
time.sleep(2)
#点击通讯录按钮
phone_address = element('//*[@id="cellBook"]/h2')
phone_address.click()
time.sleep(2)
#从通讯录滑动至呼入呼出top10
phone_address = element('//*[@id="cellBook"]/h2')
top_num = element('//*[@id="report-template"]/div[2]/span/div/div/div[2]/h2')
ActionChains(driver).drag_and_drop(phone_address, top_num).perform()
time.sleep(1)
  
#点击审核处理
deal_with = element('//*[@id="report-template"]/ul/li[4]')
deal_with.click()
time.sleep(2)
#从审核处理滑动至提交按钮
deal_with = element('//*[@id="report-template"]/ul/li[4]')
submit_button = element('//*[@id="report-template"]/div[2]/div[4]/div/div[4]/a[1]')
ActionChains(driver).drag_and_drop(deal_with, submit_button).perform()
time.sleep(3)
# #点击通过按钮
# pass_button = element('//*[@id="passThrough"]')
#点击拒绝按钮
refuse_button = element('//*[@id="unPassThrough"]')
refuse_button.click()
time.sleep(1)
# #点击加入黑名单
# add_black = element('//*[@id="joinBlack"]')
# add_black.click()
# time.sleep(1)
# #点击“是”
# yes_button = element('//*[@id="report-template"]/div[3]/div/form/div[2]/a[1]')
# yes_button.click()
# time.sleep(1)
# #点击否
# no_button = element('//*[@id="report-template"]/div[3]/div/form/div[2]/a[2]')
# no_button.click()
# time.sleep(1)
#拒绝原因选择
refuse_reason = element('//*[@id="checkInfo"]/div[5]/ul/li/select')
Select(refuse_reason).select_by_visible_text("D9----本人放弃类")
time.sleep(1)
#填写备注信息
remark_info = element('//*[@id="textAreaBlank"]')
remark_info.send_keys("自动测试本人放弃")
#点击提交按钮
sumbit_button = element('//*[@id="report-template"]/div[2]/div[4]/div/div[4]/a[1]')
sumbit_button.click()
time.sleep(1)
#对alert弹框进行处理
# 获取alert对话框
dig_alert = driver.switch_to.alert
time.sleep(1)
# 打印警告对话框内容
print(dig_alert.text)
# alert对话框属于警告对话框，我们这里只能接受弹窗
dig_alert.accept()
time.sleep(2)
#切换至审批页面
driver.back()
time.sleep(2)

#点击进件查询
case_query = element('//*[@id="slideBar"]/ul/li[2]/a')
case_query.click()
time.sleep(1)
#选择产品
select_pro = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select[1]')
Select(select_pro).select_by_visible_text("超享贷")
#选择进件方式
case_meth = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select[2]')
Select(case_meth).select_by_visible_text("H5")
#选择处理状态
deal_status = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/select')
Select(deal_status).select_by_visible_text("审核中")
#选择来源
source = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/select')
Select(source).select_by_visible_text("其他")
#搜索关键词
kw = element('//*[@id="search"]')
kw.send_keys("汤文钦")
#点击查询按钮
query_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[6]/td[2]/div[1]')
query_button.click()
time.sleep(2)
print("搜索案件成功！")
#点击案件的查看按钮
view_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[12]')
view_button.click()
time.sleep(2)
#点击用户上传信息
user_info = element('//*[@id="report-template"]/ul/li[1]')
user_info.click()
time.sleep(2)
#点击系统审核信息
sys_info = element('//*[@id="report-template"]/ul/li[2]')
sys_info.click()
time.sleep(2)
#点击证明材料
comfirm_info = element('//*[@id="report-template"]/ul/li[3]')
comfirm_info.click()
time.sleep(2)
#点击审核处理
case_deal = element('//*[@id="report-template"]/ul/li[4]')
case_deal.click()
time.sleep(2)
#点击运营数据
tel_data = element('//*[@id="report-template"]/ul/li[5]')
tel_data.click()
time.sleep(2)
#从运营数据滑动至关闭按钮
tel_data = element('//*[@id="report-template"]/ul/li[5]')
close_button = element('//*[@id="report-template"]/div[2]/span/div/div/div[6]/a')
ActionChains(driver).drag_and_drop(tel_data, close_button).perform()
time.sleep(1)
#点击关闭按钮
close_button = element('//*[@id="report-template"]/div[2]/span/div/div/div[6]/a')
close_button.click()
time.sleep(2)
print("查看案件成功")

#点击审核结果
case_result = element('//*[@id="slideBar"]/ul/li[3]/a')
case_result.click()
time.sleep(1)
#选择产品
product = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/select')
Select(product).select_by_visible_text("聚信达产品")
time.sleep(2)
#选择审核结果
case_result = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/select')
Select(case_result).select_by_visible_text("审核通过")
time.sleep(1)
#选择来源
source = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[5]/td[2]/select')
Select(source).select_by_visible_text("助力钱包")
time.sleep(1)
#关键字搜索
kw = element('//*[@id="search"]')
kw.send_keys("李骢")
time.sleep(1)
#点击查询按钮
query_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[7]/td[2]/div[1]')
query_button.click()
time.sleep(2)
print("搜素案件成功")
#点击查看按钮
view_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[10]')
view_button.click()
time.sleep(1)
#从详细信息滑动至返回按钮
detail_info = element('//*[@id="detailInfo2"]/div')
back_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/a')
ActionChains(driver).drag_and_drop(detail_info, back_button).perform()
time.sleep(1)
#点击返回按钮
back_button = element('//*[@id="main"]/div[2]/div/div/div[2]/div[2]/a')
back_button.click()
print("查看成功")
#点击全量导出按钮
all_export = element('//*[@id="tableHD"]/button')
all_export.click()
time.sleep(3)
print("全量导出成功")

#点击配置中心
config_center = element('//*[@id="menu"]/div/ul/li[3]/a')
config_center.click()
time.sleep(1)
#点击产品配置
product_config = element('//*[@id="slideBar"]/ul/li[1]/a')
product_config.click()
time.sleep(2)
#点击机构配置
organization_config = element('//*[@id="slideBar"]/ul/li[2]/a')
organization_config.click()
time.sleep(2)
#点击流程配置
process_config = element('//*[@id="slideBar"]/ul/li[3]/a')
process_config.click()
time.sleep(2)
#点击数据配置
data_config = element('//*[@id="slideBar"]/ul/li[4]/a')
data_config.click()
time.sleep(2)

#用户管理
user_control = element('//*[@id="menu"]/div/ul/li[2]/a')
user_control.click()
time.sleep(1)
#点击用户管理
user_cont = element('//*[@id="slideBar"]/ul/li[1]/a')
user_cont.click()
time.sleep(2)
current_window = driver.current_window_handle
print(current_window)
#新建用户
add_user = element('//*[@id="main"]/div[2]/div/div[1]/div[1]/div[2]/a')
add_user.click()
time.sleep(2)
#选择角色
role_select = element('//*[@id="roleid"]/div[2]')
role_select.click()
role_sp = element('//*[@id="roleid"]/div[1]/label[1]/input')
role_sp.click()
#输入账号
account = element('//*[@id="username1"]')
account.send_keys("testSp")
#输入姓名
name = element('//*[@id="realName"]')
name.send_keys("自动一条添加")
#输入邮箱
mail = element('//*[@id="userMail"]')
mail.send_keys('tangwenqin@juxinda360.com')
#点击保存按钮
save_button = element('//*[@id="save"]')
save_button.click()
time.sleep(2)
#获取alert对话框
dig_alert = driver.switch_to.alert
time.sleep(1)
# 打印警告对话框内容
print(dig_alert.text)
# alert对话框属于警告对话框，我们这里只能接受弹窗
dig_alert.accept()
time.sleep(2)
#切换至原来页面
driver.switch_to_window(current_window)
time.sleep(2)
driver.refresh()
time.sleep(1)
print("新建账号成功")

#点击角色管理
user_cont = element('//*[@id="slideBar"]/ul/li[2]/a')
user_cont.click()
time.sleep(3)
#点击新建角色按钮
add_role = element('//*[@id="main"]/div[2]/div/div/div/div[1]/div[2]/a')
add_role.click()
time.sleep(2)
#角色ID
role_id = element('//*[@id="roleId"]')
role_id.send_keys("TSPAA")
#角色昵称
role_name = element('//*[@id="roleName"]')
role_name.send_keys("自动添加审批的")
#点击保存按钮
save_button = element('//*[@id="btnSave"]')
save_button.click()
time.sleep(3)
print("新建角色成功")

#点击黑名单管理
black_us = element('//*[@id="menu"]/div/ul/li[1]/a')
black_us.click()
time.sleep(1)
#点击黑名单管理
black_uss = element('//*[@id="slideBar"]/ul/li/a')
black_uss.click()
time.sleep(1)
current_window = driver.current_window_handle
#点击新建名单
add_user = element('//*[@id="main"]/div[2]/div/div[1]/div[1]/div[2]/a')
add_user.click()
time.sleep(1)
#输入姓名
user_name = element('//*[@id="realName"]')
user_name.send_keys("这是测试黑名单")
#输入电话
tel = element('//*[@id="userTel"]')
tel.send_keys("13993339278")
#输入备注信息
other_info = element('//*[@id="remark"]')
other_info.send_keys("自动添加备注信息；自动添加备注信息；自动添加备注信息；自动添加备注信息；")
#点击保存按钮
save_button = element('//*[@id="save"]')
save_button.click()
time.sleep(1)
#点击dialog中的按钮确定
yes = element('//*[@id="main"]/div[2]/div/div/div[4]/div/form/div[2]/a[1]')
yes.click()
time.sleep(1)
#获取alert对话框
dig_alert = driver.switch_to.alert
time.sleep(1)
# 打印警告对话框内容
print(dig_alert.text)
# alert对话框属于警告对话框，我们这里只能接受弹窗
dig_alert.accept()
time.sleep(2)
print("新建黑名单成功！")
driver.switch_to_window(current_window)
time.sleep(1)
driver.refresh()
time.sleep(2)

#点击待移入按钮
wait_add = element('//*[@id="buttonLists"]/button[3]')
wait_add.click()
time.sleep(1)
#点击第一个案件的备注信息
other_info = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[5]/span')
other_info.click()
time.sleep(2)
#点击备注信息中的关闭按钮
close_button = element('//*[@id="main"]/div[2]/div/div[1]/div[4]/div/form/div[1]/div')
close_button.click()
#点击第一个案件的编辑按钮
edit_button = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/a[1]')
edit_button.click()
#修改姓名
edit_name = element('//*[@id="realName"]')
edit_name.clear()
time.sleep(1)
edit_name.send_keys("自动更改姓名")
#修改电话
edit_tel = element('//*[@id="userTel"]')
edit_tel.clear()
time.sleep(1)
edit_tel.send_keys("13666666666")
#修改备注信息
edit_other_info = element('//*[@id="remark"]')
edit_other_info.clear()
time.sleep(1)
edit_other_info.send_keys("自动测试修改信息！自动测试修改信息！自动测试修改信息！")
#点击保存按钮
save_button = element('//*[@id="save"]')
save_button.click()
#点击dialog中的按钮确定
yes = element('//*[@id="main"]/div[2]/div/div/div[4]/div/form/div[2]/a[1]')
yes.click()
time.sleep(1)
#获取alert对话框
dig_alert = driver.switch_to.alert
time.sleep(1)
# 打印警告对话框内容
print(dig_alert.text)
# alert对话框属于警告对话框，我们这里只能接受弹窗
dig_alert.accept()
time.sleep(2)
print("修改黑名单成功！")
#返回黑名单管理页
driver.switch_to_window(current_window)
time.sleep(1)
#点击第一案件的移入按钮
delete_button = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[4]/a[2]')
delete_button.click()
time.sleep(1)
#获取alert对话框
dig_alert = driver.switch_to.alert
time.sleep(1)
# 打印警告对话框内容
print(dig_alert.text)
# alert对话框属于警告对话框，我们这里只能接受弹窗
dig_alert.accept()
time.sleep(3)
print('移入黑名单成功！')
#在关键字中搜索姓名
kw = element('//*[@id="search"]')
kw.send_keys('假测')
#点击搜索按钮
query_button = element('//*[@id="main"]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]')
query_button.click()
time.sleep(2)
print("搜索成功")

#关闭浏览器
driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()