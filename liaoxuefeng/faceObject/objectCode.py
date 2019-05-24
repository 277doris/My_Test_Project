'''
1、面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，
一个对象包含了数据和操作数据的函数。
'''
#1、假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：
# stud1 = {'name': 'Michael', 'score': 98}
# stud2 = {'name': 'Bob', 'score': 70}
# #2、而处理学生成绩可以通过函数实现，比如打印学生的成绩：
# def print_score(stud):
#     print('%s : %s' % (stud['name'], stud['score']))
# #如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥
# #有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个
# # print_score消息，让对象自己把自己的数据打印出来。
# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()
'''
。Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，
比如，Bart Simpson和Lisa Simpson是两个具体的Student。
'''
'''
小结：数据封装、继承和多态是面向对象的三大特点
'''
'''上帝
class 类 (人) instance 实例 (你,我,他) 你会有些属性(身高,年龄,体重) 你会有些技能(吃饭,泡妞)
__init__ 方法的主要作用,就是初始化你的属性,这些属性,在上帝初始化你的时候就要赋予给你,比如zhangsan = Person(170,29,50)
这时上帝就把你创造出来了，也就是实例化了你，然后，你到底有哪些技能呢，这就看有没有在类里面定义了，如果有定义泡妞的技能，
那么你就可以调用泡妞的技能来泡妞，大致就是这样吧，看看下面的例子就更清楚了
class Person(object):
# 这里就是初始化你将要创建的实例的属性
    def __init__(self,hight,weight,age):
        self.hight = hight
        self.weight = weight
        self.age = age

# 定义你将要创建的实例所有用的技能
    def paoniu(self):
        print('你拥有泡妞的技能')

    def eat(self):
        print('you can eat')
# __init__就是初始化这个类person的属性property
def __init__(self,name,age,height):
    self.name = name
    self.age = age
    self.height = height
# 下面是定义你将要创建的实例的技能
def paoniu(self):
    print('你可以泡妞啦')
def eat(self):
    print('你可以吃东西啦')
def printheight(self):
    print('你的身高是: %s' % self.height)
def printname(self):
    print('%s: %s' % (self.name, self.age))
'''

# #2、类和实例：面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据
# # 类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# class Student(object):
#     pass
# #class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念
# # 我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# #定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
# bart = Student()
# print(bart)
# print(Student)
# #可以看到，变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，
# #而Student本身则是一个类。
# #可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
# bart.name = 'Bart Simpson'
# print(bart.name)
# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# # #注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，
# # #因为self就指向创建的实例本身。
# # #有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，
# # #Python解释器自己会把实例变量传进去：
# bart = Student('Bart Simpson', 59)
# print(bart.name)
# print(bart.score)
#3、数据封装：面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。
#我们可以通过函数来访问这些数据，比如打印一个学生的成绩：
# def print_score(std):
#     print('%s: %s' % (std.name, std.score))
# print_score(bart)
'''
但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义
访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
'''
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
# bart = Student('Doris', 99)
# bart.print_score()
#封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
#1、创建类
# class Student(object):
# #2、初始化实例的属性——实例化
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# #3、定义创建的实例所有用的技能——在类里定义技能
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
# #传入参数，将具体对象实例化
# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.score)
# print(bart.name, bart.score)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())
'''
小结：类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
'''

#在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
