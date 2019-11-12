# coding:utf-8
import unittest


def add(a, b):
    """计算加法"""
    return a + b

# 使用for循环
'''
from random import randint
class AddTest(unittest.TestCase):

    def test_case(self):
        for i in range(3):
            a = randint(-1, 3)
            b = randint(-1, 3)
            print("a—>", a)
            print("b—>", b)
            c1 = a + b
            c2 = add(a, b)
            print(c1)
            print(c2)
            self.assertEqual(c1, c2)
'''

# 使用hypothesis生成测试数据：
from hypothesis import given, settings
import hypothesis.strategies as st


class AddTest(unittest.TestCase):

    # @setting()装饰器中通过max_examples用来控制随机数的个数
    @settings(max_examples=10)
    # @given() 装饰测试用例，调用strategies 模块下面的 integers() 方法生成随机的测试数。
    @given(a=st.integers(), b=st.integers())
    def test_case(self, a, b):
        print("a—>", a)
        print("b—>", b)
        c1 = a + b
        c2 = add(a, b)
        print(c1, c2)
        self.assertEqual(c1, c2)


if __name__ == '__main__':
    unittest.main()
