# _*_ coding: utf-8 _*_

# 使用argv设置一个参数
from sys import argv
script, filename = argv
# 定义变量通过open打开
txt = open(filename)
# 参数的名称
print "Here's your file %r:" % filename
# 打开文件
print txt.read()

# 输入的内容必须是文件的名称
print "Tipe the filename again:"
# raw_input为用户输入
file_again = raw_input("> ")

# 定义变量通过open打开
txt_again = open(file_again)

print txt_again.read()

# 加分题
# function 和method 区别：https://blog.csdn.net/chili_min/article/details/10447923

# 删除15-21行，运行错误，因为没有open函数
from sys import argv
script, filename = argv
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
print "Tipe the filename again:"

# 只用raw_input 写脚本，相当于文件没有被写死，操作者可以按照自己的需求打印任何内容
