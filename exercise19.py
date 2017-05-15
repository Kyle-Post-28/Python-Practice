#Filename: exercise19
#Author: Kyle Post
#Date: May 14, 2017
#Purpose: To practice with functions
#and variables

#Define the function cheese & crackers with two values/parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
#Set the values of the function to straight numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#Create two variables and set them as the values for the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Set the values to individual math problems
print "We can even do matho inside:"
cheese_and_crackers(10 + 20, 5 + 6)

#Set values to a combination of math with variables.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)