#!/usr/bin/env python
#coding:utf-8

# 多态和封装
'''
the code is from: http://zetcode.com/lang/python/opp/
'''

__mataclass__ = type

class Animal:
    def __init__(self, name = ""):
        self.name = name
    def talk(self):
        pass
        
class Cat(Animal):
    def talk(self):
        print "Meow."
        
class Dog(Animal):
    def talk(self):
        print "Woof."
        
a = Animal()
a.talk

c = Cat("Missy")
c.talk()

d = Dog("Rocky")
d.talk()

# 获得属性顺序
class A(object):
    author = 'qwsir'
    def __getattr__(self, name):
        if name != 'author':
            return "from starter to master"
            
if __name__ == "__main__":
    a = A()
    print a.autor
    print a.lang
    
# 生成器
def fibs(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    
if __name__ == "__main__":
    f = fibs(10)
    for i in f:
        print i,