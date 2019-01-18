# coding:utf-8

people = 20
cats = 30
dogs = 15

if people < cats:
   print "To many cats! The world is doomed!"
   
if people > cats:
   print "Not many CATS! The world is saved!"
   
if people < dogs:
   print "The world is drooled on!"
   
if people > dogs:
   print "The world is dry!"
   
dogs += 5
if people >= dogs:
   print "People are greater than or equal to dogs."
   
if people <= dogs:
   print "People are less than or equal to dogs."
   
if people == dogs:
   print "People are dogs."
   
# 附件题
# If为判断语句，当满足条件时会输出，不满足条件时则不执行
# 如果不缩进，运行时会报错：indented block
# 如果把初始值改掉，输出结果会随着改变

people = 20
cats = 30
dogs = 15

if people < cats and people > dogs:
   print "What is people."
   
if people < cats and people < dogs:
   print "How many dogs and cats."
 
   
   
