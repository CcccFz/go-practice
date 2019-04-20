# -*- coding:utf-8 -*-

import smtplib  
#import os  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
#from email import encoders
  
user = 'ccccfz@163.com'  
pwd = 'fz.19921218'  
to = ['1980884174@qq.com']  
msg = MIMEMultipart()  
msg['Subject'] = 'Redis内存超标警报'  
content1 = MIMEText('服务器内存已超过预设最大内存', 'plain', 'utf-8')  
msg.attach(content1)  
  
#-----------------------------------------------------------  
s = smtplib.SMTP('smtp.163.com')  
s.login(user, pwd)  
s.sendmail(user, to, msg.as_string())  
print('发送邮件成功')  
s.close()  
