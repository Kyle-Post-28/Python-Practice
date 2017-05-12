#Filename: exercise4.py
#Author: Kyle Post
#Date: May 10, 2017
#Purpose: To practice variables and names

#Declare the variable cars and that there are 100 of them
cars = 100
#Declare the variable space in a car. 4.0 is a floating number
space_in_a_car = 4.0
#Declare the variable of drivers
drivers = 30
#Declare the variable of passengers
passengers = 90
#Declare cars not driven which is calculated by call variables "car" and "drivers"
cars_not_driven = cars - drivers
#Declare cars_driven as equal to drivers
cars_driven = drivers
#Declare variable carpool capacity with an equation of two other variables
carpool_capacity = cars_driven * space_in_a_car
#Declare avg passengers per car with the variables of "passengers" and "cars_driven"
average_passengers_per_car = passengers / cars_driven

#Create print statements and call variables to each statement
print "There are", cars, "cars avaiable."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."