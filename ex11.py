# _*_ coding: utf-8 _*_

print "How old are you?",
age = raw_input()
print "How tall are you?", # 加个，目的是为了程序运行时不跑到下一行
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heany." % (
  age, height, weight)
  
# 加分题
# 1. raw_input 实现的功能：raw_input() 将所有输入作为字符串看待，返回字符串类型。
# 2. \' 转义，防止被识别为字符串。

# row_inpt 用法举例
name = raw_input("What's your name?")
age = raw_input("How old are you?")

print "Your name is:",name
print "You are " + age + " years old."

# int 类型转化才能够求和，原因是raw_input 输出的是文本型字符串
after_ten = int(age) + 10 
print "You will be" + str(after_ten) + "years old after years."
