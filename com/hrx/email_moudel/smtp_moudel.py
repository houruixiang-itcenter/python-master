#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 下午2:51
# @Author  : Aries
# @Site    :
# @File    : smtp_moudel.py
# @Software: PyCharm

# todo SMTP是发送邮件的协议,python内置对SMTP的支持,可以发纯文本邮件,HTML邮件以及带附件的邮件
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
import smtplib
from email.mime.text import MIMEText

# 第一个参数是邮件正文 第二个参数就是MIME的subtype,传入plain意思就是纯文本
# todo 构造一个最简单的纯文本文件
msg = MIMEText('请协同一下', 'plain', 'utf-8')
# 然后通过SMTP发出去
# TODO 输入发件人地址
form_addr = input('from: ')
form_pwd = input('pwd: ')
# todo 输入收件人地址
to_addr = input('To: ')
smtp_server = input('SMTP server:')

server = smtplib.SMTP(smtp_server, 25)  # SMT默认端口是25
# 打印交互的所有信息
server.set_debuglevel(1)
# 登录自己的邮箱
server.login(form_addr, form_pwd)
# 发送邮件
server.sendmail(form_addr, to_addr, msg.as_string())
server.quit()



