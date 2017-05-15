#Filename: FuncPrac19.py
#Author: Kyle Post
#Date: May 14, 2017
#Purpose: Expand off of exercise19.py
#and create my own function. For this
#I decided to create a function based off
#my bartending days. So this function is 
#for stocking the bar before an event.

def alcohol(liquor, beer):
	print "I have %r bottles of alcohol!" % liquor
	print "I also have %r cans of beer!" % beer
	print "This is a big event and people will go crazy!\n"
	
liquor = int(raw_input("How many bottles of alcohol did are there? "))
beer = int(raw_input("How many beers is that? "))
alcohol(liquor, beer)

print "My employer brought even more stuff, so now"
alcohol(liquor + 5, beer + 42)

print "The guest brought stuff too."
alcohol(28, 130)

print "The host of the event is starting to complain saying"
complaint1 = "too many"
complaint2 = "not enough"

alcohol(complaint1, complaint2)
