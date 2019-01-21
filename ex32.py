# coding:utf-8

# 定义三个列表
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 'quarters']

# 依次打印
# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number
	
# 依次打印
# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# 混合打印
# also we can go through mixed lists too
# notice we have to use %r since we don't know whot's in it
for i in change:
    print "I got %r" % i

# 定义了一个空的列表，用于下面
# we can also build lists, first start with an empty one
elements = []

# the use the range function to do 0 to 5 count
for i in range(0,6):
    print "Anding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i 

# 附加题
"""
1. for 循环基本结构
for 循环规则：
    操作语句
2. 为什么每次打印都要换行：代表循环操作，一个一个的找到并且打印出来。
3. range()
- 为内建函数，最常用于for循环
- 一般形式为range(start, stop[,step])
- 函数参数必须是整数

4. 对list的操作
- len()
- +
- * 重复元素
- in 
- max(),min()
- cmp()
"""
