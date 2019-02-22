#! /usr/bin/env python
#coding:utf-8

# zip使用 简化for循环的某些功能
a = 'john li'

print zip(a)

# 对比
for i in range(1,10):
    print i * i
    
power2 = []
for i in range(1,10):
    power2.append(i * i)

print power2

print "************************************"

# while
i = 0
while i < 2:
    raw_input( ">>>  your name ：")
    i += 1
else:
    pass

print "*************************************"

# for else
# 导入模块
from math import sqrt

for n in range(99, 1, -1): 
    root = sqrt(n) # 99到2之间开方
    if root == int(root):
        print n
        break
else:
    print "Nothing."

print "*************************************"

# 函数
def times(x, y):
    print "x = ", x
    print "y = ", y
    print "x + y = ", x + y
    print "x - y = ", x - y
    print "x * y = ", x * y
    print "x / y = ", x / y
    print "x // y = ", x // y
    print round(x, y)

times(334, 92)

print "**************************************"

# 函数2
def fibs(n):
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

if __name__ == "__main__":
    lst = fibs(10)
    print lst

print "****************************************"


