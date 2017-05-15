#Filename: exercise20.py
#Author: Kyle Post
#Date: May 14, 2017
#Purpose: To practice using functions and files
#together, based off past exercises

#Import argv module from system
from sys import argv
#Assign two variables to argv
script, input_file = argv

#Create a print all function that prints the whole file
def print_all(f):
	print f.read()

#Create a rewind function that uses the seek function
#to go back to the start of the text
def rewind(f):
	f.seek(0)

#Create a print line function that will print
#the line number and that line in the file	
def print_a_line(line_count, f):
	print line_count, f.readline()

#Set variable to the opened input_file
current_file = open(input_file)

#Call the print all function
print "First let's print the whole file:\n"
print_all(current_file)

#Call the rewind function
print "Now let's rewind, kind of like a tape.\n"
rewind(current_file)

#Call the print each line function
print "Let's print three lines: "
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
