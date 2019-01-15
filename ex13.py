# _*_ coding: utf-8 _*_

# 把 argv 中的东西解包，将所有的参数依次赋予左边的变量名”。接下来就是正常的打印了
from sys import argv
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# 加分题
# 如果是3个以下信息，则会报错：ValueError:need more than 3 values to unpack。原因是包中有三个变量，但是定义少了，无法解开。

# 与raw_input 结合使用
from sys import argv
script, first, second, third = argv

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
  age, height, weight)
  
print "The script is called:", script
print "Your first variable is: , % ", (first, age)
print "Your second variable is: , % ", (second, height)
print "Your third variable is: , % ", (third,weight)

# 更多参数
from sys import argv
script, first, second, third, fouth, fifth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fouth variable is:", fouth
print "Your fifth variable is:", fifth

# 更少参数
from sys import argv
script, Z, D = argv

print "The script is called:", script
print "Your Z variable is:", Z
print "Your D variable is:", D
