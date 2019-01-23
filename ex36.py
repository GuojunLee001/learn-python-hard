#coding:utf-8

def God_job():
    print "It's the time to make a division."
	
    division = raw_input(" --> ")
    
    if division == "Beijing": 
        print "This is a good choice."
    elif division == "Chengdu":
        print "That's OK."
    else:
        print "I didn't know how to choose."

def Bad_job():
    print "You know what you can do?"

    while True:
        make_ch = raw_input("--> ")
        if make_ch == "Yes.":
            print "OK"
        elif make_ch == "NO.":
            find_job()
        else:
            print "Shut up!"

def find_job():
    print "You must choice how to work."
    print "It's very important."
    print "So let's make a choice."
	
    choice = raw_input("--> ")
    
    if choice == "Yes":
        God_job()
    elif choice == "No":
        Bad_job()
    else:
        print "Are you sure?!"
find_job()

# 总结
'''
设计程序的步骤：
1. 画出逻辑框架
2. 在源代码中先写注释，分为几个板块
3. 按照一定的逻辑先写
4. 写一部分运行一部分
5. 写完后运行检查确保能够运行
6. 优化逻辑，语句，报告程序简介优美。
'''
