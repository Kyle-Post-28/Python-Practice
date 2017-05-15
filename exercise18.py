#Filename: exercise18.py
#Author: Kyle Post
#Date: May 14, 2017
#Purpose: To practice using and creating functions
#based off similar strategies used in previous
#exercises.

def print_two(*args):
    arg1, arg2 = args
	print "arg1: %r\narg2: %r" % (arg1, arg2)
	
def print_two_again(arg1, arg2):
	print "arg1: %r\narg2: %r" % (arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothin'."
	
print_two("Kyle", "Post")
print_two_again("Gabriel", "O'Connell")
print_one("One")
print_none()