#Filename: exercise33.py
#Author: Kyle Post
#Date: May 16, 2017
#Purpose: To practice while-loops and
#then put it into a function and using
#function arguments for the while-loop


numbers = []

def all_nums(i, limit, increase):
	while i < limit:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + increase
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	print "The numbers: "
	for num in numbers:
			print num
		
all_nums(0, 10, 3)