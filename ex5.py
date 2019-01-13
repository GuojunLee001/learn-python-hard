# _*_ coding: utf-8 _*_

my_name = 'Zed A. Shaw'
my_age	= 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
  my_age, my_height, my_weight, my_age + my_height + my_weight)
  
# 附加题 去掉my后输出结果仍然一样
name = 'Zed A. Shaw'
age	= 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
  age, height, weight, age + height + weight)
  
# python 格式化字符串大全
# %% 百分号标记 #就是输出一个%
# %r 优先用repr()函数进行字符串转换
# %c 字符及其ASCII码
# %s 字符串
# %d 有符号整数(十进制)
# %u 无符号整数(十进制)
# %o 无符号整数(八进制)
# %x 无符号整数(十六进制)
# %X 无符号整数(十六进制大写字符)
# %e 浮点数字(科学计数法)
# %E 浮点数字(科学计数法，用E代替e)
# %f 浮点数字(用小数点符号)
# %g 浮点数字(根据值的大小采用%e或%f)
# %G 浮点数字(类似于%g)
# %p 指针(用十六进制打印值的内存地址)
# %n 存储输出字符的数量放进参数列表的下一个变量中