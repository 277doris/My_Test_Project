# -*- coding: UTF-8 -*
#在 Python 中，可以将出错归为两类：错误（Errors）和异常（Exceptions）
#从软件方面来说，一般将错误分为两种：语法错误、逻辑错误
import code
from _ast import Try

#语法错误
#少一个冒号：
# while True
# print("hello world")

#逻辑错误
#比较两个数，返回较大值，漏掉了相等的情况
# def compare(num1, num2):
#     if (num1 > num2):
#         return num1
#     elif (num1 < num2):
#         return num2
# print('result:', compare(12, 12))

#异常
# 异常是在程序运行中产生的，大多数的异常都不会被程序处理，并以错误信息的形式抛出，Python 中常见的异常有：
# 异常名称                                           说明
# ZeroDivisionError    除数为0
# AttributeError    试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
# IOError    输入/输出异常；常见原因是无法打开文件
# ImportError    无法引入模块或包；常见原因是路径问题或名称错误
# IndentationError    语法错误（的子类）；常见原因是代码没有正确对齐
# IndexError    下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError    试图访问字典里不存在的键
# KeyboardInterrupt    Ctrl+C被按下
# NameError    使用一个还未被赋予对象的变量
# TypeError    传入对象类型与要求的不符合
# UnboundLocalError    试图访问一个还未被设置的局部变量，常见原因是由于另有一个同名的全局变量，导致你以为正在访问它
# ValueError    传入一个调用者不期望的值，即使值的类型是正确的

# num_list = [12,34,56,78,90]
# print(num_list[14])

#异常的处理
# def compare(num1, num2):
#     try:
#         if (num1 >= num2):
#             return num1
#         else:
#             return num2
#     except:
#             return 'error'
# #正确的调用
# print ('compare(12,34):', compare(12, 34))
# #异常的调用
# print ("compare(12,'ab'):", compare(12, 'ab'))
# print("compare('12', 34):", compare('12', 34)) 

#try-except 这种异常处理机制可以让程序在不牺牲可读性的前提下增强健壮性和容错性，try-except 语句的一般形式如下。
#指定捕获某种异常，并对其进行处理（except子句负责处理）
# try:
#     <statement-1>
#     .
#     <statement-N>
# except ErrorType:
#     <statement-x>
#     .
#     <statement-y>
# 
# #同时捕获多种指定异常，多个异常需要用括号括起来
# try:
#     <statement-1>
#     .
#     <statement-N>
# except (ErrorType1,ErrorType2,…,ErrorTypeN):
#     <statement-x>
#     .
#     <statement-y>
# #不指定异常，默认捕获所有异常，如果对于一段代码，你不清楚会出现什么异常，或者出现多种异常而不需要分别处理，可以采用这种方式，捕获所有异常。
# try:
#     <statement-1>
#     .
#     <statement-N>
# except:
#     <statement-x>
#     .
#     <statement-y>

# try-except处理异常的流程为：
# 首先，try 和 except 之间的语句会被执行；
# 如果没有异常发生，except 后面的语句会被忽略；
# 如果有异常发生，try 后面的其它语句就会被跳过，如果异常的类型与 except 关键词后面的异常匹配，这个 except 后面的语句就会被执行；
# 如果没有异常发生，else 子句存在的话，else 子句将被执行；
# finally 子语会在 try 子句执行完毕之后执行，不管 try 子句是否出现异常。如果一个异常发生在 try 子句中却未被处理（捕获），或者发生在 except 或者 else 子句中时，finally 子句执行完后会再次抛出该异常。
# 补充说明：
# try 与 else，finally 结合使用的内容将在后面进一步详细说明；
# 一次性捕获多个异常时，多个异常需要用括号括起来；
# 最后一个 except 子句可以不带异常类型，这样就会捕获所有异常；
# 当一个异常发生时，可能它还有一些异常参数，except 语句异常名称后面可以跟一个参数，这个参数会与异常实例绑定，存储在 instance.args 中，如果异常中 __str__() 定义过了，就可以直接打印出参数。

# #Try与else语句结合使用
# #Try 语句可以结合 else 一起使用，如果 try 子句没有异常发生，else 子句存在的话，else 子句将被执行。
# def compare(num1, num2):
#     try:
#         if (num1 >= num2):
#             result = num1
#         else:
#             result = num2
#     except:
#         return "ERROR"
#     else:
#         print("OK")
#         return result
# #正确的调用
# print ("compare(12,34):", compare(12, 34))
# #异常的调用
# print ("compare(12, 'ab'):", compare(12, 'ab'))
# print("compare('12', 34):", compare('12', 34))

#不管 try 子句是否出现异常，finally 子语都会执行。适用场景：不管 try 是否出现异常，都需要做某种处理
#比如，打开一个文件并读取内容，不管这个过程是否出现异常，都需要关闭文件，关闭文件的动作就可以放在 finally 中。

# import sys
# #在该Python源文件同目录下新建一个文件myfile.txt，写入内容“user-name: Jack”作为测试
# try:
#     #打开文件，读取第一行
#     f = open('myfile.txt')
#     s = f.readline()
#     print("result",s)
# except:
#     print("ERROR") 
# finally:
#     print("close file")
#     f.close()
    
# import sys
# 
# try:
#     #打开一个不存在的文件
#     f = open('file.txt')
#     s = f.readline()
#     print("result",s)
# except TypeError:
#     print("ERROR") 
# finally:
#     print("close file")


#Exception 万能异常：不仅捕获了异常，而且记录下了异常的详细信息，对于定位问题十分有用。
# import sys
# 
# try:
#     #打开一个不存在的文件,将抛出异常
#     f = open('file.txt')
#     s = f.readline()
#     print("result",s)
# except FileNotFoundError as err:
#     print("Exception info:",err) 
# finally:
#     print("close file")

#主动抛出异常
# import sys
# 
# try:
#     #输入一个文件名
#     fileName = input("please input the name:")
#     splitList = fileName.split('.')
#     fileType = splitList[splitList.__len__()-1]
#     #判断文件格式，如果不是doc则抛出异常
#     if (fileType != "doc"):
#         raise NameError("the file type:%s is not excepted."%(fileType))
#     f = open(fileName)
#     s = f.readline()
#     print("result",s)
# except FileNotFoundError as err:
#     print("Exception info:",err)
# finally:
#     print("close file")

#自定义一个基础异常类
class MyException(Exception):
    def __init__(self, *args):
        self.args = args
#定义不同种类的业务异常，继承基础异常类
class loginError(MyException):
    def __init__(self, code = 100, message = 'login error',
                args = ('Internal Server Error','http:500')):
        self.args = args
        self.message = message
        self.code = code
class loginoutError(MyException):
    def __init__(self):
        self.args = ('Internal Server Error',)
        self.message = 'login out error'
        self.code = 200
        
#raise loginError(),使用默认参数
try:
    raise loginError()
except loginError as e:
    print(e)  #输出异常
    print(e.code)  #输出错误代码
    print(e.message)  #输出错误信息
#raise loginError(),传入参数
try:
    raise loginError(400, 'password is wrong!',('Internal Server Error',))
except loginError as e:
    print(e)   #异常输出
    print(e.code)  #输出错误代码
    print(e.message)  #输出错误信息
    



































