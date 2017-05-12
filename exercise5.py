#Filename: exercise5.py
#Author: Kyle Post
#Date: May 10, 2017
#Purpose: To practice more variables, some printing
#methods and also learn about format characters.

#Create basic variables. Some as strings and others as integers
name = 'Kyle A. Post'
age = 26
height = 65 #inches
weight = 170 #lbs
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

#Create print statements to view all of the variables above
print "Let's talk about %s." % name
#Use %r to print a whole variable since %r represents a repr()
x = "He's %d inches tall." % height
print "%r" % x
#Practice python math by converting and round height to cm
convert_centi = round(height * 2.54, 2)
print "Now my height in centimeters is %.2f" % convert_centi,"cm."
#Practice conversions with weight variable from lbs to kilos
convert_weight = round(weight / 2.2, 2)

print "He's %d pounds heavy" % weight
print "Actually that isn't too heavy"
print "My weight in kilograms is %.2f" % convert_weight,"kilos."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)