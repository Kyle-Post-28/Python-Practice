#Filename: exercise16.py
#Author: Kyle Post
#Date: May 13, 2017
#Purpose: To practice reading and writing
#files. This exercise will use test16.txt

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file...."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."
target.write("""%s\n%s\n%s\n""" % (line1, line2, line3))
#This commented stuff below was the original writing method
#of the program
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally we close it."
target.close()