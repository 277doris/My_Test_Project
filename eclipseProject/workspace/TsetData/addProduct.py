#coding:utf-8
from selenium import webdriver
import time
#用断点调试脚本
import pdb
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

#封装等待时间
def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)

#封装浏览器并返回一个句柄
def openBrower():
    '''return Webdriver Handle'''
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle 

#封装url地址
def openUrl(handle, url):
    '''open url'''
    handle.get(url)
    
#封装查找元素的方式，以参数形式传入
def loginElement(d, arg):
    '''
    arg must dict
    1:uesrid（用户名）
    2:pwdid （密码）
    3:loginbtn(登录按钮)
    return useEle, pwdEle, codeEle, loginEle
    '''
    userEle = d.find_element_by_xpath(arg['userid'])
    pwdEle = d.find_element_by_xpath(arg['pwdid'])
    loginEle = d.find_element_by_xpath(arg['loginbtn'])
    return userEle, pwdEle, loginEle

def appManageElement(d, arg):
    '''
    arg must dict
    1:appmana（app管理）
    2:upApp （产品上架管理）
    3:addPro(添加产品)
    return appmanaEle, upAppEle, addProEle
    '''
    appmanaEle = d.find_element_by_xpath(arg['appmana'])
    upAppEle = d.find_element_by_xpath(arg['upApp'])
    addProEle = d.find_element_by_xpath(arg['addPro'])
    return appmanaEle, upAppEle, addProEle

#封装元素值，并用循环语句在元组中执行
def sendVals(ele_tuple, args):
    '''
    1、eletuple
    2、account:uname, upwd, loginbtn
    '''
    listkey = ['uname', 'upwd']
    i = 0
    for key in listkey:
        ele_tuple[i].send_keys('')
        ele_tuple[i].clear()
        time.sleep(1)
        ele_tuple[i].send_keys(args[key])
        time.sleep(1)
        i += 1
    ele_tuple[2].click()
#     #打断点调试
#     pdb.set_trace()

#封装元素值，并用循环语句在元组中执行
def click(ele2_tuple, args):
#     '''
#     1、ele2_tuple
#     2、appmana, upApp, addPro
#     '''
    listkey2 = ['appmana', 'upApp', 'addPro']
    i = 0
    for key in listkey2:
        i += 1
    ele2_tuple[i].click()
    
def login_test(ele1_dict, user_list):
    d = openBrower()
    d.maximize_window()
    openUrl(d, ele1_dict['url'])
    #以元组形式，从字典中单独取值，定位元素
    ele1_tuple = loginElement(d, ele1_dict)
    #调用发送值的函数，把登录信息，发送给对应定位元素，并检查
    for args in user_list:
        sendVals(ele1_tuple, args)  
    
def addProd_test(ele2_dict, login_test):
    d = openBrower()
    #以元组形式，从字典中单独取值，定位元素
    ele2_tuple = appManageElement(d, ele2_dict)
    for args in user_list:
        sendVals(ele2_tuple, args)
    
    d.quit()

if __name__ == '__main__':
    #测试数据
    url = 'http://fea.super.com/#/'
    account = 'master'
    pwd = 111111
    #以字典形式定义元素的xpath值
    ele1_dict = {'url': url,
                'userid':'//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/div/input',
                'pwdid':'//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/div/input', 
                'loginbtn':'//*[@id="app"]/div/div[2]/div/div/div/form/div[3]/div/button'}
    ele2_dict = {'appmana':'//*[@id="app"]/div/div[1]/ul/li[5]',
                  'upApp':'//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[1]',
                  'addPro':'//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/button'}
    user_list = [{'uname':account, 'upwd':pwd}]
    login_test(ele1_dict, user_list)
    addProd_test(ele2_dict)
    