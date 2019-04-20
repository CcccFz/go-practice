# -*- coding: utf-8 -*-

""" 用于清除指定目录中的中间文件，只留下源码
"""

import os
import sys
import shutil

RMV_DIR = [u'Debug']
RMV_EXT = ['.dsp', '.dsw', '.ncb', '.opt', '.plg', '.pyc']


def get_rmv_paths(root):
    rmv_paths = set()
    for current, dirs, files in os.walk(root):
        if current in rmv_paths:
            continue
        if os.path.split(current)[-1] in RMV_DIR:
            rmv_paths.add(current)
            continue
        for f in files:
            if os.path.splitext(f)[-1] in RMV_EXT:
                rmv_paths.add(os.path.join(current, f))
    return rmv_paths

def ckear_middle_files(root):
    rmv_paths = get_rmv_paths(root)
    for str_path in rmv_paths:
        if os.path.isfile(str_path):
            os.remove(str_path)
        else:
            shutil.rmtree(str_path)


if __name__ == '__main__':
    try:
        root = sys.argv[1]
    except:
        root = os.getcwd()
    finally:
        ckear_middle_files(root)

