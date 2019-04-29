# -*- coding: UTF-8 -*
#定义一个简单的类，描述一个人的基本信息
# class Person:
#     #定义类的数据成员：姓名，年龄
#     name = ''
#     age = 0
#     #定义一个函数:打印类实例的基本信息
#     def printPersonInfo(self):
#         print('person-info:{name:%s, age:%d}' %(self.name, self.age))
#     #定义一个简单的函数
#     def hello(self):
#         print("hello world!")
# #实例化，创建一个对象
# p1 = Person()
# #访问类的属性：数据成员，访问语法obj.X
# print("name:", p1.name)
# print("age:", p1.age)
# #访问类的函数
# p1.printPersonInfo()
# p1.hello()

#定义一个简单的类，描述一个人的基本信息        
# class Person:
#     #定义类的数据成员：姓名，年龄
#     name=''
#     age=0
#     #定义一个函数：打印类实例的基本信息    
#     def printPersonInfo(self):
#         print('name:',self.name)
#         print('self:',self)
#         print('self class:',self.__class__)
# #实例化，创建一个对象
# p1 = Person()
# #访问类的函数
# p1.printPersonInfo()

# #定义一个简单的类，描述一个人的基本信息        
# class Person:
#     #定义类的数据成员：姓名，年龄
#     name=''
#     age=0  
# #定义构造函数，用于创建一个类实例，也就是类的具体对象
# #通过参数传递，可以赋予对象初始状态
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age  
#     #定义一个函数：打印类实例的基本信息    
#     def printPersonInfo(self):
#         print('person-info:{name:%s, age:%d}'%(self.name,self.age))
# 
# 
# #实例化，创建两个对象，默认调用构造函数：__init__()
# p1 = Person("Zhang San",12)
# p2 = Person("Li Si",13)
# #访问类的属性：数据成员,访问语法obj.X
# print("name:",p1.name)
# print("age:",p1.age)
# #调用函数
# p1.printPersonInfo()
# p2.printPersonInfo()

#继承：通常将实施继承行为的类称为子类（Child Class）或者派生类（Derived Class），被继承的类称为父类（Parent Class）或者基类（Base Class)。
#定义一个类occupation，描述职业
# class Occupation:
#     #定义构造函数
#     def __init__(self,salary,industury):
#         self.salary = salary
#         self.industry = industury
#     def printOccupationInfo(self):
#         print('Occupation-info:{salary:%d, industry:%s}' %(self.salary,self.industry))
# #定义一个简单的类person，继承自类Occupation
# class Person(Occupation):
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age 
#         def printPersonInfo(self):
#             print('person-info:{name:%s, age:%d}' %(self.name, self.age))
# #创建一个子类对象
# temp = Person('Wu-Jing', 38)
# #访问父类的数据成员
# temp.salary = 21000
# temp.industry = 'IT'
# #分别调用本身和父类的函数
# temp.printOccupationInfo()
# temp.printPersonInfo()
# 
# #定义一个类BankAccount,描述银行账户
# class BankAccount:
#     def __init__ (self,number,balance):
#         self.number = number
#         self.balance = balance
#     #计算并返回年利息
#     def getAnnualInterest(self):
#         return self.balance*0.042   
# #定义一个类Occupation,描述职业
# class Occupation:
#     def __init__(self,salary,industry):
#         self.salary = salary
#         self.industry = industry
#     def printOccupationInfo(self):
#         print('Occupation-info:{salary:%s, industry:%s}' %(self.salary, self.industry))
# #定义一个类Person，继承自类BankAccount和BankAccount
# class Person(Occupation,BankAccount):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     #定义一个函数：打印类实例的基本信息
#     def printPersonInfo(self):
#         print('person-info:{name:%s, age:%d}'%(self.name, self.age))
# 
# #创建一个子类对象
# temp = Person('Wu-Jing', 38)
# #访问父类数据成员
# temp.number = 622202050201
# temp.balance = 1000000.99
# temp.salary = 21000
# temp.industry = "IT"
# #分别调用本身和父类的函数
# temp.printOccupationInfo()
# temp.printPersonInfo()
# print('Annual interset:', temp.getAnnualInterest())

#定义一个类BankAccount,描述银行账户
#需要注意的是，多继承中，子类继承了不同父类中的属性和函数，这些属性和函数可能存在同名的情况，在子类使用这些同名的函数或属性时，
#在没有指定的情况下，Python 将根据一定顺序进行搜索：首先搜索子类，如果未找到则根据多继承定义的顺序，从左至右在父类中查找。
# class BankAccount:
#     def printInfo(self):
#         print('BankAccount-info')
# #定义一个类Occupation,描述职业
# class Occupation:
#     def printInfo(self):
#         print('Occupation-info')
# #定义一个类Person,继承自类BankAccount和BankAccount
# class Person(Occupation,BankAccount):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def printPersonInfo(self):
#         print('person-info')
# #创建一个子类对象
# temp = Person('Wu-Jing',38)
# temp.printInfo()

#函数的重写：从父类继承来的函数并不能完全满足需求，需要在子类中对其进行修改
#重写：在子类中重写父类中的函数，当子类对象调用该名称的函数时，会调用子类中重写的函数，父类中的同名函数将被覆盖。
#定义一个occupation，描述职业
# class Occupation:
#     #定义构造函数
#     def __init__ (self,salary, industry):
#         self.salary = salary
#         self.industry = industry
#     def printInfo(self):
#         print('{salary:%d, industry:%s}'%(self.salary,self.industry))
# #定义一个简单的类person，继承自类Occupation
# class Person(Occupation):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     #定义一个函数：打印类实例的基本信息
#     def printInfo(self):
#         print('name:%s, age:%d'%(self.name, self.age))
#         print('salary:%d, industry:%s'%(self.salary,self.industry))
# #创建一个子类对象
# temp = Person('Wu-Jing',38)
# #访问父类的数据成员
# temp.salary = 21000
# temp.industry = 'IT'
# #分别调用函数printInfo()
# temp.printInfo()

#私有属性与私有方法
#私有属性：__attribute：属性名前面加两个下划线，即声明该属性为私有，不能在类的外部直接访问，在类内部访问时用 self.__attribute。
#私有函数：__function：函数名前面加两个下划线，即声明该函数为私有，不能在类的外部直接访问，在类内部访问时用 self.__ function

#类中的函数必须有一个额外的参数 self，并且 self 参数必须放在第一个参数的位置。
#定义一个简单的类，描述一个人的基本信息
# class Person:
#     #定义类的数据成员：姓名、年龄
#     name = ''
#     age = 0
#     #定义一个函数：打印类实例的基本信息
#     def printPersonInfo(self):
#         print('name:', self.name)
#         print('self:', self)
#         print('self class:', self.__class__)
# #实例化，创建一个对象
# p1 = Person()
# #访问类的函数
# p1.printPersonInfo()

#实例化
#定义一个简单的类，描述一个人的基本信息
# class Person:
#     #定义类的数据成员：姓名、年龄
#     name = ''
#     age = 0
#     #定义构造函数，用于创建一个类实例，也就是类的具体对象
#     #通过参数传递，可以赋予对象初始状态
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
#     #定义一个函数：打印类实例的基本信息
#     def printPersonInfo(self):
#         print('person-info:{name:%s, age:%d}'%(self.name, self.age))
# #实例化，创建两个对象，默认调用构造函数：__int__()
# p1 = Person('zhangsan', 13)
# p2 = Person('lisi', 27)
# #访问类的属性：数据成员，访问语法obj.X
# print("name:",p1.name)
# print("age:",p1.age)
# #调用函数
# p1.printPersonInfo()
# p2.printPersonInfo()

#定义一个简单的类，描述一个人的基本信息
class Person:
    #定义两个私有属性：name、age
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    #定义公有函数，在类外不可以访问
    def getName(self):
        self.__fun()
        return self.__name
    def getAge(self):
        return self.__age
    #定义一个私有函数，只能在类内部使用
    def __fun(self):
        print('hello')
# #实体化
# p1 = Person('Zhang San', 12)
# #访问类的私有化属性和私有函数，将会报错
# print('name:', p1.__age)
# print('age:', p1.__name)
# p1.__fun()

#实体化
p1 = Person('Zhang San', 12)
#访问类的公有函数
print("name:",p1.getName())
        


        













            
            
            
        
    























