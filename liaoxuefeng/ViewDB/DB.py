# 你可以用一个文本文件保存，一行保存一个学生，用,隔开：
# Michael,99
# Bob,85
# Bart,59
# Lisa,87
# 你还可以用JSON格式保存，也是文本文件：
# [
#     {"name":"Michael","score":99},
#     {"name":"Bob","score":85},
#     {"name":"Bart","score":59},
#     {"name":"Lisa","score":87}
# ]
# 你还可以定义各种保存格式，但是问题来了：
# 存储和读取需要自己实现，JSON还是标准，自己定义的格式就各式各样了；
# 不能做快速查询，只有把数据全部读到内存中才能自己遍历，但有时候数据的大小远远超过了内存（比如蓝光电影，40GB的数据）
# 根本无法全部读入内存。
# 为了便于程序保存和读取数据，而且，能直接通过条件快速查询到指定的数据，就出现了数据库（Database
# 这种专门用于集中存储和查询的软件。数据库软件诞生的历史非常久远，早在1950年数据库就诞生了。经历了网状数据库
# 层次数据库，我们现在广泛使用的关系数据库是20世纪70年代基于关系模型的基础上诞生的。
# 关系模型有一套复杂的数学理论，但是从概念上是十分容易理解的。举个学校的例子：
# 假设某个XX省YY市ZZ县第一实验小学有3个年级，要表示出这3个年级，可以在Excel中用一个表格画出来：

# 数据库类别
# 既然我们要使用关系数据库，就必须选择一个关系数据库。目前广泛使用的关系数据库也就这么几种：
# 付费的商用数据库：
# Oracle，典型的高富帅；
# SQL Server，微软自家产品，Windows定制专款；
# DB2，IBM的产品，听起来挺高端；
# Sybase，曾经跟微软是好基友，后来关系破裂，现在家境惨淡。
# 这些数据库都是不开源而且付费的，最大的好处是花了钱出了问题可以找厂家解决，不过在Web的世界里，常常需要部署成千上万的数
# 据库服务器，当然不能把大把大把的银子扔给厂家，所以，无论是Google、Facebook，还是国内的BAT，都选择了免费的开源数据库：
# MySQL，大家都在用，一般错不了；
# PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；
# sqlite，嵌入式数据库，适合桌面和移动应用。
# 作为Python开发工程师，选择哪个免费数据库呢？当然是MySQL。因为MySQL普及率最高，出了错，可以很容易找到解决方法。
# 而且，围绕MySQL有一大堆监控和运维的工具，安装和使用很方便。

# 在使用SQLite前，我们先要搞清楚几个概念：
# 表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，如学生的表，班级表，学校表等等。表和表之间通过外键关联
# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
# 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
# 由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。
# 我们在Python交互式命令行实践一下：

# # 导入SQLite驱动：
# import sqlite3
# # 连接到SQLite数据库
# # 数据库文件是test.db
# # 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect('test.db')
# # 创建一个Cursor:
# cursor = conn.cursor()
# # 执行一条SQL语句，创建user表：
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20), pwd varchar(20))')
# # 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# cursor.execute('insert into user (name, pwd) values (\'abc\', \'password\')')
# # 通过rowcount获得插入的行数
# print(cursor.rowcount)
# # 关闭Cursor
# cursor.close()
# # 提交事务：
# conn.commit()
# # 关闭Connetion:
# conn.close()
#
# # 我们再试试查询记录：
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# # 执行查询语句：
# cursor.execute('select * from user where id=?', ('1',))
# values = cursor.fetchall()
# print(values)
# # 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# # 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
# # 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
# # 获得查询结果集：
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()

# 小结
# 在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
# 要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
# 如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。

# work:请编写函数，在Sqlite中根据分数段查找指定的名字：
# -*- coding: utf-8 -*-
import os, sqlite3
db_file = os.path.join(os.path.dirname(__file__), 'test.db')

if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(r"select name from user where score>=? and score <=? order by score",(low,high))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return [x[0] for x in values]

# 测试
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('Pass')

