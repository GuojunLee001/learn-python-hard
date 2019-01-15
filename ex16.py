# coding utf-8

# 参数包
from sys import argv
script, filename = argv 

# 打开文件夹名称
print "we're going to erase %r." % filename
# 定义是否创建
print "If you don't want that, hit CRRL-C (^C)."
print "If you do that, hit RETURN."
raw_input("?")

# 打开文件
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

# 定义输入的内容
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# 写入文档
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# 保存文档
print "And finally, we close it."
target.close()

# 加分题
