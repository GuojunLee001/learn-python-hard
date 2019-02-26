#!/usr/bin/env python
#coding:utf-8

# 标准库sys
import sys

print "The file name: ", sys.argv[0] # 第一个参数
print "The number of argument", len(sys.argv)
print "The argument is: ", str(sys.argv)

# sys.exit
for i in range(10):
    if i == 10:
        sys.exit("this programe is over")
    else:
        print i
        
# urllib 使用
import urllib

itdiffer = urllib.urlopen("https://www.yangzhiping.com/")

print itdiffer.read()

