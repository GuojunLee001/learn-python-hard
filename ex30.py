# coding:utf-8

people = 30
cars = 40
trucks = 15

# 第一种情况输出
if cars > people:
    print "We should take the cars."
elif cars < people:                                  # 第二种情况输出
    print "We should not take take the cars."
else:                                                # 第三种情况输出
    print "We can't decide."

# 第一种情况输出 
if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:                                  # 第二种情况输出
    print "Maybe we could take the trucks."
else:                                                # 第三种情况输出
    print "We still can't decide."
	
# 表示只有两种情况的输出
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
	
# 附加题
# 1. elif 表示3个及3个以上分支时使用。

# 复杂的布尔表达式
if people > cars and people > trucks:
    print "First."
elif people < cars and people < trucks:
    print "Second"
elif people > cars and people < trucks:
    print "Third."
elif people < cars and people > trucks:
    print "Fouth."