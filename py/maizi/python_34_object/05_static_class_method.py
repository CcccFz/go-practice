# -*- coding:utf-8 -*-

"""
静态方法  @staticmethod装饰  参数不需要self
         不能引用或访问实例属性，可以访问类属性
         用类或类实例调用
         本质  在类中一个普通函数而已，使面相对象中的函数归属于类，易于代码管理
         用途  与类相关但不依赖或改变类与实例，创建不同实例，把类相关工具方法放入类中

类方法  @classmethod装饰  必须代cls参数
       同样不能引用或访问实例属性
       同样可以用类或类实例调用
       继承时，传入的cls是子类而非父类
       用途  与类相关但不依赖或改变类实例
            工厂方法，创建类实例，完成有关预处理
            在内类调用静态方法时不用硬编码类名
"""


class Person:
    company = 'Huawei'
    base_money = 500

    def __init__(self, money=1000):
        self.salary = money

    @staticmethod
    def get_trial_salary(money):
        # print self.salary #静态方法不能引用实例属性
        print Person.company
        return money * 0.8

    @classmethod
    def get_company_salary(cls):
        print cls.company, ' ', cls.get_trial_salary(cls.base_money)

if __name__ == '__main__':
    print Person.get_trial_salary(Person().salary)
    print Person(2000).get_trial_salary(Person(2000).salary)
    print Person.get_company_salary()