#Filename: exercise29.py
#Author: Kyle Post
#Date: May 16, 2017
#Purpose: To learn and practice
#what if statements and tie it
#in with booleans from previous
#exercises

people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats: 
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry"
	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people == dogs:
	print "People are dogs."
	
#Add additional if-statements	
if cats != dogs:
	print "Cats are not dogs."
	
if cats == dogs:
	print "All cats are dogs."
	