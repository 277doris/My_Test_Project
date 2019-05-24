# #coding:utf-8
# #一、定义函数
# #1、求绝对值的函数
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-99))
#
# #2、空函数,pass用来做占位符
# def nop():
#     pass
#
# #3、参数检查，如果参数不对，python编辑器会提示TypeError
# my_abs('A')

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# my_abs('A')

# #4、返回多个值
# import math
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y + step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
# r = move(100, 100, 60, math.pi / 6)
# print(r)

#小结：
'''
1、定义函数时，需要确定函数名和参数个数；
2、如果有必要，可以先对参数的数据类型做检查；
3、函数体内部可以用return随时返回函数结果；
4、函数执行完毕也没有return语句时，自动return None。
5、函数可以同时返回多个值，但其实就是一个tuple。
'''

#二、函数的参数
#1、位置参数
# def power(x):
#     return x * x
# print(power(8))
'''
修改后的power(x, n)函数有两个参数：x和n，
这两个参数都是位置参数，调用函数时，
传入的两个值按照位置顺序依次赋给参数x和n'''
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(2,3))

#2、默认参数
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5))
# print(power(5, 3))
'''
使用默认参数时需注意以下几点：
1、必选参数在前，默认参数在后，否则Python的解释器会报错
2、如何设置默认参数
3、当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
'''
#写个一年级小学生注册的函数，需要传入name和gender两个参数：
# def enroll(name, gender):
#     print('name:', name)
#     print('gender:', gender)
# enroll('Sarah', 'F')
#把年龄和城市设为默认参数：
# def enroll(name, gender, age=6, city='BeiJing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
# # enroll('Sarah', 'F')
# #只有与默认参数不符的学生才需要额外提供信息：
# enroll('Bob', 'M', 7)
# enroll('Adam', 'M', city='TianJin')
'''
1、可见，默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，
2、又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。
3、默认参数必须指向不变对象
'''

#可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# nums = [1, 2, 3]
# print(calc(*nums))
#*nums表示把nums这个list的所有元素作为可变参数传进去。

#关键字参数
'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为
一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict。请看示例：
'''
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
# person('Michael', 30)
# person('Bob', 35, city='BeiJing')
# person('Adam', 45, gender='M', job='Engineer')

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
# extra = {'city': 'BeiJing', 'job': 'Engineer'}
# person('Jack', 24, **extra)
'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
'''

#命名关键字参数
'''
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
至于到底传入了哪些，就需要在函数内部通过kw检查。
仍以person()函数为例，我们希望检查是否有city和job参数：
'''
# def person(name, age, **kw):
#     if 'city' in kw:
#         #有city参数
#         pass
#     if 'job' in kw:
#         #有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:',kw)
#但是调用者仍可以传入不受限制的关键字参数：
# person('Jack', 24, city='Beijing', address='Chaoyang', zipcode=123456)
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# def person(name, age, *, city, job):
#     print(name, age, city, job)
# person('Jack', 24, city='Beijing', job='Engineer')
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
# #命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# person('Jack', 24, 'Beijing', 'Engineer')
'''
小结：Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''

#递归函数：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
# def fact(n):
#     return fact_iter(n, 1)
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
# print(fact(5))
'''
小结：使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
'''

#汉诺塔的移动实现递归函数
def move(n, a, b, c):
    if n == 1:
        # 如只有一个盘子，从A柱直接移动它到终点C柱
        print('move', a, '-->', c)
    else:
        # 如果不止一个盘子，先把上面的n-1个盘子移到B柱去
        move(n-1, a, c, b)
        # 然后把最下面的盘子移到终点C
        move(1, a, c, b)
        # 现在，不要去管那个已经移动到C柱的大盘子，相当于A,B两柱交换了位置，C柱还是终点。
        move(n-1, b, a, c)
move(4, 'A', 'B', 'C')
