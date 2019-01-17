# coding: utf-8

# 最基本输出
print "Let's practice everything."
# 转义字符使用 \'单引号、\\反斜杠、\n 换行、\t横向制表符
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# """ 使用
poem = """
\tThe lonely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\ttwhere there is none # 先换行，在横向制表（在里面的这行被打印出来了！）
"""

# 必须用""，表示文本
print "--------------"
print poem
print "--------------"

# 变量赋值
five = 10 - 2 + 3 -6 
# 用% 打印
print "This should be five: %s" % five

# 函数
def secret_formula(started):
    jelly_beans = started * 500  # 下面三行在变量中赋值
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates   # 返回函数

# 定义具体的函数值	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# 二次赋值
start_point = start_point / 10

print "We can also do that way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# 修改表达方式
start_point = 10000
secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# 二次赋值
start_point = start_point / 10

print "We can also do that way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
