# coding: gbk

import os
import re
import sys
import time
import ctypes
from collections import OrderedDict
from os import popen

STD_OUTPUT_HANDLE = -11
FOREGROUND_BLUE = 0x01
FOREGROUND_GREEN = 0x02
FOREGROUND_RED = 0x04
FOREGROUND_INTENSITY = 0x08
EXE_PATH = r'/usr/bin/typora'
ROOT_PATH = r'/home/ccccfz/Repos/ccccfz.coding.me'
SOURCE_PATH = os.path.join(ROOT_PATH, 'source')
POST_PATH = os.path.join(SOURCE_PATH, '_posts')
TITLE_PATTERN = re.compile(r'^([a-zA-Z0-9]+-)*[a-zA-Z0-9]+$')
CONTENT = """---
title: %s
date: %s
category: %s
---


<!--more-->

"""


def set_color(color):
    if sys.platform == 'linux':
        pass
    else:
        handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)


def print_error():
    print('[', end='')
    set_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
    print('错误', end='')
    set_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
    print(']', end='')


def print_ok():
    print('[', end='')
    set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    print('成功', end='')
    set_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
    print(']', end='')


def get_categories():
    if not os.path.isdir(POST_PATH):
        raise BlogException('博客路径不正确: %s !' % POST_PATH)

    categories = os.listdir(POST_PATH)
    if not len(categories):
        raise BlogException('没有检测到任何分类 !')

    return categories


def get_category(categories):
    while True:
        display_categories = ', '.join('({}){}'.format(i+1, v) for i, v in enumerate(categories))
        category = input('检测到博客的分类有：{} ! \n请从上面选择一种分类 > '.format(display_categories))

        exit(category)

        if category.isdigit() and int(category) in range(1, len(categories)+1):
            category = categories[int(category)-1]                

        try:
            ind = categories.index(category)
        except ValueError:
            print_error()
            print('输入的分类 %s 不存在 !' % category)
            continue
        else:
            print_ok()
            print('选择分类 %s 成功 !' % categories[ind])
            return categories[ind]


def get_action():
    actions = {'add': add_blog, 'edit': edit_blog}
    while True:
        action = input('支持的操作有%s，请从中选择一项操作 > ' % ', '.join(actions.keys())).strip()
        exit(action)

        if action == 'a':
            print_ok()
            print('选择操作 add 成功 !')
            return actions['add']
        elif action == 'e':
            print_ok()
            print('选择操作 edit 成功 !')
            return actions['edit']
        elif action not in actions:
            print_error()
            print('不支持所输入的操作: %s !' % action)
            continue
        else:
            print_ok()
            print('选择操作 %s 成功 !' % action)
            return actions[action]


def add_blog(category):
    category_path = os.path.join(POST_PATH, category)

    while True:
        filename = input('请输入新增博客的文件名 > ').strip()
        if TITLE_PATTERN.match(filename):
            for name in os.listdir(category_path):
                if re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}-%s\.markdown$' % filename, name):
                    print_error()
                    print('输入的文件名已存在: %s !' % name)
                    break
            else:
                break
        else:
            print_error()
            print('输入的文件名不满足格式: ^([a-zA-Z0-9]+-)*[a-zA-Z0-9]+$')
            continue

    cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    cur_date = cur_time.split()[0]
    title = filename
    blog_path = os.path.join(category_path, '%s-%s.markdown' % (cur_date, filename))

    with open(blog_path, 'w') as wf:
        wf.write(CONTENT % (title, cur_time, category))

    os.chdir(category_path)
    popen('git add %s' % blog_path)
    open_blog(blog_path)


def edit_blog(category):
    counter = 0
    results = OrderedDict()

    for name in os.listdir(os.path.join(POST_PATH, category)):
        path = os.path.join(POST_PATH, category, name)
        with open(path, 'rb') as rf:
            for line in rf:
                if line.strip().startswith(b'title'):
                    counter += 1
                    title = line.split(b':')[-1].strip()
                    results[str(counter)] = (title, path)
                    break
            else:
                print_error()
                print('该文件没有找到title: %s !' % path)

    tip = '\n'.join('%s. %s' % (no, tup[0].decode()) for no, tup in results.items())
    while True:
        print(tip)
        idx = input('请输入要编辑博客的编号 > ').strip()
        if not idx.isdigit() or idx not in results:
            print_error()
            print('输入的编号有误: %s !' % idx)
        else:
            blog_path = results[idx][-1]
            break

    open_blog(blog_path)


def open_blog(path):
    if not os.path.exists(EXE_PATH):
        print_error()
        print('没有找到该程序 %s !' % EXE_PATH)
    else:
        print_ok()
        print('博客打开成功 !!!')
        popen('%s %s' % (EXE_PATH, path))
    sys.exit()


def start():
    try:
        categories = get_categories()
    except BlogException as e:
        print_error()
        print(str(e))
        time.sleep(3)
        return

    category = get_category(categories)
    action = get_action()
    action(category)


def exit(value):
    if value == 'q' or value.startswith('quit') or value.startswith('exit'):
        sys.exit()


class BlogException(Exception):
    pass


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        print()
        print_ok()
        print('程序退出...')
        time.sleep(3)
