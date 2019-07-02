
# 纯文本文件+HTML邮件+发送附件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

# # 发送纯文本文件
# msg = MIMEText('Hello, this email is send by Python...', 'plain', 'utf-8')

# 发送HTML邮件
# 如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，
# 再把第二个参数由plain变为html就可以了：
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
    # h1标签后面是hello加粗，p标签里是send by + python的一个超链。
# msg['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)           # 发件人
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)                      # 收件人
# msg['Subject'] = Header('汤编写的自动化邮件...', 'utf-8').encode()     # 标题

# 发送附件
# 如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个
# MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
# 邮件对象：
msg = MIMEMultipart()       # from email.mime.multipart import MIMEMultipart
msg['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)           # 发件人
msg['To'] = _format_addr('管理员 <%s>' % to_addr)                      # 收件人
msg['Subject'] = Header('汤编写的自动化邮件...', 'utf-8').encode()     # 标题
# # 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 发送图片
# 把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片：
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="C:cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase,从本地读取一个图片
with open('C://Users//22648/Desktop//test//图片//1.61M.jpg', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='1.61M.jpg')   # 需要from email.mime.base import MIMEBase
    # 加上必要的头部信息：
    mime.add_header('Content-Disposition', 'attachment', filename='1.61M.jpg')
    mime.add_header('Contet-ID', '<0>')
    mime.add_header('X-Attachment-ID', '0')
    # 把附件的内容读进来：
    mime.set_payload(f.read())
    # 用base64编码：
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 我们编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为如果包含中文，
# 需要通过Header对象进行编码。
# msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
# 再发送一遍邮件，就可以在收件人邮箱中看到正确的标题、发件人和收件人：

# 同时支持HTML和Plain格式
# 如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？
#
# 办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。
#
# 利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
#
# msg = MIMEMultipart('alternative')
# msg['From'] = ...
# msg['To'] = ...
# msg['Subject'] = ...
#
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# # 正常发送msg对象...
# 加密SMTP
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
#
# 某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。
#
# 必须知道，Gmail的SMTP端口是587，因此，修改代码如下：
#
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()
# # 剩下的代码和前面的一模一样:
# server.set_debuglevel(1)
# ...
# 小结
# 使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。
#
# 构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：
#
# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage
# 这种嵌套关系就可以构造出任意复杂的邮件。你可以通过email.mime文档查看它们所在的包以及详细的用法。
