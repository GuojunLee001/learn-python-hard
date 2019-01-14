# _*_ coding: utf-8 _*_

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# 此处使用''' 和“”“结果一样
fat_cat = """
I'll do a list:
\t* Cat food
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


# 加分题
# （1）使用''' 和“”“结果一样
# （2）
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,	
