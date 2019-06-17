import re
# print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))   #返回一个match对象
# print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))   #返回一个None
# # match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：

# test = '用户输入的字符串'
# if re.match(r'好饿', test):
#     print('ok')
# else:
#     print('failed')

#切分字符串：用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：
# # 'a b  c'.split(' ')
# print('a b  c'.split(' '))
#
# #无法识别连续的空格，用正则表达式试试：
# re.split(r'\s+', 'a  b   c')
# print(re.split(r'\s+', 'a  b   c'))
#
# #无论多少个空格都可以正常分割。加入,试试：
# re.split(r'[\s\,]+', 'a,b, c,  d')      #分割逗号
# print(re.split(r'[\s\,]+', 'a,b, c,  d'))
# # 再加入;试试：
# re.split(r'[\s\,\;]+', 'a,b;; c  d')        #分割逗号和分号\s\,\;
# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

#分组：除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
# m = re.match(r'^(\d{3})-(\d{3,8})-(\d{2,8})$', '010-12345-11')
# print(m)
# m.group(0)      #使用group分组，给函数传值，0代表原始字符串，1代表第一个子串，2代表第二个子串……
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))


# #贪婪匹配：最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
# re.match(r'^(\d+)(0*)$', '102300').groups()
# print(re.match(r'^(\d+)(0*)$', '102300').groups())
# #由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
# # 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
# re.match(r'^(\d+?)(0*)$', '102300').groups()
# print(re.match(r'^(\d+?)(0*)$', '102300').groups())

#编译
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
编译正则表达式，如果正则表达式的字符串本身不合法，会报错；用编译后的正则表达式去匹配字符串。
如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，
接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''

# import re
# #编译
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# #使用
# re_telephone.match('010-12345').groups()
# # print(re_telephone.match('010-12345').groups())
# re_telephone.match('010-8086').groups()
# # print(re_telephone.match('010-8086').groups())


import re
def is_valid_email(addr):
    r_addr = re.match(r'([0-1a-zA-Z.]*)@([a-z.]*)', addr)
    if r_addr is None:
        print('False')
        return False
    else:
        print(r_addr.groups())
        return True

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    rm = re.match('<(\w+\s+\w+)>', addr)      #\w可以匹配一个字母或数字,\s匹配任意字符，\s+表示至少有一个空白符
    if rm is None:
        return re.match('(\w+)@(\w+)', addr).group(1)
    else:
        return rm.group(1)

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

