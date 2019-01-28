#coding:utf-8

## Animal is-a object(yes, sort of confusing) look at the extra credit
# 定义一个类的基本结构
class Animal(object):
    pass
	
## Dog is-a object
# 创建一个实例基本结构
class Dog(Animal):

    def __init__(self, name):   # 强制绑定属性，第一个参数永远是self
        ## has-a
		self.name = name
		
## Cat is-a object
# 创建第二个实例
class Cat(Animal):

    def __init__(self, name):
        ## has-a
		self.name = name
		
## Person is-a object
# 创建类
class Person(object):

    def __init__(self, name):
        ## has-a
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None

## Employee is-a a object
# 创建实例
class Employee(Person):
    def __init__(self, name, salary):
    ## is-a hmm what is this strange magic?
	super(Employee, self).__init__(name)
	## has-a
	self.salary = salary
	
## Fish is-a object
class Fish(object):
    pass
	
## Sammon is-a object
class Salmon(Fish):
    pass
	
## Fish has-a Halibut
class Halibut(Fish):
    pass
	
## rover ia-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary.pet has-a satan
mary.pet = satan

## frank haa-a Employee
frank = Employee("Frank", 120000)

## Fish has-a flipper
flipper = Fish()

## Salmon has-a crouse
crouse = Salmon()

## Halibut has-a harry
harry = Halibut()

# 附加题
"""
类的基本结构：class A...(object)
object 的作用是oop中的继承
如果子类重写了父类的方法，就使用子类的该方法，父类的被遮盖。
"""
