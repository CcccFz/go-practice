# -*- coding:utf-8 -*-

"""
构造序列类必须实现以下方法：
__len__(self)
__getitem__(self, key)
__setitem__(self, key, value)
__delitem__(self, key)


构造iter实现迭代器：
__iter__(self)
next(self)   py3.4 此方法为__next__(self)

构造可比较类： __it__(),__le__(),__gt()__,__ge__(),__eq()__,__ne__()
"""


class MySeq:
    def __init__(self):
        self.lseq = ['I', 'II', 'III', 'IV']

    def __len__(self):
        return len(self.lseq)

    def __getitem__(self, item):
        if 0 <= item < 4:
            return self.lseq[item]


class MyIter:
    def __init__(self, start, end):
        self.count = start
        self.end = end

    def __iter__(self):
        return self

    def next(self):
        if self.count < self.end:
            r = self.count
            self.count += 1
            return r
        else:
            raise StopIteration


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, oth):
        return self.x < oth.x

    def __gt__(self, oth):
        return self.y > oth.y

    def __add__(self, oth):
        return Point(self.x + oth.x, self.y + oth.y)

    def info(self):
        print(self.x, self.y)

if __name__ == '__main__':
    m = MySeq()
    for i in range(4):
        print m[i]

    for j in MyIter(1, 10):
        print j

    pa = Point(0, 1)
    pb = Point(1, 0)
    print(pa < pb)
    print(pa > pb)

    pc = pa + pb
    pc.info()