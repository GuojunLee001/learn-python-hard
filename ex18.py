# _*_ coding: utf-8 _*_

# this one is like your scripts with argv
# 使用参数解包的方式创建函数
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we just do this
def print_two_again(arg1, arg2):  # 直接()中使用函数,有几个变量
	print "arg1: %r, arg2: %r" % (arg1, arg2) # 变量输出结果是什么
	
# this just takes one argument
def print_one(arg1): # 与第二种类似，但只有一个变量
	print "arg1: %r" % arg1

# this one takes no argument
def print_none():
	print "I got nothin'."
	
# 赋予变量名称，输出，此处可以写在最后，也可以放在每个函数后面
print_two("Zed", "Shaw") 
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# 加分题，复习见 http://www.runoob.com/python/python-functions.html
# 1. 定义函数必须以def开头
# 2. 函数名称不一定都要以字符下划线组成,必须紧跟(): ，后面使用四个空格缩进，函数结束后取消缩进
# 3. 括号里包含参数，多个参数用括号隔开
# 4。总结函数基本形式 :
# def xx(参数):
#    print ""
# xx(定义参数）


