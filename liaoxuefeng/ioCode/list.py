#coding：utf-8
#序列化：
# d = dict(name='Bob', age=20, score=88)
#我们把变量从内存中变成可存储或传输的过程称为“序列化，在python中也叫pickling
#序列化之后，就可以把内容写入磁盘，通过网络传输到别的机器上
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

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
# # d = dict(name='Bob', age=20, score=88)
# # json.dumps(d)
# # print(d)
# #dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# #要把json转换成python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
# json_str = '{"age": 20, "name": "Bob", "score": 80}'
# json.loads(json_str)
# print(json_str)

#json进阶
# import json

# class Student(object):
#
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#
# s = Student('Bob', 20, 88)
# print(json.dumps(s))
# #运行代码，毫不留情地得到一个TypeError：

import json
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

#可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
#Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON

