# -*- coding: UTF-8 -*
#定义函数
# def compare(Parameter1,Parameter2):
#     if (Parameter1 > Parameter2):
#         print(1)
#     elif (Parameter1 == Parameter2):
#         print(0)
#     else :
#         print(-1)
# #调用函数
# compare(123, 12)
# compare(123, 345)
# compare(3.14, 23)
# compare(123, 123)
        
#在 Python 中，所有类型：函数、模块、数字、字符串、列表、元组、字典等等都是对象，而变量是没有类型的
# a = 12
# print("a=", a)
# a = "ABCDE"
# print("a=", a)
# a = [1,2,3,4,5]
# print("a=", a)
# a = (1,2,3,4)
# print("a=", a)
# a = {'key':12,'key1':13}
# print("a=", a)

#不可变类型:这种只能通过创建新的对象才能改变对变量的赋值的数据类型，称为不可变类型，如整数、字符串、元组都是不可变类型。
# def change(x):
#     x = 10
# a = 5
# change(a)
# print("a=", a)

#可变类型:列表、字典、集合、队列等
# def change(x):
#     x.append(2012)
# a = [1, 2, 3, 4]
# change(a)
# print("a=", a)

#函数的参数类型
#必须参数
#声明参数为一个
# def update(arg):
#     arg = arg + 1
# #正确
# update(12)
# #不正确，参数缺失
# update()
# #不正确，参数多余
# update(1, 2)

# #参数顺序要一致
# def printInfo (name, sex, age):
#     print("name:", name)
#     print("sex:", sex)
#     print("age:", age)
# #正确
# printInfo("Jack", "female", 18)
# #错误，参数顺序不对应
# printInfo(18, "female", "Jack")

#关键字参数
# def printInfo(name, sex, age):
#     print("name:", name)
#     print("sex:", sex)
#     print("age:", age)
# #都是正确的
# printInfo(name="Jack", sex="female", age=18)
# printInfo(sex="female", name="Doris" ,age=20)
# printInfo(sex="female", age=34, name="Jack")

#默认参数
#声明参数为一个
# def printInfo(name, sex, age=0):
#     print("name:", name)
#     print("sex:", sex)
#     print("age:", age)
# #正确
# printInfo(name="Jack", sex="female")

#不定长参数,有些场景下，我们希望设计一个参数数量不确定的函数，
#如任意个整数求和，调用形式可以是：sum(a)、sum(a,b,c)、sum(a,b,c,d)……
#这时候我们需要使用一种不定长参数，一般定义形式如下：
# def functionname([formal_args,] *var_args_tuple):
#     functionbody
#定义一个求和函数
# def sum(num, *num_list):
#     sum = num
#     for element in num_list:
#         sum += element
#     print("sum=",sum)
# sum(1)
# sum(1, 2, 3, 4)

#return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
#不带参数值的 return 语句返回 None，表示没有任何值。如果函数没有显式的使用 return 语句，Python 函数也会默认返回 None 对象。
#定义比较函数
# def compare(parameter1, parameter2):
#     if (parameter1 > parameter2):
#         return 1
#     elif (parameter1 == parameter2):
#         return 0
#     else:
#         return -1
# result = compare(123, 456)
# print("result=", result)

#作用域：同名的变量并没有发生冲突，这是因为它们的“作用域”不同，变量只在自己的作用域内有效，a=123 处属于全局变量，function() 函数内部 a=10 属于局部变量，作用域不同，因此并不会冲突。
#这里的a是全局变量
a = 123
def function():
    #这里的a是局部变量
    a = 10
    print("I a=", a)
function()
print("II a=", a)
#作用域的分类：L(Local),局部作用域；E（Enclosing）,闭包函数外的函数中；G（Global）,全局作用域；B（Built-in）,内建作用域；
#优先级顺序：L->E->G->B,即在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

    
    
    
    
    
    
    
    
    

