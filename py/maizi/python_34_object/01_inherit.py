class A:
    def __init__(self, a):
        print('A init')

    def run(self):
        print('A run')

class B:
    def run(self):
        print('B run')

class C(A):
    def __init__(self):
        super().__init__(a=0)
        print('C init')        

class D(A, B):
    pass

print(A.__base__)
print(C.__bases__)
print(D.__bases__)

# 继承调用原则：先在子类中找属性和方法；没找到去父类挨个找；
#               若子类找到属性\方法\构造，就只调用子类的，不会调用父类的（所以不会像c++每次都调用父、子的构造方法）
#               若实在需调用父类，可以以super().方法调用
C()
D().run()   # 先继承的，先调用；这里调用A的run方法
