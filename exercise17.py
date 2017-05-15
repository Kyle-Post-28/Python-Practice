#Filename: exercise17.py
#Author: Kyle Post
#Date: May 13, 2017
#Purpose: To practice more reading and writing
#files by copying one file into another. Also,
#using the 'exists' function

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "\nDoes the output file exist? %r" % exists(to_file)
print "\n Ready...hit RETURN to continue or CTRL-C to abort."
raw_input()
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"
out_file.close()
in_file.close()
 