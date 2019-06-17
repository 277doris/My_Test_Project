#coding:utf-8
import os
os.name
#操作文件和目录
# # 查看文件的绝对路径
# os.path.abspath('.')
# print(os.path.abspath('.'))
# #在某个目录下创建一个新目录，首先把新目录的完整路径表示出来：
# os.path.join('C:/Users/22648/learngit/liaoxuefeng/ioCode', 'testdir')
# #然后创建一个目录
# os.mkdir('C:/Users/22648/learngit/liaoxuefeng/ioCode/testdir1')
# #删除掉一个目录
# os.rmdir('C:/Users/22648/learngit/liaoxuefeng/ioCode/testdir')
#注意：
#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
#同样要拆分路径时，要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
#print(os.path.split('C:/Users/22648/learngit/liaoxuefeng/ioCode/testdir1'))

# #对文件重命名：
# os.rename('aa.txt', 'aa.py')
# 删掉文件:
# os.remove('aa.py')

# 比如我们要列出当前目录下的所有目录，只需要一行代码：
[x for x in os.listdir('.') if os.path.isdir(x)]
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 要列出所有的.py文件，也只需一行代码：
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

