'''
IO在计算机中指Input/Output，也就是输入和输出。由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，
涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。
比如你打开浏览器，访问新浪首页，浏览器这个程序就需要通过网络IO获取新浪的网页。浏览器首先会发送数据给新浪服务器，
告诉它我想要首页的HTML，这个动作是往外发数据，叫Output，随后新浪服务器把网页发过来，这个动作是从外面接收数据，叫Input。
所以，通常，程序完成IO操作会有Input和Output两个数据流。当然也有只用一个的情况，比如，从磁盘读取文件到内存，
就只有Input操作，反过来，把数据写到磁盘文件里，就只是一个Output操作。
IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。
Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。对于浏览网页来说，
浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。
由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。举个例子来说，
比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘要接收这100M数据可能需要10秒，怎么办呢？有两种办法：
第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；
另一种方法是CPU不等待，只是告诉磁盘，于是，后续代码可以立刻接着执行，这种模式称为异步IO。
同步和异步的区别就在于是否等待IO执行的结果。
很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。想想看，
你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是回调模式，
如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。总之，异步IO的复杂度远远高于同步IO。
'''

'''
文件读写：
读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中
读取数据（读文件），或者把数据写入这个文件对象（写文件）。
'''
# #读文件，标示符'r'表示读，这样，我们就成功地打开了一个文件。
# f = open('C:/Users/22648/Desktop/err.py', 'r')
# #调用read()方法可以一次读取文件的全部内容
# print(f.read())
#最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，
#并且操作系统同一时间能打开的文件数量也是有限的：
# f.close()
#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，
#我们可以使用try ... finally来实现：
# f = open('C:/Users/22648/Desktop/err.py', 'r')
# try:
#     f = open('C:/Users/22648/Desktop/err.py', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# with open('C:/Users/22648/Desktop/err.py', 'r') as f:
#     print(f.read())
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
'''
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，
每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
因此，要根据需要决定怎么调用。如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
如果是配置文件，调用readlines()最方便：
'''
# for line in f.readlines():
#     print(line.strip()) # 把末尾的'\n'删掉

#file-like Object
#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，
#网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

#二进制文件
#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
# f = open('C:/Users/22648/Desktop/6月份上线安排.png', 'rb')
# print(f.read())     #十六进制表示的字节
# f.close()

#字符编码
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数。例如要读取GBK文件：
# f = open('C:/Users/22648/Desktop/6月份上线安排.png', 'r', encoding='gbk')
# f.read()
#open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
# f = open('C:/Users/22648/Desktop/6月份上线安排.png', 'r', encoding='gbk', errors='ignore')

# #写文件
# f = open('C:/Users/22648/Desktop/test.txt', 'w')
# f.write('Hello, world!')
# f.write('你好！')
# f.close()
# #用with语句比较保险
# with open('C:/Users/22648/Desktop/test.txt', 'w') as f:
#     f.write('Use with language!')
#以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？
#可以传入'a'以追加（append）模式写入。
# with open('C:/Users/22648/Desktop/test.txt', 'a') as f:
#     f.write('Use with language!')

#练习：
# #read
# with open('C:/Users/22648/Desktop/test.txt', 'r') as f:
#     #一定不要忘了加()
#     s = f.read()
#     print(s)
#write
# # with open('C:/Users/22648/Desktop/test.txt', 'w') as f:
# #     f.write('I am so happy !')
# #
# # #用参数'a'替换'w'，以append的形式在末尾添加，而不是把之前内容覆盖
# # with open('C:/Users/22648/Desktop/test.txt', 'a') as f:
# #     f.write('Do you know ?')
# #read
# with open('C:/Users/22648/Desktop/test.txt', 'r') as f:
#     #一定不要忘了加()
#     # s = f.read()    #全部一次性读完
#     # print(s)
#     for line in f.readlines():
#         print(line.strip())  # 一行行读






