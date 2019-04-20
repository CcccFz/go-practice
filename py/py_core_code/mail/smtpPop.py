from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.qq.com'
POP3SRV = 'pop.qq.com'

origHdrs = ['From: 1980884174@qq.com',
            'To: 1980884174@qq.com',
            'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSrv = SMTP(SMTPSVR)
sendSrv.login('1980884174@qq.com', 'fz.19921218')
errs = sendSrv.sendmail('1980884174@qq.com', ('1980884174@qq.com',), origMsg)

sendSrv.quit()
assert len(errs) == 0, errs
sleep(10)

recvSrv = POP3(POP3SRV)
recvSrv.user('1980884174@qq.com')
recvSrv.pass_('fz.19921218')

rsp, msg, siz = recvSrv.retr(recvSrv.stat()[0])

sep = msg.index(b'')
recvBody = msg[sep+1:]
print(recvBody)