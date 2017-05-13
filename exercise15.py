#Filename: exercise15.py
#Author: Kyle Post
#Date: May 12, 2017
#Purpose: To practice reading files and
#have the user input what file needs to
#be read.

#Import argv module
from sys import argv
#Unpack argv and assign it to two variables
script, filename = argv
#txt variable uses the open function of the filename
txt = open(filename)
#Print statement to make sure filename is correct
print "Here's your file %r:" % filename
#use the variable function of read with no parameters.
print txt.read()
#Have the user input the name of the file instead
#of using a script
print "\nType the filename again:"
file_again = raw_input("> ")
#open the file set it to equal to another variable
txt_again = open(file_again)
#Use the "read" variable function again and
#print results.
print txt_again.read()
#Try the "readlines" function
print txt_again.readlines(2)
#close files
txt.close()
txt_again.close()
#By running this line, programs confirms closes
print "The %r has been closed" % filename



