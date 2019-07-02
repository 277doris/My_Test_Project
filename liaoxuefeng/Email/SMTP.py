# # SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# # Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
# # 首先，我们来构造一个最简单的纯文本邮件：
# from email.mime.text import MIMEText
# # 第一个参数：邮件正文   第二个参数：MIME的subtype，plain纯文本   第三个参数：编码格式'utf-8'
# msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
# # 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
# # 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
# # 然后，通过SMTP发出去：
# # 输入email地址和口令
# from_addr = input('From:854018766@qq.com ')
# password = input('Password:dontgwrtwjjxbcfb ')
# # 输入收件人地址
# to_addr = input('To:2264866101@qq.com ')
# # 输入SMTP服务器地址：
# smtp_server = input('SMTP server:smtp.qq.com ')
#
# import smtplib
# server = smtplib.SMTP(smtp_server, 25)      # SMTP协议的默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, [to_addr], msg.as_string())
# server.quit()
#
# # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。
# # login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，
# # 邮件正文是一个str，as_string()把MIMEText对象变成str。

# # 如果一切顺利，就可以在收件人信箱中收到我们刚发送的Email：
# 注意：password是“QQ邮箱-设置-账号-开启服务-POP3/SMTP中的口令，需要开启此服务。

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server:  ')

msg = MIMEText('我用python写的邮件啊', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('汤写的用python自动发送邮件……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


