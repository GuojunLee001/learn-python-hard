 #coding:utf-8

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# 扫描定义的变量
stuff = ten_things.split(' ')
# 定义一个新的列表变量
more_stuff = ["Day“， ”Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# 判断长度
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Addind: ", next_one
    stuff.append(next_one)
    print "There are %d items now." %len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

# 提取
print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar

# 加分题
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# 扫描定义的变量
stuff = split(ten_things, ' ')
# 定义一个新的列表变量
more_stuff = ["Day“， ”Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# 判断长度
while len(stuff) != 10:
    next_one = pop(more_stuff)
    print "Addind: ", next_one
    append(stuff, next_one)
    print "There are %d items now." %len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

# 提取
print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar

# 面向对象的三大特点（封装，继承，多态）缺一不可。

# 列表使用
list = [1, 2, 3, 4, 55, 6, 7, 8, 10]

# 取值
list[-1]

# 查找元素出现次数
list.count(1)

# 查看重复原色
list.index(1)

# 增加元素
list.append(19)

# 指定位置添加元素
list.insert('L')

# 删除
del list[6]

# pop
list.pop(2)
num.pop(3)

# 删除指定元素
list.remove(3)

# reserse() 翻转
list.reserse()

# 切片
list[:3]
list[1:5:2] # 步长为2
list[::2]
