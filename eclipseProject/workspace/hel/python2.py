# -*- coding: UTF-8 -*
#队列
# 
# from collections import deque
# #基于列表初始化一个队列
# queue = deque(['A','B','C'])
# #队尾添加元素
# queue.append('D')
# print('queue',queue)
# #队头出列
# queue.popleft()
# print('queue',queue)
# #队头出列
# queue.popleft()
# print('queue',queue)
# 
# #条件、循环及其他语句  if-else
# A = 8
# B = 10
# if A >= B:
#     print('The larger number is:',A) 
# else:
#     print('The larger number is:',B)
# 
# #从控制台输入数据默认为字符串类型，需要强制转换为int类型
# A = int(input("Please enter the number A:"))
# B = int(input("Please enter the number B:"))
# if A > B:
#     print('The larger number is:',A) 
# elif A == B:
#     print('A and B are equal to ',A)  
# else:
#     print('The larger number is:',B)  
#     
# #创建一个“学号-成绩”字典
# exam_results = {'2018002':95, '2018013':90, '2018023':87}
# #接受从控制台输入的学号，默认为字符串类型
# stu_num = input("Please enter the student number:")
# #删除输入学号首尾空格，避免影响
# stu_num = stu_num.strip()
# #判断输入的学号是否存在于“学号-成绩”字典中
# if stu_num in exam_results.keys():
#     print("Your score is:",exam_results.get(stu_num))
# else:
#     print("The student number you entered is incorrect!") 
#     
# #for 循环语句
# #for循环的形式    for <item> in <sequence>:   <actions>
# #测试数据集
# num_set = [98,94,82,67,58,90,86]
# sumOfNum = 0
# #遍历列表中的元素，求和
# for element in num_set:
#     sumOfNum += element
# #求平均值并打印结果    
# average = sumOfNum/len(num_set)
# print("The average is:%f"%(average))
#ctrl+/可以批量注释
# 通过 range() 函数遍历数据序列，range() 函数可以生成数列，将生成的数列作为索引，我们可以遍历数字序列。range() 函数的参数是可变的：
# range(n)：生成步长为1的数列：1，2，3……n；
# range(m, n)：生成步长为1的数列：m，m+1，m+2，……，n；
# range(m, n, s)：生成步长为s的数列：m，m+s，m+2s，……，X(<=n)
from test.test_statistics import AverageMixin

# for index in range(4):
#     print("index:",index)
# for index in range(4,10):
#     print("index:",index)
# for index in range(4,9,2):
#     print("index:",index)
# #测试数据集
# city_set = ['BeiJin','TianJin','ShangHai','HangZhou','SuZhou']
# #索引从0开始，以步长2遍历
# for index in range(0,len(city_set),2):
#     print("city_set[%d]:%s"%(index,city_set[index]))

#求一组数据的平均值
#初始化测试数据
# num_set = [98, 94, 82, 67, 58, 90, 86]
# sumOfNUM = 0
# index = 0
# 
# while index < len(num_set):
#     sumOfNUM += num_set[index]
#     index += 1
#     #求平均值并打印结果
#     average = sumOfNUM/len(num_set)
#     print("The average is:%f"%(average))
# #break语句   跳出for和while循环体，也就意味着循环结束。
# num_set = [98,94,82,67,58,90,86]
# for i in range(len(num_set)):
#     if num_set[i] < 60:
#         print("Someone failed!")
#         break
#     else:
#         print(num_set[i])

# while True:
#     a = input('Please enter a number:')
#     if int(a) > 100:
#         print('error!!!')
#         break
#     else:
#         print(a)

#continue语句 ，与 break 不同，continue 不会退出循环体，而是跳过当前循环块的剩余语句，继续下一轮循环。
#初始化测试数据
# num_set = [98,94,82,67,58,90,86]
# for i in range(len(num_set)):
#     if num_set[i] < 60:
#         print("Someone failed!")
#         continue
#     print(num_set[i])
#pass  pass 是空语句，一般用做占位，不执行任何实际的操作，只是为了保持程序结构的完整性
#初始化测试数据
# num_set = [98,82,67,58,90]
# for i in range(len(num_set)):
#     if num_set[i] < 60:
#         print("Someone failed!")
#         pass
#     print(num_set[i])
#初始化测试数据
num_set = [98,94,82,67,58,90,86]
for i in range(len(num_set)):
    if num_set[i] < 60:
        print("Someone failed!")
    else:
        pass
    


   
    