# _*_ coding: utf-8 _*_

# 调用一个打开文件的包
from sys import argv

script, input_file = argv

# 定义读文件函数
def print_all(f):
    print f.read()

# 定义寻找函数	
def rewind(f):
    f.seek(0)

# 定义两个变量
def print_a_line(line_count, f):
    print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

# 打开文件，第一个定义的函数
print_all(current_file)

# 打开第二个定义的函数，打开三行文件
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines."

# 打开第一行
current_line = 1
print_a_line(current_line, current_file)

# 打开文件第二行
current_line = current_line + 1
print_a_line(current_line, current_file)

# 打开文件第三行
current_line = current_line + 1
print_a_line(current_line, current_file)

# 加分题 += 相当于w = w + 1
# 再打开一遍
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines."

# 打开第一行
current_line = 1
print_a_line(current_line, current_file)

# 打开文件第二行
current_line += current_line
print_a_line(current_line, current_file)

# 打开文件第三行
current_line += current_line
print_a_line(current_line, current_file)