import imaplib

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i: i+n]

conn = imaplib.IMAP4_SSL('imap.exmail.qq.com', 993)
imaplib.Debug = 1
conn.login("name@domain.com", "password")

# 列出邮箱中的文件夹
box_list_info_buffer = conn.list()
print(box_list_info_buffer[1])

conn.select('INBOX')   # 选择默认邮箱

# 获取所有邮件的id
ttype, data = conn.search(None, 'ALL')
data_list =  data[0].split()

for i in list(chunks(data_list, 1000)):
    conn.store(b",".join(i), '+FLAGS', '\\Deleted')

conn.expunge()
conn.logout()