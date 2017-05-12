#Filename: exercise12.py
#Author: Kyle Post
#Date: May 11, 2017
#Purpose: To practice prompting users for input
#by essentially use the raw_input function with
#a prompt in the parenthesis

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So you are %r old, %r tall, and weigh about %r." % (
	age, height, weight)