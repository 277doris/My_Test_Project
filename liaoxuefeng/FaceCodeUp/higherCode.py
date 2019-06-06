#coding:utf-8
#数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，
# 允许我们写出非常强大的功能。
'''
#1、使用__slots__
class Student(object):
    pass
s = Student()   #动态给实例绑定一个属性
s.name = 'Michael'
print(s.name)
#还可以尝试给实例绑定一个方法：
def set_age(self, age):     #定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)  #给实例绑定一个方法
s.set_age(25)   #调用实例方法
print(s.age)    #测试结果
s2 = Student()      #创建新的实例
#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = set_score
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)
#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，
这在静态语言中很难实现。
'''
#使用__slots__
#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
'''
class Student(object):
    __slots__ = ('name', 'age')     #用tuple定义允许绑定的属性名称
s = Student()       #创建新的实例
s.name = 'Michael'      #绑定属性'name'
s.age = 25              #绑定属性'age'
# s.score = 99            #绑定属性'score'      #AttributeError: 'Student' object has no attribute 'score'
# print(s.score)
print(s.name, s.age)
#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 9999
print(g.score)
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''
#使用@property
'''
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
'''
# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between o~100!')
#         self._score = value
#
#     #现在，对任意的Student实例进行操作，就不能随心所欲的设置score了：
# s = Student()
# s.set_score(60)
# s.set_score(999)
# print(s.get_score())

#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# class Student(object):
#
#     @property
#     #等价于get_score(self)函数
#     def score(self):
#         return self._score
#
#     @score.setter
#     #等价于set_score(self, value)函数
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# #@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，
# #@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
# s = Student()
# s.score = 60    #实例转化为s.set_score(60)
# print(s.score)  #实例转化为s.get_score()
# s.score = 999
# print(s.score)

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2019 - self._birth
#
# s = Student()
# s.birth = 27
# print(s.age)
#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
'''
小结：@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，
这样，程序运行时就减少了出错的可能性。
'''
#作业：
# class Screen(object):
#
#     @property
#     def width(self):    #get_value
#         return self._width
#
#     @width.setter
#     def width(self, value):     #set_value
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self._width * self._height
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution = ', s.resolution)
# if s.resolution == 786432:
#     print('测试通过！')
# else:
#     print('测试失败！')

'''
多重继承，继承是面向对象编程的一个重要的方式，因为通过继承，子类可以扩展父类的功能
通过多重继承，一个子类就可以同时获得多个父类的所有功能。
MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，
而不是设计多层次的复杂的继承关系。
'''
# class Dog(Mammal, RunnableMinIn, CarnivorousMixIn):
#     pass
#比如编写一个多进程模式的TCP服务，定义如下：
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass
#编写一个多线程模式的UDP服务，定义如下：
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass
#如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass
#这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
#小结：由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
#只允许单一继承的语言（如Java）不能使用MixIn的设计。

'''
定制类：看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在python中是有特殊用途的
'''
# __str__
#我们先定义一个student类，打印一个实例：
# class Student(object):
#     def __init__(self, name):
#         self.name = name
# print(Student('Marry'))
#打印出一堆<__main__.Student object at 0x109afb190>，不好看。
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
# print(Student('Michael'))
#Student object (name: Michael)
#这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
#解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
# class Student(object):
#     def __init__(self):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name=%s)' % self.name
#     __repr__ = __str__()

#__iter__
#如果一个类想被用于for...in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
#然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1   #初始化两个计数器a,b
#
#     def __iter__(self):
#         return self     #实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b    #计算下一个值
#         if self.a > 100000: #退出循环的条件
#             raise StopIteration()
#         return self.a   #返回下一个值
# for n in Fib():
#     print(n)
#
# #__getitem__
# #Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如取第5个元素
# Fib()[5]

# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
# f = Fib()
# print(f[0])
# print(f[3])
# print(f[100])
# #但是list有个神奇的切片的方法：
# L5 = list(range(100))[5:10]
# print(L5)
#对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int):  #n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):    #n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
# f = Fib()
# print(f[0:5])
# print(f[:10])
# #但是没有对step参数作处理：
# print(f[:10:2])
'''
也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
'''

# #__getattr__:Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
# class Student(object):
#
#     def __init__(self):
#         self.name = 'Michael'
#
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 99
#
# #当调用不存在的属性时，比如score，python解释器会调用__getattr__(self, attr)来尝试获取属性，来返回score的值
# s = Student()
# print(s.name)
# print(s.score)

#返回函数也是完全可以的：
# class Student(object):
#
#     def __getattr__(self, attr):
#         if attr == 'age':
#             return lambda: 25
#
# #只是调用方式要变为：
# s = Student()
# print(s.age())
#注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
#此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，
#我们就要按照约定，抛出AttributeError的错误：

# class Student(object):
#
#     def __getattr__(self, attr):
#         if attr == 'age':
#             return lambda: 25
#         raise ArithmeticError('\'Student\' object has no attribute \'%\'' % attr)
#这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
'''
举个例子：
现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
http://api.server/user/friends
http://api.server/user/timeline/list
如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
利用完全动态的__getattr__，我们可以写出一个链式调用：
'''

# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
# C = Chain().status.user.timeline.list
# print(C)
#这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
#还有些REST API会把参数放到URL中，比如GitHub的API：
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：

#__call__
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
# class Student(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
# s = Student('Michael')
# s()     #self的参数不用传入
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

#小结：Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。

'''
使用枚举类：当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
'''
# JAN = 1
# FEB = 2
# MAR = 3
# OCT = 10
# DEC = 11
# 好处是简单，缺点是类型是int，并且仍然是变量。
#更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
# from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# #这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
#value属性则是自动赋给成员的int常量，默认从1开始计数。
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
# from enum import Enum, unique
#
# @unique
# class Weekday(Enum):
#     Sun = 0  # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# #@unique装饰器可以帮助我们检查保证没有重复值。
# #访问这些枚举类型可以有若干种方法：
# day1 = Weekday.Mon
# print(day1)
# print(Weekday.Tue)
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(day1 == Weekday.Mon)
# print(day1 == Weekday.Tue)
# for name, member in Weekday.__members__.items():
#     print(name, '=>', member)
# #可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

# from enum import Enum, unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过！')
# else:
#     print('测试失败！')

'''
#使用元类type()
动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
比方说我们要定义一个Hello的class，就写一个hello.py模块：
'''

# from hello import Hello
# h = Hello()
# h.hello()
#当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象，测试如下
# from hello import Hello
# h = Hello()
# h.hello()
# print(type(Hello))
# print(type(h))
#type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello
#type()函数既可以返回一个对象的类型，又可以创建新的类型,
#比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

# def fn(self, name='world'):     #先定义函数
#     print('Hello, %s.' % name)
# Hello = type('Hello', (object,), dict(hello=fn))    #创建Hello class
# h = Hello()
# h.hello()
# print(type(Hello))
# print(type(h))

'''
要创建一个class对象，type()函数依次传入3个参数：
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''

#连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
#有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass
'''
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
__new__()方法接收到的参数依次是：
当前准备创建的类的对象；
类的名字；
类继承的父类集合；
类的方法集合。
测试一下MyList是否可以调用add()方法：
'''
# L = MyList()
# L.add(1)
# L.add(2)
# print(L)
# #而普通的list没有add()方法：
# L2 = list()
# L2.add(1)
#动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。
#但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。ORM全称“Object Relational Mapping”，
#即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
#编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，
#想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：
# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()
# class Field(object):
#
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)
#
# class StringField(Field):
#
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')
#
# class IntegerField(Field):
#
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')
#
# class ModelMetaclass(type):
#
#     def __new__(cls, name, bases, attrs):
#         if name=='Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings # 保存属性和列的映射关系
#         attrs['__table__'] = name # 假设表名和类名一致
#         return type.__new__(cls, name, bases, attrs)
# class Model(dict, metaclass=ModelMetaclass):
#
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))
#
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# u.save()