# python的内建模块itertools提供了非常有用的操作迭代对象的函数
# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来。

# cycle()会把传入的一个序列无限重复下去：
# import itertools
# cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
# for c in cs:
#     print(c)
# 无限循环字符串‘ABC'中的字符

# repeat()负责把一个元素无线重复下去，不过如果提供第二个参数就可以限定重复次数：
# import itertools
# ns = itertools.repeat('A', 3)   # 第一个参数代表重复的参数，第二个代表总共重复的次数
# for n in ns:
#     print(n)

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，
# 事实上也不可能在内存中创建无限多个元素。
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
# import itertools
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# list(ns)
# itertools提供的几个迭代器操作函数更加有用：

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
# import itertools
# for c in itertools.chain('ABC', 'XYZ'): #chain()把后面的对象串联起来进行迭代
#     print(c)

# # groupby()，把迭代器中相邻的重复元素挑出来放在一起：
# import itertools
# for key, group in itertools.groupby('AAABBBCCAA'):
#     print(key, list(group))
# # 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
# # 而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
# for key, group in itertools.groupby('AaaaBbbCccA', lambda c: c.upper()):    # Lambda表达式可以定义一个匿名函数。
#     print(key, list(group))
# # groupby()把迭代器中相邻的重复元素挑出来放在一起,"相邻"

# 练习：计算圆周率的公式
import itertools

def pi(N):
    # ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    a = itertools.count(1, 2)   # 第一个参数代表开始值， 第二个参数代表步长
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    aa = itertools.takewhile(lambda x: x <= 2*N -1, a)  # 通过值判断，取a序列中的前N项
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    aaa = list(map(lambda x: 4 / x if x % 4 == 1 else -4 / x, aa))
    # step 4: 求和:
    s = sum(aaa)
    return s

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
