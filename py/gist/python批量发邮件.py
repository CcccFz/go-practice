# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os
import time
import string
import urllib2
import smtplib
import datetime
import StringIO
import traceback
import distutils.dir_util
from urllib import urlencode
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.header import Header
from py_mail_all_receivers import RECEIVERS


def send_mails(fro, to, subject, files=[]):
    msg = MIMEMultipart()
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "ISO-8859-1, utf-8"
    msg['From'] = fro
    msg['Subject'] = Header(subject, 'utf-8')
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(subject, 'plain', 'utf-8'))

    # 添加附件
    for file in files:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file, 'rb').read().decode('utf-8').encode('gbk'))  # 构造文件转换编码, 不然附件要乱码
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file).encode('gbk'))
        msg.attach(part)

    smtp.sendmail(fro, to, msg.as_string())


if __name__ == '__main__':
    RECEIVERS = [
        {'loc': 'zjk', 'loc_cn': '张家口', 'to': ['jianjun@xxx.com.cn']},
    ]

    smtp = smtplib.SMTP('smtp.exmail.qq.com')
    smtp.login('cwkj@xxx.cn', '231111')

    # 循环向RECEIVERS发邮件
    for receiver in RECEIVERS:
        send_mails(
            'cwkj@xxx.cn',
            ['mou@xxx.cn', 'channel@xxx.cn'] + city['to'],
            '(%s)运营统计数据,系统自动发送,请不要回复!' % city['loc_cn'],
            files=[
                '/tmp/mail/statistics_jms0_report_%s.xls' % city['loc'],
                '/tmp/mail/statistics_jms1_report_%s.xls' % city['loc'],
                '/tmp/mail/statistics_jms2_report_%s.xls' % city['loc']
            ]
        )

    smtp.close()