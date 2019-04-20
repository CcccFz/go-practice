# 实例属性： 类被实例化后才会有实例属性，一般构造方法中创建和初始化。类内引用self.a;类外引用obj.a
#            可以在类外/内修改或添加实例属性，如obj.b=10，但是一般不这样用，最好通过类方法来改变。
# 类属性： 类定义后就存在，不需要实例化，相同类的不同对象共用类属性。即任意对象修改，其它对象里也变了。
# 私有属性: 使用__开头标识私有(强制),使用_开头标识保护(非强制)
# 特殊属性： __doc__ __name__ __dict__ __module__ __bases__
class Test:
    css = 'Hello'
    def __init__(self):
        self.a = 0
        self.b = 10

    def info(self):
        print('a:', self.a, 'b:', self.b, 'css:', Test.css)

if __name__ == '__main__':
    t1 = Test()
    t2 = Test()
    t1.a, t1.b, t1.css = 10, 20, '0'  # 同Test.css = '0'
    t1.info()
    t2.info()

    print( dir(Test) ) # 看类的特殊属性
    #字典做输入格式
    str = "doc: %(doc)s\nname: %(name)s\ndict: %(dict)s\nmodule: %(module)s\nbases: %(bases)s"
    templet = {
        'doc': Test.__doc__,
        'name': Test.__name__,
        'dict': Test.__dict__,
        'module': Test.__module__,
        'bases': Test.__bases__
    }

    print(str % templet)