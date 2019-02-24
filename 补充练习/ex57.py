#！\usr/bin/env python
#coding:utf-8

class Person(object):
    
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
        
    def color(self, color):
        d = {}
        d[self.name] = color
        return d

if __name__ == "__main__":
    girl = Person("John")
    print girl.name
    name = girl.get_name()
    print name
    her_color = girl.color("white")
    print her_color

# 第二个练习
class Person:
     def __init__(self, name, lang = "golang", website = "qing.qqw.com"):
         self.name = name
         self.lang = lang
         self.website = website
         self.email = "qiye@qq.com"

# 第三个练习
class Foo(object):
    def __init__(self, name):
        self.name = name

    def check_t():
              T = 1
              return T

    def get_name(self):
              if self.check_t():
                        return self.name
              else:
                        return "no person"

if __name__ == "__main__":
          f = Foo("John")
          name = f.get_name()
          print name 
