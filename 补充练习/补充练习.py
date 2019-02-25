# coding:utf -8
# 嵌套循环
print "\tDog \tBun \tKetchup \tMustard \tOnions"
count = 1

for dog in [0,1]:
    for bun in [0,1]:
        for ketchup in [0,1]:
            for mustard in [0,1]:
                for onion in [0,1]:
                     print "#", count, "\t",
                     print dog, "\t", bun, "\t", ketchup, "\t",
                     print mustard, "\t", onion
                     count = count + 1


import time
line = 1
for i in range (10, 0, -1):
    for line in range(1,5):
        print i
        print "*"
        time.sleep(0.01)
        line = line + 1
print "BLAST OFF!"
        
# 列表使用
list = [1, 2, 3, 4, 5, 6]

# 末尾增加元素
list.append(12)
print list

# 末尾增加多个元素
list.extend([45, 67, 'a'])
print list

# 指定位置增加元素
list.insert(4, 'd')
print list

# 元素位置
print list.index(4)

for last in list:
    print last