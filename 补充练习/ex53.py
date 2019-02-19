#coding:utf-8

def add_function(a, b): # 定义函数类型及变量个数
    c = a + b           # 定义函数关系
    print c             # 定义输出的内容
    

def add(x, y):
    return x + y
    
# 给变量赋值
add_function(2, 3)
add(3, 7)
add(x = 3, y = 7)
add(x = y =3, y=7)

# 注意：少使用全局变量、代码尽可能简短运行高效
