#Filename: Combo13.py
#Author: Kyle Post
#Date: May 12, 2017
#Purpose: To practice modules and raw_input together
#This is part of exercise 13

#Import module from sys
from sys import argv
#Unpack argv and gets assigned to two variables
script, first = argv
#Create user input to combine with module
meat = raw_input("What is your favorite type of meat? ")
side_dish = raw_input("What is your favorite side dish? ")
#IMPORTANT: Created a first variable to replace whatever user types after script
first = raw_input ("For here or to go? ")

#Two print statements
print "So you would like to order a: %s and %s %s?" % (meat, side_dish, script)
print "To clarify you want: ", meat, "and", side_dish, script,"for", first,"?"