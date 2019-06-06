#coding:utf-8

# import unittest
# from stu import Student
#
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 59)
#         s2 = Student('Lisa', 49)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
# if __name__ == '__main__':
#     import doctest
#     unittest.main()

# #doctest文档测试
# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.
#
#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

'''
什么输出也没有。这说明我们编写的doctest运行都是正确的。如果程序有问题，比如把__getattr__()方法注释掉，再运行就会报错：
1 items had failures:
   2 of   9 in __main__.Dict
***Test Failed*** 2 failures.
'''

def fact(n):
    '''
    Calculate 1*2*...*n
    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
      ...
    ValueError
    '''

    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()