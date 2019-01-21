#coding:utf-8

i = 0
numbers = []
# 当小于6时执行字典输出
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1   # 赋值
    print "Numbers now:", numbers
    print "At the bottom i is %d" % i 

print "The numbers:"

for num in numbers:
    print num 
	
# 附加题
i = 0
numbers = []
# i改成函数
while i < 100:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 5.33333   # 赋值
    print "Numbers now:", numbers
    print "At the bottom i is %d" % i 
	
else:
    print "The numbers:"

for num in numbers:
    print num 
	