# -*- coding: UTF-8 -*
from inspect import stack
print("hello world")
a = 12
print("a=", a)
a = "ABCDE"
print("a=", a)
a = 1 + 4j
print("a=", a)


def add(a,b):
    return a+b;
print('10的3次方 = %d' %pow(10,3))
print('1+2 = %d' %add(1,2))

a = 123
b = 3.1415926
print("int(b)=", int(b))
print("float(a)=", float(a))
print("complex(a)=", complex(a))
print("complex(a,b)=", complex(a,b))

import math
#求绝对值：abs(x)
print("abs(-12)=", abs(-12))

#向上取整：ceil（x）
print("ceil(3.1415)=", math.ceil(3.1415))

#向下取整：floor（x）
print("floor(3.678)=", math.floor(3.678))

#四舍五入：round（x）
print("round(3.678)=", round(3.678))

#乘方运算：pow（x,y）,x的y次方
print("pow(3,4)=", pow(3,4))

#求平方根：sqrt（x）
print("sqrt(144)=", math.sqrt(144))

#初始化测试数据
X = 24
Y = 5
Z = 0
#分别进行7种算术运算
Z = X + Y
print("X + Y =", Z)
Z = X - Y
print("X - Y =", Z)
Z = X * Y
print("X * Y =", Z)
Z = X / Y
print("X / Y =", Z)
#取模%---求余数
Z = X % Y
print("X % Y =", Z)
#取整//
Z = X // Y
print("X // Y =", Z)
#乘方**
Z = X ** Y
print("X ** Y =", Z)

#比较运算符
X = 24
Y = 5
print("X == Y:", X == Y)
print("X != Y:", X != Y)
print("X > Y:", X > Y)
print("X < Y:", X < Y)
print("X >= Y:", X > Y)
print("X <= Y:", X < Y)

#赋值运算
#初始化测试数据
X = 2
Y = 3
#分别进行7种赋值运算
Y = X
print("Y = X, Y =", Y)
Y += X
print("Y += X, Y =", Y)
Y -= X
print("Y -= X, Y =", Y)
Y *= X
print("Y *= X, Y =", Y)
Y /= X
print("Y /= X, Y =", Y)
Y **= X
print("Y **= X, Y =", Y)
Y //= X
print("Y //= X, Y =", Y)

#逻辑运算（or或、and与、not非）
X = 2
Y = 3
Z = 5
print("X>Y and X<Z:", X>Y and X<Z)
print("X<Y and Z:", X<Y and Z)
print("X>Y or Z:", X>Y or Z)
print("X<Y or Z:", X<Y or Z)
print("X or X<Z:", X or X<Z)
print("not X :", not X)
print("not X<Y :", not X<Y)

#位运算  &与（有0则0，全1为1）、|或（有1为1）、^异或（相异为1）、~取反（把1变0）、>>右移动、<<左移动

temp1 = "ABCDEFG"
temp2 = [4,2,3,5,8,9]
a = "CDE"
b = 5
c = "CDF"
print("a in temp1?", a in temp1)
print("b in temp2?", b in temp2)
print("c in temp1?", c in temp1)

#身份运算符   is；  is not 计算结果为布尔值
#字符串   str
str1 = "Hello World!"
str2 = "ABCDEFG"
print('str1:',str1)
print('str1[0]:',str1[0])
print('str1[0:4]:',str1[0:5])
print('str1[5:9]:',str1[6:11])

#修改字符串
str1 = "Hi!"
str2 = "Jack"
#通过拼接修改字符串
str1 = str1 + str2
print("After splicing str1:",str1)
#通过替换修改字符串：replace（old，new）
str1 = str1.replace(str2, "Tom")
print("After replacement str1:",str1)

#字符串运算符
str1 = "Hello World!"
str2 = "Jack"
#字符串拼接
print("str1 + str2:",str1+str2)
#字符串截取
print("str1[0:6]:",str1[0:6])
#字符串复制
print("str2*3:",str2*3)
#成员运算：判断一个字符串是否包含某个成员
print("World in str1?","World" in str1)
print("world in str1?","world" in str1)

#字符串格式化
#格式化为十进制:%d
print('PI is approximately equal to %d (I)'%(3.1415926))
#格式化字符串:%s
print('PI is approximately equal to %s (II)'%(3.1415926))
#格式化浮点数字，可指定小数点后的精度,默认为6位小数:%f
print('PI is approximately equal to %f (III)'%(3.1415926))
#格式化浮点数字，指定n位小数:%.nf
print('PI is approximately equal to %.2f (IV)'%(3.1415926))
#用科学计数法格式化浮点数:%e
print('PI is approximately equal to %e (V)'%(3.1415926))
#格式化为十进制:%d
print('The road is about %d meters long (VI)'%(1234))
#格式化无符号八进制数:%d
print('The road is about %o meters long (VII)'%(1234))
#格式化无符号十六进制数:%x
print('The road is about %x meters long (VIII)'%(1234))


#字符串内建函数
str1 = " Hello World! Hello"
str2 = "Hello"
#返回字符串的长度
print("str1的长度:",len(str1))
#对字符串进行分割：split(str),分隔符为str,此处以空格进行分割
print("str1以空格分割的结果：",str1.split(" "))
#删除字符串的首尾空格
print("str1删除首尾空格:",str1.strip())
#count(str2,beg>=0,end<=len(str1))
#返回 str2 在 str1 里面出现的次数,如果 beg 或者 end 指定则返回指定范围内 str2出现的次数
print("str2在str1中出现的次数:",str1.count(str2))
print('str2在str1中出现的次数(指定范围):',str1.count(str2,10,20))

#检查字符串是否以 obj (对象)结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束
#如果是，返回 True,否则返回 False.
print('str1是否以 str2结尾:',str1.endswith(str2))
print('str1是否以 str2结尾(指定范围):',str1.endswith(str2,10,19))
#检测 str2是否包含在字符串str1中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，
#如果包含返回开始的索引值，否则返回-1
print('str1中是否包含str2:',str1.find(str2))
print('str1中是否包含str2(指定范围):',str1.find(str2,10,20))

#列表[]
#创建列表  list
list1 = [3.14, 5.96, 1897, 2020, "China",3+4j];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["BeiJing", "ShangHai", "NanJing", "GuangZhou"]; 
list4 = [] 
#通过索引下标访问列表中的单个元素
print("list1[2]: ",list1[2]) 
print("list2[2]: ",list2[2])
print("list3[2]: ",list3[2])
#通过索引下标一次访问多个元素
print("list1[0:2]:",list1[0:2])

#更改列表中的元素
list1 = [3.14, 5.96, 1897, 2020, "China",3+4j];
print("before list1[3]: ",list1[3]) 
list1[3] = "Change"
print("after list1[3]: ",list1[3])

#删除列表中的元素   del、remove(obj)、clear（）
list1 = [3.14, 5.96, 1897, 2020, "China", 3+4j];
print("Before the operation:", list1)
del list1[3]
list1.remove(3+4j)
print("After deleting the element:", list1)
list1.clear()
print("After the emptying of the list:", list1)

#项列表中添加新元素
#append（obj）:添加新元素将新元素添加到列表的末尾；
#insert（index，object）：超如新元素到指定索引位置。
list1 = [3.13, 5.96, 1897, 2020, "China", 3+4j];
print("Before list1: ",list1)
list1.append("New Ele-I")
list1.insert(2, "New Ele-II")
print("After list1:",list1)


#列表常用内建方法
list1 = [2012, 1949, 1897, 2050, 1945, 1949];
#求列表长度，即列表中元素的个数:len(obj)
print("The length of the list:", len(list1))
#求列表中最大值;max(list)
print("The largest element in the list:",max(list1))
#求列表中最小值：min(list)
print("The smallest element in the list:",min(list1))
#统计某个元素在列表中出现的次数：list.count(obj)
print("The number of times 1949 appears:", list1.count(1949))
#从列表中找出某个值第一个匹配项的索引位置：list.index(obj)
print("The index of the first location of 1949:", list1.index(1949))
#复制一个已有的表：list.copy（）
list2 = list1.copy()
print("list2:",list2)
#反转一个已有的表：list.reverse()
list1.reverse()
print("After reversing :", list1)

#列表的拼接、嵌套、乘法、迭代
list1 = [1,2,3,4]
list2 = [5,6,"BeiJing",7,8]
#列表的拼接
print("list1 + list2:",list1 + list2)
#列表的乘法
print("list1*2:",list1*2)
#判断元素是否存在于列表中
print("3 in list1?", 3 in list1)
print("100 in list1?", 100 in list1)
#迭代
for element in list1:
    print(element)
#列表嵌套
list3 = [list1, list2]
print("list3:", list3)

#栈 append(obj):添加元素到列表尾部；pop():从列尾取出元素。
#通过 append(obj) 函数最后添加的元素，可以通过 pop() 函数最先取出来，也就是“后进先出”，这种数据结构称为“栈”。利用列表的两个内建方法，很容易实现“栈”这种数据结构。
#初始化一个列表
stack1 = [1, 2, 3, 4, 5]
#向表尾添加元素
stack1.append(123)
print("stack1:",stack1)
#从表尾取出元素
print("stack1.pop():",stack1.pop())


#元组()
#列表采用方括号 []，元组采用圆括号 ()；
#元组中的元素不能改变，元组一旦创建就不能再对其中的元素进行增、删、改，只能访问。
tuple1 = ()
tuple2 = (12,)
tuple3 = (1, 2, 3, 4, 5)
tuple4 = (3.14, 5.96, 1897, 2020, "China", 3+4j)
tuple5 = 4, 5, 6, 7
#不过需要注意：
#如果元组只有一个元素，那么这个元素后面要加逗号，如 tuple2，否则将被认为是一个基本数据类型，而不是元组；
#创建元组，可以没有括号，元素之间用逗号隔开即可。

tuple1 = (3.14, 5.96, 1897, 2020, "China", 3+4j)
print("tuple1[2]:",tuple1[2])
print("tuple1[1:3]:",tuple1[1:3])
tuple1 = (3.14, 5.96, 1897, 2020, 1949)
#求元组的长度 len(tuple)
print("The length of the tuple:", len(tuple1))
#求元组中元素的最大值：max(tuple)
print("The largest of the tuple:",max(tuple1))
#求元组中元素的最小值：min(tuple)
print("The smallest element in the tuple: ", min(tuple1))
#统计某个元素在元组中出现的次数：tuple.count(obj)
print("The number of times 1949 appears: ", tuple1.count(1949))
#从元组中找出某个值第一个匹配项的索引位置：tuple.index(obj)
print("The index of the first location of 1949: ", tuple1.index(1949))

tuple1 = (1,2,3,4)
tuple2 = (5,6,"BeiJin",7,8)

#元组拼接
print("tuple1 + tuple2:",tuple1 + tuple2)

#元组乘法
print("tuple1*2:",tuple1*2)

#判断元素是否存在于元组中
print("3 in tuple1?",3 in tuple1)
print("100 in tuple1?",100 in tuple1)

#迭代
for element in tuple1:
    print(element)
    
#元组嵌套
tuple3 = [tuple1, tuple2]
print("tuple3:", tuple3)

#字典
#创建几个字典
dict1 = {"ID0012":"ZhangSan", "ID0019":"LiSi", "ID0015":"WangWu"}
dict2 = {1:"BeiJin",3:"ShangHai",5:"HangZhou"}
dict3 = {"Excellent":100, "Good":80, "Pass":60, "Fail":50}
#字典也可以嵌套
dict4 = {"A":["LiTong","XiaoMing"], "B":["XiaoHong","XiaoHua"]}

dict1 = {"Excellent":100, "Good":80, "Pass":60, "Fail":50}
dict2 = {1:"BeiJin",3:"ShangHai",5:"HangZhou"}
print("dict1['Good']:", dict1['Good'])
print("dict2[1]:", dict2[1])
print("dict1.get('Good'):", dict1.get('Good'))

#修改字典中的元素
dict1 = {"Excellent":100, "Good":80, "Pass":60, "Fail":50}
dict1['Good'] = 85
print("dict1['Good']:", dict1.get('Good'))
dict1 = {"Excellent":100, "Good":80, "Pass":60, "Fail":50}
#删除字典中的一个元素
del dict1['Good']
print("dict1:", dict1)
#使用内建方法pop(key)删除指定元素
dict1.pop('Pass')
print("dict1:", dict1)
#清空字典
dict1.clear()
print("dict1:", dict1)

#删除字典
del dict1

dict1 = {"Excellent":100, "Good":80, "Pass":60, "Fail":50}

#字典的常用内建方法
#计算字典的长度
print("The length of the dict1: ", len(dict1))
#获取字典中所有的键
print("Get all the keys in dict1:\n", dict1.keys())
#获取字典中所有的值
print("Get all the values in dict1:\n", dict1.values())
#获取字典中所有的键值对
print("Get all the key-value pairs in dict1:\n", dict1.items())

#集合
#集合的特点：1、确定性，集合中的元素必须是确定的；2、互异性，集合中的元素互不相同；3、无序性，集合中的元素没有先后之分。
#注意：可以用大括号（{}）创建集合。但需要注意，如果要创建一个空集合，必须用 set() 而不是 {} ；后者创建一个空的字典。
country1 = {'China', 'America', 'German'}
country2 = set('China')
country3 = set()

print("country1:",country1)
print("country2:",country2)
print("country3:",country3)

setA = {'A', 'B', 'C'}

print("setA:",setA)
setA.add('D')
print("setA.add('D'):",setA)
setA.add('A')
print("setA.add('A'):",setA)
setA.remove('A')
print("setA.remove('A'):",setA)

#集合的运算   交集、并集、补集
setA = {'A', 'B', 'C'}
setB = {'D', 'C', 'E'}
#交集
print("setA & setB:",setA&setB)
#并集
print("setA | setB:",setA|setB)
#差集
print("setA - setB:",setA-setB)
















