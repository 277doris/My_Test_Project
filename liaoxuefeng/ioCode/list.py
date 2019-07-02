#coding：utf-8
#序列化：
# d = dict(name='Bob', age=20, score=88)
#我们把变量从内存中变成可存储或传输的过程称为“序列化，在python中也叫pickling
#序列化之后，就可以把内容写入磁盘，通过网络传输到别的机器上
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
#
# import pickle
# d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))
# # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# # 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
#
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# import pickle
# #当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以
# #直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)


#python内置的json模块提供了非常完善的json格式转换
# import json
# d = dict(name='Bob', age=20, score=88)
# json.dumps(d)
# print(json.dumps(d))
# #dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# #要把json转换成python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
# json_str = '{"age": 20, "name": "Bob", "score": 80}'
# json.loads(json_str)
# print(json_str)


# json进阶
# import json
#
# class Student(object):
#
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# s = Student('Bob', 20, 88)
# print(json.dumps(s))
# #运行代码，毫不留情地得到一个TypeError：

import json
# class Student(object):
#
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# #可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
# def student2dict(std):
#     return {
#             'name': std.name,
#             'age': std.age,
#             'score': std.score
#     }
# s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict))
#Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON

# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
# print(json.dumps(s, default=lambda obj: obj.__dict__))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，
# 我们传入的object_hook函数负责把dict转换为Student实例：
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2student))

# 小结
# Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
#
# json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化
# 或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，接口简单易用、扩展性和灵活性强。

# work:对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：

import json
obj = dict(name='小米', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
# 如果ensure_ascii为True(默认值)，则输出保证将所有输入的非ASCII字符转义。如果确保ensure_ascii为False，这些字符将原样输出。
s = json.dumps(obj, ensure_ascii=False)
print(s)

