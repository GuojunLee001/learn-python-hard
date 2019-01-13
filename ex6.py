# _*_ coding: utf-8 _*_

# 定义变量，此处字符串包含字符串
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "There who know %s and those who %s." % (binary, do_not)

# xy为什么不加“” --> 变量不用加”“ ，否则会识别为文本字符。此处输出为变量定义后的值
print x
print y 

# 此处字符串包含字符串
print "I said: %r." % x
print "I also said: ‘%s.’" % y

# 定义变量，第二行的%r 实际上代指了第一行的，优先用repr()函数进行字符串转换
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# 字符串加起来还是字符串
w = "This is the left side of..."
e = "a string with a right side."

print w + e 