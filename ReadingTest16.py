#Filename: ReadingTest16.py
#Author: Kyle Post
#Date: May 13, 2017
#Purpose: To practice every to do with files
#based on exercise 16.

from sys import argv

script, filename = argv

answer = raw_input("Would you like to open %r? " % filename)

print "Opening %r..." % filename
target = open(filename, 'r+')

#print "\nLet's read the existing file first:"
#print target.read()

print "That was fun, now let's truncate it forever!!!"
target.truncate()

print"\nNow make some new lines for the file."
line1 = raw_input("First Line: ")
line2 = raw_input("Second Line: ")
line3 = raw_input("Third Line: ")

print "\nGood job! Time to write those lines to the file."
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
target.close()
print "We should read it one more time"
target_again = open(filename, 'r')
print target_again.read()

print "Goodbye, time to close up shop."

target_again.close()