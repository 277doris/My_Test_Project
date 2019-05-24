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
# list_creat = [x * x for x in range(1, 11)]
# print(list_creat)
#判断奇数偶数的
# odd_num = [x * x for x in range(1, 11) if x % 2 != 0]
# print (odd_num)
#还可以使用两层循环，可以生成全排列：
# two_list = [m + n for m in 'ABC' for n in 'XYZ']
# print(two_list)
# import os #导入os模块
# dic = [d for d in os.listdir('.')]  #os.listdir可以列出当前文件和目录
# print(dic)
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k, v in d.items():
#     print(k, '=', v)
# #表生成式也可以使用两个变量来生成list：
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# list_arg = [k + '=' + v for k, v in d.items()]
# print(list_arg)
#把一个list中所有的字符串变成小写/大写/首字母大写
# L = ['Hello', 'World', 'IBM', 'Apple']
# lower_list = [s.lower() for s in L]  #小写
# upper_list = [s.upper() for s in L]  #大写
# title_list = [s.title() for s in L]  #首字母大写
# print(lower_list)
# print(upper_list)
# print(title_list)

# L1 = ['Hello', 'World', 18, 'Apple', None]
# #使用内建的isinstance函数可以判断一个变量是不是字符串：
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
#
# # 测试:
# print(L2)
# #判断实际结果和预期结果是否一致，如果一致则打印一条“测试通过”的信息
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

#在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# L = [x * x for x in range(10)]
# print(L)
# g = (x * x for x in range(10))
# print(g)
# print(next(g))
# print(next(g))
'''generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
'''
# g = (x * x for x in range(10))
# for n in g:
#     print(n)
#下面的函数可以输出斐波那契数列的前N个数:
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# print(fib(6))
# #要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# #如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
'''
generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
'''

#迭代器
'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：
'''
#杨辉三角
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [1]+[L[i-1]+L[i] for i in range(1,len(L))]+[1]
# n = 0
# results = []
# for t in triangles():
#     #把每行的数据打印
#     print(t)
#     results.append(t)
#     #控制行数
#     n = n + 1
#     if n == 10:
#         break
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')

#迭代器
'''
可以直接作用于for循环的数据类型有以下几种：
1、集合数据类型：list，tuple,dict,set,str等；
2、一类是generator，包括生成器和自带的yield的generator function
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
可以使用isinstance（）判断一个对象是否是Iterable对象
'''
# from collections import Iterable
# >>> isinstance([], Iterable)
# True
# >>> isinstance({}, Iterable)
# True
# >>> isinstance('abc', Iterable)
# True
# >>> isinstance((x for x in range(10)), Iterable)
# True
# >>> isinstance(100, Iterable)
# False
'''
而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象：
'''
# >>> from collections import Iterator
# # >>> isinstance((x for x in range(10)), Iterator)
# # True
# # >>> isinstance([], Iterator)
# # False
# # >>> isinstance({}, Iterator)
# # False
# # >>> isinstance('abc', Iterator)
# # False
'''
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
'''
#小结：
'''
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass
    
实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
'''





