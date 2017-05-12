#Filename: exercise6.py
#Author: Kyle Post
#Date: May 11, 2017
#Purpose: To practice strings, quotes, and format characters

#Create a few string variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#Create a string variable with two string variables in it
y = "Those who know %s and those who %s." % (binary, do_not)

#Print both string statements
print x
print y

#Use different format characters in print statements
#Notice that the %r will print the entire "raw" data
print "I said: %r." % x
print "I also said: '%s'." % y

#Set a variable to a boolean
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Intigrating two variables and using the %r to print
#the boolean of the variable hilarious
print joke_evaluation % hilarious

#Create two variables that will be later combined
w = "This is the left side of "
e = "a string with a right side."

#Print statement with a simple addition of variables
print w + e