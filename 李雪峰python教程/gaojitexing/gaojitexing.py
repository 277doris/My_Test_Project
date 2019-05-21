#coding:utf-8
#切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
# print(L[0:3])
# #L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# #如果第一个索引是0，还可以省略
# print(L[:3])
# #倒数切片,切倒数第一第二个元素
# print(L[-2:])
# L = list(range(100))
# print(L)
# print(L[:10])
# #甚至什么都不写，只写[:]就可以原样复制一个list：
# print(L[:])
#字符串也可以用切片操作，只是操作结果仍是字符串
# print('ABCDEF'[:3])

#迭代
#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
# from collections import Iterable
# isinstance('abc', Iterable)  # str可迭代
# isinstance([1,2,3], Iterable)  # list可迭代
# isinstance(123, Iterable)  # 整数不可迭代
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
# #同时引用两个变量
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)

# def findMinAndMax(L):
#     if len(L) == 0:
#         return (None, None)
#     else:
#         for i, x in enumerate(L):
#             if i == 0:
#                 min = max = x
#             else:
#                 if x > max:
#                     max = x
#                 if x < min:
#                     min = x
#     return (min, max)
# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

#列表生成式
# list = list(range(1,11))
# print(list)
# L = []
# for x in range(1, 11):
#     L.append(x * x)
# print(L)
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，
# 十分有用，多写几次，很快就可以熟悉这种语法。
list_creat = [x * x for x in range(1, 11)]
print(list_creat)
#判断奇数偶数的






