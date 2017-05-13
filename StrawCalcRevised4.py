#Filename:StrawCalcRevised.py
#Author: Kyle Post
#Date: May 10, 2017
#Purpose: I teach after school architecture classes
#to elementary school kids. One project was they had
#to construct geodesic domes out of straws. Each side
#of the dome is a hexagon with a total of 14 sides to
#complete the dome. Each side is constructed out of 
#triangles, 3 straws per triangle
#Goes with exercise 4

#This program is based off the previous version
#except this time we are going to use variables
#to express equations and call during print statements

#Create print statements to briefly explain word problem again.
print "This geodesic dome will have 14 sides."
print "Each side is a hexagon made up of 6 triangles."

#Create print statement to ask the first question
print "If 3 straw make one triangle, how many straws are needed for the whole project?"

#First create variable "straws" to calculate the number of straws in a side
straws = 3 * 6
print "There are", straws, "straws needed per side."

#Next create variable "total straws", then call variable straws and multiply it by 14
total_straws = straws * 14
print "To complete this whole project you need", total_straws, "straws."

#Now formulate a different question
print "How many triangles are needed for the whole dome?"

#Explain the solution
print "Well there are 6 triangles per side and 14 sides total therefore,"
#Declare string variable of total triangles equation and total triangles answer
total_triangles_equation = "6 x 14"
total_triangles = 6 * 14
print "The equation needed is", total_triangles_equation, "which equals", total_triangles, "triangles."

#Last question
print "How many triangles are in half of the dome?"
#Declare string variable of total triangles equation and total triangles answer
half_triangles_equation = "6 x 7"
half_triangles = 6 * 7
#print solution
print "The equation needed is", half_triangles_equation, "which equals", half_triangles, "triangles."
