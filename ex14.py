# _*_ coding: utf-8 _*_

# 调用包,只有一个参数
from sys import argv
script, user_name = argv
# 将用户提示符设置为变量 prompt，这样就不需要在每次用到 raw_input 时重复输入提示字符
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# 加分题1 修改prompt值
from sys import argv
script, user_name = argv
answer = '--> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(answer)

print "Where do you live %s?" % user_name
lives = raw_input(answer)

print "What kind of computer do you have?"
computer = raw_input(answer)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# 加分题2 增加参数
from sys import argv
script, user_name, other_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "DO you hate %s?" % other_name
hate = raw_input(prompt)

# 三个引号 """ 可以定义多行字符串，而 % 是字符串的格式化工具
print """
Alright, so you said %r about liking me.
You hate %r.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, hate, lives, computer)