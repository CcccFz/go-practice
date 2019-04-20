# -*- coding:utf-8 -*-

"""
待续。。。

深入理解类  类也是一个对象，但有创建其自身实例的能力
           类可以和一个变量绑定，可以为类增加属性，类可以作为函数参数

元类(type)  类的创建者和管理者，所有类都是元类的实例
            python3.4元类才是type

类实例化过程  __new()__
            __init()__
            python3.4

自定义元类  继承type，定义__new()__方法，还可以定义__init()__方法

"""


class Empty:
    def __init__(self):
        pass


class Custom:   # py3.4
    def __init__(self):
        print('Init method')

    def __new__(cls, *args, **kwargs):
        print('New Instance')
        return object.__new__(cls, *args, **kwargs)


class MyMeta(type):
    def __init__(self, name, bases, dicts):
        print('Init Instance')

    def __new__(cls, name, bases, dicts):
        # dicts['info'] = lambda self:print('Djx.')
        res = type.__new__(cls, name, bases, dicts)
        res.company = 'MaiZi'
        return res


class NewClass(metaclass=MyMeta):
    pass

def get_class_instance(moc):
    print(moc)
    print(moc())

if __name__ == '__main__':
    ept = Empty
    print(ept())

    ept.foo = 0
    print(ept().foo)

    get_class_instance(ept)

    print(type(Empty))   # py3.4 查看类的类型
    # Hello = type('Hello', (object,), dict=(hello=lambda self:print('Hello!')))    # 创建类
    print(isinstance(Empty, type))   # py3.4 类是否是type的实例

    Custom()    # py3.4 类实例化步骤

    cus = NewClass()
    cus.info()
    print(cus.company)