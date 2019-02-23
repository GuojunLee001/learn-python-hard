#!/usr/bin/env python
#coding:utf-8

# 参数收集，解决参数个数的不确定性问题,*表示多个参数，？表示一个参数
def func(x, *arg):
    print x
    result = x
    print arg
    for i in arg:
        result += i
    return result
print func(1, 2, 3, 4, 5, 6, 7, 8, 9)

# 收集字典的数据
def foo(**kargs):
    print kargs

foo(a = 1, b = 2, c = 3, d = 4)

# 综合练习
def foo(x, y ,z ,*arg, **kargs):
    print x
    print y
    print z
    print arg
    print kargs

foo(1, 2, 3)
foo(1, 2, 3, 4, 5)
foo(1, 2, 3, 4, 5, a = 'lgsir')
