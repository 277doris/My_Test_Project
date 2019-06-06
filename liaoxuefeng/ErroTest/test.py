#coding:utf-8
#程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，
#有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。
#第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()


#第二种方法：凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
# def foo(s):
#     n = int(s)
#     #assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()
#如果断言失败，assert语句本身就会抛出AssertionError
#程序中如果到处充斥着assert，在启动Python解释器时可以用-O参数来关闭assert（是英文大写字母O）

#第三种：logging
# import logging
# logging.basicConfig(level=logging.INFO)
# #INFO:root:n = 0
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
#这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，
#logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
#logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

#第四种pdb
# s = '0'
# n = int(s)
# print(10 / n)
# python -m pdb err.py

#第五种pdb.set_trace()
# import pdb
#
# s = '0'
# n = int(s)
# pdb.set_trace() #断点
# print(10 / n)
#运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行

