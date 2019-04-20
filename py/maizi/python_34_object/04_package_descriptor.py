# -*- coding:utf-8 -*-

"""
属性包装  将方法包装成属性，以隐藏相关实现同时增添功能属性；控制属性的类型或范围的一种虚拟属性（有其他真实属性处理得到）
三种属性操作   可读：@property
              可写：@<property-name>.setter
              可删：@<property-name>.deleter

描述符
将实现特殊协议方法的类作为另外一个类的类属性，用来拦截和控制属性访问并可以重复使用,
当访问属性时，需要对属性做进一步处理时，用描述符；@property、@classmethod、@staticmethod是基于描述符实现的
只有类属性才能作为描述符，type(obj).__dict__[x].__get__()
数据描述符 > 实例属性 > 非数据描述符 (会被覆盖)

协议方法   __get()__、__set()__、__delete()__
分类  数据描述符（实现全部协议方法）、非数据描述符（实现部分协议方法）  所有成员函数都是非数据描述符
同名实例属性和非数据描述符（以方法为例）访问优先级  注意：py2.7中，描述符只能在老式类中中使用

__call__()  当类实现了__call()__方法后，该类实例可以被直接当作函数调用，即调用__call__()方法
"""


class Student:
    def __init__(self, year):
        self.date = 2016
        self.__start = year

    def __call__(self, *args, **kwargs):
        print 'call', args, kwargs

    @property
    def work_year(self):
        return self.date - self.__start

    @work_year.setter
    def work_year(self, years):
        if 0 < years < 5:
            self.work_year = years
        else:
            print('set Failure!')


class NonNeg(object):
    def __init__(self, default=0):
        self.default = default

    def __get__(self, instance, owner):
        return self.default

    def __set__(self, instance, value):
        if value > 0:
            self.default = value
        else:
            print 'The value must be NonNegative!'

    def __delete__(self, instance):
        pass


class Movie(object):
    score = NonNeg()

    def __init__(self):
        pass

    def func(self):
        pass

if __name__ == '__main__':
    stu = Student(2013)
    print(stu.work_year)
    stu.work_year = 2
    print(stu.work_year)

    m = Movie()
    print 'score %s' % m.score
    print dir(m.score)
    print dir(m.func())

    stu()
