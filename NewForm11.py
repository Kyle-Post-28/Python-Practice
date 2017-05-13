#Filename: NewForm11.py
#Author: Kyle Post
#Date: May 11, 2017
#Purpose: To create my own form and practice
#raw inputs and displaying them in strings
#Goes with exercise 11
		
#Create my own form using raw_input functions
print "What is your favorite video game?",
game = raw_input()
print "If you could see only in one color what would it be?",
eye_color = raw_input()
print "Name one food you can't live without",
food = raw_input()

print "So you like playing %r, you only want to see %r, and eat %r." % (
game, eye_color, food)

print "So you like playing %s, you only want to see %s, and eat %s." % (
game, eye_color, food) 
