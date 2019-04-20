# 属性访问的特殊方法 反射： 提供字符串来操作类的属性/方法的方式
# 主要工具函数;   hasattr(obj, '属性名') setattr(obj, '属性名', '值')  getattr(obj, '属性名'), 一般写框架时用

class Test:
    a = 0
    def __init__(self):
        self.a = 10
        self.b = 20

if __name__ == '__main__':
    t = Test()
    # 类属性与实例属性同名  以实例名.属性优先引用实例属性；以类名.属性只引用类属性
    print(t.a)
    print(Test.a)
    print(t.b)
    # print(Test.b) 错误  没有这个类属性

    print('  ', getattr(t, 'a'), setattr(t, 'a', 100), getattr(t, 'a'), hasattr(t, 'b'))