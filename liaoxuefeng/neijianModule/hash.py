# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
# 举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章
# 的摘要是'2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，
# 你可以一下子指出Bob篡改了你的文章，因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。
# 可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过
# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，
# 但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
#
# import hashlib
#
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
#
# # 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?' .encode('utf-8'))
# print(md5.hexdigest())

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
# import hashlib
#
# sha1 = hashlib.sha1()
# sha1.update('how to use shal in ' .encode('utf-8'))
# sha1.update('python hashlib?' .encode('utf-8'))
# print(sha1.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

'''
摘要算法应用：
摘要算法能应用到什么地方？举个常用例子：
任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：
name	    password
michael	    123456
bob	        abc999
alice	    alice2008
如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，
也就是能获取到所有用户的口令。
正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
username	password
michael	    e10adc3949ba59abbe56e057f20f883e
bob	        878ef96e86145580c38c87f0410ad153
alice	    99b1c2188db85afee403b1536010c2c9
当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，不一致，口令错误。
'''
# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
# 这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
# def calc_md5(password):
#     return get_md5(password + 'the-Salt')
# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
# 但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。
# 有没有办法让使用相同口令的用户存储不同的MD5呢？
# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。

# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
import hashlib

def calc_md5(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def login(user, password):
    if user not in db:
        return False
    else:
        return db[user] == calc_md5(password)

# 测试:
assert login('michael', '123456')       #   检查登录密码
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')  #   检查是否有别的账号登录
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')