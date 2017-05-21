#Filename: exercise40.py
#Author: Kyle Post
#Date: May 20, 2017
#Purpose: To practice learning about and using
#modules, classes, and objects.

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

new_line = "\n"
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there."])
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells!"])
know_my_name = Song(["Calm yourself because one else here can save you",
					"Love will betray you",
					"Are you ready to die?"])

happy_bday.sing_me_a_song()
print new_line
bulls_on_parade.sing_me_a_song()
print new_line
know_my_name.sing_me_a_song()