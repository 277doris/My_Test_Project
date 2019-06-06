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

'''
#定义一个学生的类
class Student(object):

    def __init__(self, name, score):     #对实例进行初始化
        self.name = name
        self.score = score

    def get_grade(self):        #定义类的属性
        if self.score >= 90:
            return 'A'
        if self.score >= 60:
            return 'B'
        else:
            return 'C'
#实体化类
lisa = Student('Lisa', 99)
bart = Student('Bart', 57)
#打印类的实例及属性
print (lisa.name, lisa.score, lisa.get_grade())
print (bart.name, bart.score, bart.get_grade())
'''
'''
#创建类
class Student(object):
    #初始化类的属性
    def __init__(self, name, score):
        self.name = name
        self.score = score
    #定义类的属性
    def get_grade(self):
        if self.score >= 90:
            return '您的本次考试优秀，被评为A'
        if self.score > 60:
            return '您的本次考试合格，被评为B'
        else:
            return '很抱歉，您的本次考试未通过，被评为C'
#实例化类
lisa = Student('Lisa', 90)
bart = Student('Bart', 55)
print(lisa.name, lisa.score, lisa.get_grade())
print(bart.name, bart.score, bart.get_grade())
'''

'''
#访问限制：
#创建一个类
class Student(object):
    #初始化类的属性
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    #私有化类的属性
    def get_gender(self):
        return self.__gender
    #重新定义类，检查参数
    def set_gender(self, gender):
        if gender.lower() in ['male', 'female']:
            self.__gender = gender
        else:
            raise ValueError('Wrong!')
#实例化类
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败！')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败！')
    else:
        print('测试成功！')
'''

''' 
#继承和多类
#在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称
#为基类、父类或超类（Base class、Super class）。
#比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：

# class Animal(object):
#     def run(self):
#         print('Animal is running……')
# class Dog(Animal):
#     def run(self):
#         print('Dog is running……')
#     def size(self):
#         print('Dog is big……')
# class Cat(Animal):
#     def run(self):
#             print('Cat is running……')
#     def eat(self):
#         print('Cat like eat fish!')
# dog = Dog()
# dog.run()
# dog.size()
# cat = Cat()
# cat.eat()
#
# a = list() #a是list类型
# b = Animal() #b是Animal类型
# c = Dog() #c是Dog类型
# #判断一个变量是否是某个类型可以用isinstance()判断
# print(isinstance(a, list))      #True
# print(isinstance(b, Animal))    #True
# print(isinstance(c, Dog))       #True
# print(isinstance(c, Animal))    #True
# #在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
# print(isinstance(b, Dog))       #False
# #要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
# def run_twice(animal):
#     animal.run()
#     animal.run()
# #当我们传入Animal的实例时，run_twice()就打印出：
# run_twice(Animal())
# run_twice(Cat())
# class Tortoise(Animal):
#     def run(self):
#         print('Tortoise is running slowly……')
# run_twice(Tortoise())
#新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法
#都可以不加修改地正常运行，原因就在于多态。
'''
'''
多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是
Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，
就会自动调用实际类型的run()方法，这就是多态的意思：对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的
代码是如何调用的。这就是著名的“开闭”原则：对扩展开放：允许新增Animal子类；对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
'''
'''
#静态语言VS动态语言
#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
# 小结：继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

#获取对象信息
#基本类型都可以用type()判断
# print(type(123))    #<class 'int'>
# print(type('123'))  #<class 'str'>
# print(type(None))   #<class 'NoneType'>
#如果一个变量指向函数或者类，也可以用type()判断
# print(type(abs))    #<class 'builtin_function_or_method'>
#但是type()函数返回的是class类型，如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
# print(type(123) == type(345))
# print(type(123) == type('345'))
# print(type(123) == int)
#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数，需要在types模块中定义常量

# import types
# def fn():
#     pass
# print(type(fn) == types.FunctionType)

#使用isinstance()
#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
#如果继承的关系是：object——>Animal——>Dog——>Husky
#那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
# class Animal(object):
#     def run(self):
#         print('Animal is running……')
# class Dog(Animal):
#     def run(self):
#         print('Dog is running……')
#     def size(self):
#         print('Dog is big……')
# class Husky(Animal):
#     pass
# a = Animal()
# d = Dog()
# h = Husky()
# print(isinstance(a, Animal))
# print(isinstance(d, Husky))
# print(isinstance(d, Dog) and isinstance(d, Animal))
#
# print(isinstance([1, 2, 3], (list, tuple)))
# print(isinstance((1, 2, 3), (list, tuple)))
# #总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))
print(len('ABC'))
print('ABC'.lower())

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
#假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，
#则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
'''

'''  
#实例属性和类属性，根据类创建的实例可以任意绑定属性，给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
    def __init__(self, name):
        self.name = name
s = Student('Bob')
s.score = 90

#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student(object):
    name = 'Student'
s = Student()   #创建实例s
print(s.name)   #打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name) # 打印类的name属性
s.name = 'Michael'  # 给实例绑定name属性
print(s.name)   # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name  # 如果删除实例的name属性
print(s.name)   # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
'''

class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')