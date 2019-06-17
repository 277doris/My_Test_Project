# # n = 10240099
# # b1 = (n & 0xff000000) >> 24
# # print(b1)
# # b2 = (n & 0xff0000) >> 16
# # print(b2)
# # b3 = (n & 0xff00) >> 8
# # print(b3)
# # 非常麻烦。如果换成浮点数就无能为力了。
# import struct
# s = struct.pack('>I', 10240099)
# print(s)
# # pack的第一个参数是处理指令，'>I'的意思是：
# # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# # 后面的参数个数要和处理指令一致。
# # unpack把bytes变成相应的数据类型：
# su = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
# print(su)
# # 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
# # BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
# # 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图； 一个4字节整数：表示位图大小； 一个4字节整数：保留位，始终为0；
# # 一个4字节整数：实际图像的偏移量； 一个4字节整数：Header的字节数； 一个4字节整数：图像宽度； 一个4字节整数：图像高度； 一个2字节整数：始终为1； 一个2字节整数：颜色数。
# # 所以，组合起来用unpack读取：
# ssu = struct.unpack('<ccIIIIIIHH', s)
# print(ssu)

# # work
# import struct
# def bmp_info(data):
#
#     bmpbytes = data[:30]
#     s = struct.unpack('<ccIIIIIIHH', bmpbytes)
#
#     if s[1] == b'M':
#         print('该文件是位图文件。')
#         return {
#             'width': s[6],
#             'height': s[7],
#             'color': s[9],
#         }
#     else:
#         print('该文件不是位图文件。')