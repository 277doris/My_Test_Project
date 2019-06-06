#coding:utf-8
#如果你听说过“测试驱动开发”（TDD：Test-Driven Development）
#单元测试是针对一个模块、一个函数或者一个类来进行正确性检验的测试工作

# import unittest
#
# from mydict import Dict
#
# class TestDict(unittest.TestCase):
# #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         #调用assertEqual等方法断言输出是否是我们所期望的
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         #断言assertRaises就是期待抛出指定类型的Error
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
#
# #运行单元测试
# if __name__ == '__main__':
#     unittest.main()

#可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
