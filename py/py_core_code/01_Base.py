# -*- coding:utf-8 -*-

# PEP8 python开发增强提案

# 正则表达式
import re
pattern = re.compile(r'^\.1(\.\d+)+$')
print pattern.match('.1.1.1.1')

# 打印
print 'My name is %s, age is %d' % ('liuxiaofan', 24)

# 输入,输入永远是字符串
# user = raw_input('Input your name:')
# print 'your name is ', user

# 输出重定向到标准错误输出和文件
import sys
print >> sys.stderr, 'Fatal error, invalid input'

logfile = open('log.txt', 'a')
print >> logfile, 'Fatal error, invalid input'
logfile.close()

# 字符串切片
str = 'Hello'
print str[1:-1]

# 字典
dic = {'a': 1, 'b': 2}
print dic.keys()
for key in dic:
    print key, dic[key]

# range
for i in range(len(str)):
    print str[i], i

# enumerate
for i in enumerate(str):
    print i
for i, v in enumerate(str):
    print i, v

# 列表解析
print [x ** 2 for x in range(8) if not x % 2]

# 文件
file = open('git.txt', 'r')
for eachline in file:
    print eachline,
file.close()


# class 类名
class A:
    """
    class A
    """
    def __init__(self):
        print self.__class__
        print self.__class__.__name__
obj = A()
print dir(obj)
print help(obj)
print obj.__doc__

import sys
print sys.version
print sys.platform
# print sys.stdout.write('Hello\n')

# 可变/不可变对象
def func(n):
    n += n
a = 2
b = [2]
func(a)
func(b)
print a, b

# 多元赋值(两边都是元组)
x, y, z = 1, 2, 3

# 对象三特性：身份，类型，值
print id(42)
print id(42)  #同一对象
print type(42)
print type(type(42))  # 元类
42 is 42    # 对象身份比较
42 == 42    # 对象值比较

# 切片实现逆序
print('abcde'[::-1])
print('abcde'[::-2])

# isinstance
num = 4.4
if isinstance(num, (int, long, float, complex)):
    print num, True,
import types
print num, ' is ',
if type(num) is types.IntType:
    print 'Integer'
elif type(num) is types.LongType:
    print 'Long'
elif type(num) is types.FloatType:
    print 'Float'
elif type(num) is types.ComplexType:
    print 'Complex'

# //地板除
print 1.0 / 2
print 1.0 // 2

# round 小数近似值
# int 去除小数部分
# floor 得到最接近且小于原数的整数
print round(1.2345)
print round(1.2345, 2)

# 十六、八进制
print hex(255)
print oct(255)
print 010
print 0x10

# 转ASCII只
print chr(97)
print ord('A')

# random
import random
print random.random()   # 0到1之间的随机小数
print random.randint(1, 10)     #之间的任意整数
print random.randrange(1, 10, 5)     #之间取步长的任意整数
print random.uniform(1, 10)     #之间任意浮点数
print random.choice(['a', 'b', 'c'])    #序列中任意元素

# 连接序列
str = 'abcd'
list = [1, 2, 3, 4]
str.join('e')
list.extend([5])
print str
print list

# 切片
s = 'abcde'
for i in [None] + range(-1, -len(s), -1): # s[:None] = s[:]
    print s[:i]
print range(1, 5)
print range(5, 1, -1)   # 从大到小，必须要逆序-1
print range(-1, -5, -1)
print range(-5, -1)
print s[:], s[None:], s[:None]

list = [None]
list.extend(range(-1, -len(s), -1))  # extend没有返回值
for i in list:
    print s[:i]

# 序列类型转换工厂函数
# list(iter) 把可迭代对象转换为列表
# str(obj) 把 obj 对象转换成字符串(对象的字符串表示法)
# unicode(obj) 把对象转换成 Unicode 字符串(使用默认编码)
# basestring() 抽象工厂函数,其作用仅仅是为 str 和 unicode 函数提供父类，所以不能被实例化，也不能被调用(详见第 6.2 节)
# tuple(iter) 把一个可迭代对象转换成一个元组对象
print zip(s, reversed(s), s)

# 成员操作符
str = 'abcdefghijklmnopqrstuvwxyz'
print 'afz' in str
print str.find('afz')
print str.find('cde')   # 可以跟下标区间，指定查找范围
print str.index('cde')  # 找不到不返回-1，而是抛异常
# rindex和rfind是从最后开始找

import string
print string.ascii_uppercase
print string.ascii_lowercase
print string.ascii_letters
print string.digits

# 四种连接字符串
print 'abc' + 'cde'  # 最笨
print '%s%s' % ('abc', 'bcd') # 格式化字符串，一种十元组，一种是字典
print ('abc'
     'bcd')  # 可在其中加注释
print ''.join(['abc', 'bcd'])

print 'dec:%d oct:%#o hex:%#X' % (num, num, num)
print "MM/DD/YY = %02d/%02d/%03d" % (2, 15, 67)

# 字符串模版
from string import Template  # 字符串模版，解决格式化字符串必须带参数类型
s = Template('There are ${howmany} ${lang} Quotation Symbols')
print s.substitute(lang='Python', howmany=3)
# print s.substitute(lang='Python') 缺少参数报错
print s.safe_substitute(lang='Python')

print isinstance(u'\0xAB', type(str))
print not isinstance('foo', unicode)
print isinstance(u'', basestring)

quest = 'what is your favorite color?'
print ''.join(['ab ', quest])
print ' a '.join(quest.split())


# 序列的浅拷贝和深拷贝，适用于具有对象和含有可变类型的序列
hubby = ['liu', ['savings', 100]]
wifey = hubby[:]
wifey[0] = 'zhao'
wifey[1][1] = 50  # hubby和wifey都会变为50
print '浅拷贝'
for person in hubby, wifey:
    print id(person),
    for ele in person:
        print id(ele),
    print ''

import copy
wifey = copy.deepcopy(hubby)
wifey[0] = 'zhao'
wifey[1][1] = 50  # 只有wifey会变为50
print '深拷贝'
for person in hubby, wifey:
    print id(person),
    for ele in person:
        print id(ele),
    print ''

# 第一,非容器类型(比如数字,字符串和其他"原子"类型的对象,像代码,类型和 xrange 对象等)没有被拷贝一说
# 第二，如果元组变量只包含原子类型对象,对它的深拷贝将不会进行，因为元组元素不可变
# 浅拷贝的方式：1)完全切片操作[:]；2)利用工厂函数,比如 list(),dic()等；(3)使用copy模块的copy函数

# 字典的创建
dic = dict((['x', 1], ['y', 2])) # --> dict(zip(['x', 'y'], [1, 2]))
print dic
dic = {}.fromkeys(('a', 'b', 'c'))
print dic
dic = {}.fromkeys(('a', 'b', 'c'), -1)
print dic
dic = dict(x=1, y=2)
print dic
dic1 = dict(**dic)
print dic1
dic1 = dic.copy()
print dic1
# 字典比较规则 长度、key、值

# 可哈希
# hash([])
# hash({})
hash(())

dic1 = {'host': 'earth', 'port': 80}
dic2 = {'host': 'venus', 'server': 'http'}
dic1.update(dic2)
print dic1

# 安全方法
# 没有的话，返回给与的值
print dic2.get('xxx')
print dic2.get('xxx', 'acd')
print dic2

# 没有的话，添加条目
print dic2.setdefault('host', 'baidu')
print dic2.setdefault('xxx', 3)
print dic2

# 空行\r\n空格
a = ' as d '
print a.strip()
a = '\r asd ss\n\r '
print a.strip()

# if 0 == a.strip(): 常用于判断是否是空行
a = 'asdwweeddasd'
print a.strip('asd')

# 装饰器原型
def des(func):
    def two():
        print 'two'
        func()
    return two

def one():
    print 'one'

after_one = des(one)
after_one()

# 装饰器
def des(func):
    def two():
        print 'two1'
        func()
    return two

@des
def one():
    print 'one1'

one()

# 带参数装饰器
def des(a):
    def old_des(func):
        def two():
            print 'two2'
            func()
        return two
    return old_des

@des(a=1)
def one():
    print 'one2'

one()
print one.__name__

# 装饰器名字伪装
import functools
def des(a):
    def old_des(func):
        @functools.wraps(func)
        def two():
            print 'two3'
            func()
        return two
    return old_des

@des(a=1)
def one():
    print 'one3'

one()
print one.__name__

# 任意参数装饰器
def des(func):
    def two(*args, **kwargs):
        print 'ha ha'
        func(*args, **kwargs)
    return two

@des
def one(a, b):
    print a, b

one(1, 2)

# 自定义能够用于with语句的类
class UserFile():
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        return self

    def write(self, text):
        print text

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print exc_type
            print exc_val
            print exc_tb
        return True

with UserFile('a.txt', 'w') as f:
    f.write('Ha UserFile')
    int('H')