# '''
# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，
# 第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。
# 假设第一步已经完成了，第二步应该如何解析HTML呢？
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：
# '''
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('<%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&#%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')
# # 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。

# 小结:利用HTMLParser，可以把网页中的文本、图像等解析出来。
# 练习：
# 找一个网页，用浏览器查看源码并复制。
# work
from html.parser import HTMLParser
# from html.entities import name2codepoint
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self.__parsedata='' # 设置一个空的标志位

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == 'time':
            self.__parsedata = 'time'
        if ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        if ('class', 'event-location') in attrs:
            self.__parsedata = 'location'

    def handle_endtag(self, tag):
        self.__parsedata = ''# 在HTML 标签结束时，把标志位清空

    def handle_data(self, data):
        if self.__parsedata == 'name':
            print('会议名称:%s' % data) # 通过标志位判断，输出打印标签内容

        if self.__parsedata == 'time':
            print('会议时间:%s' % data)

        if self.__parsedata == 'year':
            if re.match(r'\s\d{4}', data): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                print('会议年份:%s' % data.strip())

        if self.__parsedata == 'location':
            print('会议地点:%s' % data)
            print('----------------------------------')

parser = MyHTMLParser()

URL = 'https://www.python.org/events/python-events/'

with request.urlopen(URL, timeout=15) as f:  # 打开网页并取到数据
    data = f.read()
parser.feed(data.decode('utf-8'))


