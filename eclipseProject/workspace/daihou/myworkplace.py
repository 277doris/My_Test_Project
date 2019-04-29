#coding:utf-8
from selenium import webdriver
import time
#用断点调试脚本
import pdb
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from log_module import Loginfo, Xlloginfo
#导入获取用户信息的模板
from userdata import get_webinfo, get_userinfo, XlUserinfo

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
def findElement(d, arg):
    '''
    arg must dict
    1:uesrid（用户名）
    2:pwdid （密码）
    3:checkcode（图形验证码）
    4:loginbtn(登录按钮)
    return useEle, pwdEle, codeEle, loginEle
    '''
    userEle = d.find_element_by_xpath(arg['userid'])
    pwdEle = d.find_element_by_xpath(arg['pwdid'])
    codeEle = d.find_element_by_xpath(arg['checkcode'])
    loginEle = d.find_element_by_xpath(arg['loginbtn'])
    return userEle, pwdEle, codeEle, loginEle

#封装元素值，并用循环语句在元组中执行
def sendVals(ele_tuple, args):
    '''
    1、eletuple
    2、account:uname, upwd, ucode, loginbtn
    '''
    listkey = ['uname', 'upwd', 'ucode']
    i = 0
    for key in listkey:
        ele_tuple[i].send_keys('')
        ele_tuple[i].clear()
        time.sleep(1)
        ele_tuple[i].send_keys(args[key])
        time.sleep(1)
        i += 1
    ele_tuple[3].click()
    time.sleep(3)

#封装测试结果，并将测试结果写在log日志中
def checkResult(d, passid, arg, log):
    result = False
    time.sleep(2) 
    try:
        #通过对登录成功页面元素进行定位，判断登录状态
        d.find_element_by_xpath(passid)
        print('Account And Pwd Right!')
        #输出uname,upwd,ucode,pass,换行
        msg = '%s %s %s : pass \n'%(arg['uname'], arg['upwd'], arg['ucode'])
        log.log_write(arg['uname'], arg['upwd'], arg['ucode'], 'pass')
        result = True  
    except:
        print('Account And Pwd Error!')
#         msg = '%s %s %s : error \n'%(arg['uname'], arg['upwd'], arg['ucode'])
        log.log_write(arg['uname'], arg['upwd'], arg['ucode'], 'error')
    return result

#封装退出登录函数
def logout(d, ele_dict):
    #点击退出按钮
    d.find_element_by_xpath(ele_dict['logoutbtn']).click()
    time.sleep(1)          

#封装登录函数，并在元素及用户信息中取值
def login_test(ele_dict, user_list):
    d = openBrower()
#     log = Loginfo()
    log = Xlloginfo()
    log.log_init('sheet1', 'uname', 'upwd', 'ucode', 'result')
    d.maximize_window()
    openUrl(d, ele_dict['url'])
    #以元组形式，从字典中单独取值，定位元素
    ele_tuple = findElement(d, ele_dict)
    #调用发送值的函数，把登录信息，发送给对应定位元素，并检查
    for arg in user_list:
        sendVals(ele_tuple, arg)  
        result = checkResult(d, ele_dict['passid'], arg, log) 
        if result:
            #注销logout
            logout(d, ele_dict)
            #重新login
            ele_tuple = findElement(d, ele_dict)
            
    #关闭日志         
    log.log_close()
    
    #关闭浏览器
    d.quit()

if __name__ == '__main__':
    #读取页面元素信息及用户信息
    ele_dict = get_webinfo(r'C:\eclipse\workspace\TestH5\webinfo.txt')
#     user_list =  get_userinfo(r'C:\eclipse\workspace\TestH5\userinfo.txt')
    xinfo = XlUserinfo(r'C:\Users\22648\Desktop\userinfo.xlsx')
    #用user_list代替原文件中的info
    user_list = xinfo.get_sheetinfo_by_index(0)
    login_test(ele_dict, user_list)
    
    
    
    
    
    