#coding:utf-8
'''
函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，
通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，
这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。
'''
#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

'''
高阶函数：函数本身也可以赋值给变量，即：变量可以指向函数。
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
'''
# def add(x, y, f):
#     return f(x) + f(y)
# #给函数的变量赋值
# x = -5
# y = 6
# f = abs
# #调用函数
# print(add(x, y, f))

#Python内建了map()和reduce()函数。
'''
我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
# def f(x):
#     return x * x
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# list(r)
'''
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
'''
#map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
# r = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(r)
#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#例如序列求和：
# from functools import reduce
# def add(x, y):
#     return x + y
# add_res = reduce(add, [1, 3, 5, 7, 9])
# print(add_res)
# from functools import reduce
# def fn(x, y):
#     return x * 10 + y
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# print(reduce(fn, map(char2num, '13579' )))
#用lambda函数进一步简化成：
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def char2num(s):
#     return DIGITS[s]
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！


'''
filter:Python内建的filter()函数用于过滤序列
'''
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
# def is_odd(n):
#     return n % 2 == 1
# odd_num = list(filter(is_odd, [1, 2, 3,  5, 7]))
# print(odd_num)
#把一个序列中的空字符串删掉，可以这么写：
# def not_empty(s):
#     return s and s.strip()
# not_emptyNum = list(filter(not_empty, ['A', 'B', None, 'C', ' ']))
# print(not_emptyNum)
#可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# #用filter求素数
# #1、可以先构造一个从3开始的奇数序列
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# #2、然后定义一个筛选函数：
# def _not_divisible(n):
#     return lambda x: x % n > 0
# #3、最后，定义一个生成器，不断返回下一个素数：
# def primes():
#     yield 2
#     it = _odd_iter()  #初始序列
#     while True:
#         n = next(it)  #返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it)  #构建新序列
# #这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# #由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# #打印20以内的素数：
# #由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# for n in primes():
#     if n < 20:
#         print(n)
#     else:
#         break
#注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁
# def is_palinderome(n):
#     return str(n) == str(n)[::-1] #s[::1]实现字符串翻转
# print(list(filter(is_palinderome,range(1, 200))))
# if list(filter(is_palinderome,range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

#sorted排序算法
'''
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
'''
#默认按正序排序
# sorted_num = sorted([1, 4, 21, -21, 0])
# # print(sorted_num)
# # #sorted()函数也是一个高阶函数，还可以接收一个key函数来实现自定义的排序
# # sorted_abs = sorted([1, 8, 21, 0, -11, 7, 22], key=abs)     #按绝对值大小排序
# # print(sorted_abs)
#忽略大小写的排序：
# lower_sort = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# print(lower_sort)
#进行反向排序，不必改动key函数，可以传入第三个参数reverse=True:
# lower_sortTrue = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# print(lower_sortTrue)
#1、创建一个列表
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#2、定义一个姓名的函数，取L列表的第一个元组（tuple）
def by_name(L):
    return L[0]
#3、定义一个分数的函数，取L列表的第二个元组（tuple)，按分数倒序排
def by_score(L):
    return -L[1]
#4、按分数排序
L2 = sorted(L, key=by_score)
print(L2)
#5、按姓名排序
L3= sorted(L, key=by_name)
print(L3)
#6、检查排序是否正确
if L2 == [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]:
    print('测试通过!')
else:
    print('测试失败!')
if L3 == [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]:
    print('测试通过!')
else:
    print('测试失败!')

