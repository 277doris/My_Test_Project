#coding:utf-8
'''
Created on 2019年3月26日

@author: tangwenqin
'''
#导入Excel读取的包
import xlrd
#打开Excel文件
xl = xlrd.open_workbook(r'C:\Users\22648\Desktop\Python\userinfo.xlsx')
#获取所有表单信息
xl.sheets()
#通过索引获取第一张sheet
sheet = xl.sheets()[0]
#获取有效行数和列数
sheet.nrows
sheet.nclos
#获取第一行数据
sheet.row_values(0)

