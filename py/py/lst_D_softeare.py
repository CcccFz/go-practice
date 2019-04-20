# -*-coding: utf-8 -*-

import os

"""
用于列出D盘的所有安装软件。
重装系统前执行一次，方便重装系统后，确认需要安装的软件。
"""

D = r'D:\\'
softwares = []
for item in os.listdir(D):
    if os.path.isdir(os.path.join(D, item)):
        softwares.append(' -- %s' % item)

with open('software.list.txt', 'w') as wf:
    wf.write('\n'.join(softwares))
