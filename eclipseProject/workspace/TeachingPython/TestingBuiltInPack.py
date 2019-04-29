# -*- coding:utf-8 -*-
'''
Created on 2018-9-27
@author: 22648
'''
import requests
url = "http://h5.super.com/"
#发送get请求
response = requests.get(url)
#显示指定字符编码
response.encoding = "utf-8"
#html源码
print(response.text)




