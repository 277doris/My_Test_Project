#coding:utf-8
# 阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f)
# print(f())
# '''
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# '''
# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# if f1 == f2:
#     print('测试通过')
# else:
#     print('测试失败')
# print(f1)
# print(f2)

#闭包：注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
#另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# print(f1(), f2(), f3())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
# def count():
#     def f(j):
#         def g():
#             return j * j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))     #f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())
#缺点是代码比较长，可利用lambda函数缩短代码

#练习，利用闭包返回一个计算器函数，每次调用它返回递增整数：
# def creatCounter():
#     a = 0
#     def counter():
#         nonlocal a
#         a += 1
#         return a
#     return counter
# counterA = creatCounter()
# print(counterA(), counterA(), counterA(), counterA())
# counterB = creatCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

#匿名函数
#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
#例如：
# map_num = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9] ))
# print(map_num)
# #通过对比可以看出，匿名函数lambda x: x * x实际就是：
# def f(x):
#     return x * x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# f = lambda x: x * x
# print(f(5))
#上下两式子实现的结果一样，lambda是匿名函数，不用定义及返回可直接调用
# def f(x):
#     return x * x
# print(f(5))
#也可以把匿名函数作为返回值返回，比如：
# def build(x, y):
#     return lambda: x * x + y * y

#练习：
# def is_odd(n):
#     return n % 2 == 1
# #用函数调用方式，求1-19之间的奇数，filter方法嵌入函数及参数
# L1 = list(filter(is_odd, range(1, 20)))
# print(L1)
# #使用lambda匿名函数求1-19之间的奇数
# L2 = list(filter(lambda n: n%2==1, range(1, 20)))
# print(L2)
# if L1 == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]:
#     print('L1 测试通过！用函数调用方式通过！')
#     if L1 == L2:
#         print('L1 and L2测试通过！用函数及匿名函数均测试通过')
# else:
#     print('L1 != L2 and测试失败！')

#装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也能调用该函数
# def now():
#     print('2019-5-23')
# #将函数now赋值给变量f
# f = now
# #通过变量f调用now函数
# f()

# #函数对象有一个__name__属性，可以拿到函数的名字：
# now.__name__
# print(now.__name__)     #将函数的名字打印出来
# f.__name__
# print(f.__name__)
#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# #观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
# @log
# def now():
#     print('2019-5-23')
# now()
#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
#把@log放到now()函数的定义处，相当于执行了语句 now = log(now)
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# @log('execute')
# def now():
#     print('2019-05-23')
# now()
# #和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)
# #我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
# now.__name__
# print(now.__name__)     #函数的__name__属性已经从原来的'now'变成了'wrapper'
#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#或者针对带参数的decorator
import functools
# def log(text):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('%s %s():' % (text, func.__name__))
#         return wrapper
#     return decorator
#import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。


'''
偏函数：Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：
int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
'''
# int_num = int('12345')
# print(int_num)
# #但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
# int_num = int('12345', base=8)
# print(int_num)
# int_num = int('12345', base=16)
# print(int_num)
#假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
# def int2(x, base=2):
#     return int(x, base)
# print(int2('1000000'))
# print(int2('1010101'))
#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
#使用functools.partial的内置函数，传入数据类型及二进制转换条件
# int2 = functools.partial(int, base=2)
# #调用函数，在参数位置填写需要转换的数据
# print(int2('1000000'))
# print(int2('1010101'))
# #所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# print(int2('1000000',base=16))      #默认值是2，调用时可以传入其他的值，如base=16
#最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
int2 = functools.partial(int, base=2)
print(int2('1000000'))
#相当于：
kw = {'base': 2}
int('1000000', **kw)
print(int('1000000', **kw))
#当传入：
max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7)
print(max2(5, 6, 7))
#相当于：
args = (10, 5, 6, 7)
max(*args)
print(max(*args))
'''
小结：当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''
