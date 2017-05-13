#Filename: exercise13.py
#Author: Kyle Post
#Date: May 12, 2017
#Purpose: To practice creating a script
#that runs arguments. Also, will practice
#importing modules

#Import the argv module from sys
from sys import argv

#Assign argv to four variables
script, first, second, third = argv

#Create print statements
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#When running the file add "first, second and third arguments
#to the filename being run.
#Example: python exercise13.py huckle berry fin
