#Filename: exercise30.py
#Author: Kyle Post
#Date: May 16, 2017
#Purpose: To learn else-if statements and
#continue working with if-statements and
#boolean expressions and variables.

#Create three variables with values
people = 30
cars = 40
buses = 15

#If this is tre then print
if cars > people:
	print "We should take the cars."
#If the first statement isn't true it will run this
#statement. If true then it will print.
elif cars < people:
	print "We should not take the cars."
#If neither statement before is true, it will just
#print this. 
else:
	print "We can't decide."
	
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."

#Add additional else-if statements
cars -=10
if people == cars and buses != people:
	print "Each person gets there own car, don't have to take the bus!"
else:
	print "Not enough cars for everyone, have to take the bus!" 