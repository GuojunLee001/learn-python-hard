# _*_ coding: utf-8 _*_

# 定义cheese_and_crackers 函数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count  # 定义需要打印的内容
	print "You have %d boxes of crackers!" % boxes_of_crackers # 定义需要打印的内容
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# 第一种输出：直接打印数字
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# 第二种输出：函数变量单独赋值
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 第三种输出：相加
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# 第四种输出：数字和变量相加
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

# 第五种输出：相加的相加
print "And there is another:"
amount_of_cheese = A + 10
amount_of_crackers = B + 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 第六种输出：变量的变量，运行错误！
print "How about this:"
def A_a(B1, C2)
    print "T Have %r." % B1
	print "You have %r!" % C2

def D_d(B3, C4)
    print "T Have %r." % B3
	print "You have %r!" % C4

A_a(10, 20)
D_d(89, 50)

amount_of_cheese = A
amount_of_crackers = D
cheese_and_crackers(amount_of_cheese, amount_of_crackers)