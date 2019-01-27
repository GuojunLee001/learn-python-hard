#coding:utf-8

class Song(object):

	def __init__(self, lyrics):  #创建歌曲类别
		self.lyrics = lyrics
		
	def sing_me_a_song(self):    # 创建循环结构
		for line in self.lyrics:
			print line
			
hally_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parde = Song(["They rally around tha familly",
						"With pockets full of shells"])
# 类别的输出，用a.AA()形式		
hally_bday.sing_me_a_song() 

bulls_on_parde.sing_me_a_song()

# 附件题
class Person(object):
	def __init__(self, name):
		self.name = name 
	
	def getName(self):
		return self.name
		
	def breast(self, n):
		self.breast = n 
		
	def color(self, color):
		print "%s is %s" % (self.name, color)
		
	def how(self):
		print "%s breast is %s" %(self.name, self.breast)
		
girl = Person('canglaoshi')
girl.breast(90)

girl.color("white")
girl.how()