#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 下午2:51
# @Author  : Aries
# @Site    :
# @File    : smtp_moudel.py
# @Software: PyCharm

# 仔细观察，发现如下问题：
#
# 邮件没有主题；
# 收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
# 明明收到了邮件，却提示不在收件人中。
# 这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，
# 所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件
# todo 发件人and收件人并不是直接发送smtp,而是发给MTA的文本中的
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')
# todo 发送普通文本
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# todo 发送html
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
# todo 发送附件
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
msg = MIMEMultipart()
with open('/Users/houruixiang/python/python-master/com/hrx/third_party/test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
msg['From'] = _format_addr('you father <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s> ' % to_addr)
msg['Subject'] = Header('来自lily的问候...', 'utf-8').encode()
# todo 发送图片
# 如果要把一个图片嵌入到邮件正文中怎么做？直接在HTML邮件中链接图片地址行不行？答案是，
# 大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。
#
# 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，
# 在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
# todo cid:0 就是第一个附件  如果有多个附件依次排序  当然,如果不加下面代码,就仅仅是发送附件而已
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8'))
# todo 当然考虑到古老的邮件应用看不了链接  所以我们支持文本和连接同时发

server = smtplib.SMTP(smtp_server, 25)
# todo 加密SMTP
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，
# 可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
#
# 某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。
#
# 必须知道，Gmail的SMTP端口是587，因此，修改代码如下：
# todo 建立安全连接  调用starttls就建立了安全连接
server.starttls()

server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


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
