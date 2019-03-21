#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 下午9:00
# @Author  : Aries
# @Site    : 
# @File    : PopParser.py
# @Software: PyCharm

# 输出纯文本Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。
#
# 所以我们要递归地打印出Message对象的层次结构：
from email import message
from email.header import decode_header
from email.utils import parseaddr

#  todo 解析Sbuject或者email中包含的名字
def decode_str(s):
	value, charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value

# decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。
# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
	charset = msg.get_charset()
	if charset is None:
		content_type = msg.get('Content-Type', '').lower()
		pos = content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos + 8:].strip()
	return charset


# intent 用于缩进显示:
def print_info(msg, indent=0):
	# assert isinstance(msg, message)
	if indent == 0:
		for header in ['From', 'To', 'Subject']:
			value = msg.get(header, '')
			if value:
				if header == 'Subject':
					value = decode_str(value)
				else:
					hdr, addr = parseaddr(value)
					name = decode_str(hdr)
					value = u'%s <%s>' % (name, addr)
				print('%s%s:  %s' % ('  ' * indent, header, value))
	
	# todo 获取正文
	if msg.is_multipart():
		parse = msg.get_payload()
		for n, part in enumerate(parse):
			print('%spart %s' % (' ' * indent, n))
			print('%s-----------------------' % ('' * indent))
			print_info(part, indent + 1)
	else:
		content_type = msg.get_content_type()
		if content_type == 'text/plain' or content_type == 'text/html':
			content = msg.get_payload(decode=True)
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
			print('%sTfext: %s' % ('' * indent, content + '...'))
		else:
			print('%s Attachment: %s' % ('  ' * indent, content_type))
# 小结
# 用Python的poplib模块收取邮件分两步：第一步是用POP3协议把邮件获取到本地，
# 第二步是用email模块把原始邮件解析为Message对象，然后，用适当的形式把邮件内容展示给用户即可。