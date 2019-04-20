# -*-coding: utf-8 -*-

"""
甩手工具从淘宝网上爬下来的宝贝图片，是用数字命名的。如1, 10, 12, 2, 3。
这样图片放置顺序是不对的。
解决方法是，将数字转化为字母，如1-->a，2-->b，10-->j。
"""

import os
import re
from functools import partial

pattern = re.compile(r'(\d+)')
for path, dirs, files in os.walk(os.getcwd()):
    join = partial(os.path.join, path) 
    for oldname in files:
        newname = pattern.sub(lambda r: chr(96+int(r.group(1))), oldname)
        if oldname != newname:
            os.rename(join(oldname), join(newname))

