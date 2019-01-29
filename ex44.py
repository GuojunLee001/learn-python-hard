#coding:utf-8

# 子类的方法隐性继承父类方法
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"
        
# 继承与父系一致，用pass代替
class Child(Parent):
    pass
    
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# 子类重写父类
class Parent(object):

    def override(self):
        print "PARENT override()"
        
# 子类直接重写
class Child(Parent):

    def override(self):
        print "CHTLD override()"
        
dad = Parent()
son = Child()

dad.override()
son.override()

# 对子类的操作改变父类
class Parent(object):
    
    def altered(self):
        print "PARENT altered()"
        
class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
    
dad = Parent()
son = Child()

dad.altered()
son.altered()

# 完整代码
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"
        
    def override(self):
        print "PARENT override()"
        
    def altered(self):
        print "PARENT altered()"
        
class Child(Parent):
    def override(self):
        print "CHTLD override()"
    
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
