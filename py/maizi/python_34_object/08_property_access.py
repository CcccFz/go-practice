# -*- coding:utf-8 -*-

"""
属性访问：
__getattrbute__(self, item)
    只要属性访问，都要调用，哪怕是不存在的属性
    不能用return self.__dict__[item]会陷入死循环
    return object.__getattribute__(self, name)

__getattr__(self. item)
    不存在属性时，调用，相当于错误处理
    return 'default'
    return self.__dict__[item]

__setattr__(self, item, value)
    为属性赋值时调用
    self.__dict__[item] = value

"""


class Person(object):
    def __init__(self):
        pass

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        if item == 'after':
            return self.__dict__['salary'] * 0.8
        return 0

    def __setattr__(self, item, value):
        if item == 'salary':
            self.__dict__[item] = value * 2
        else:
            self.__dict__[item] = value

if __name__ == '__main__':
    p = Person()
    p.salary = 1000
    p.aa = 1
    print p.salary
    print p.after
    print p.beagin
    print p.aa
