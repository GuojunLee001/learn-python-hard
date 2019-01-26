#coding:utf-8

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
hally_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parde = Song(["They rally around tha familly",
						"With pockets full of shells"])
						
hally_bday.sing_me_a_song()

bulls_on_parde.sing_me_a_song()