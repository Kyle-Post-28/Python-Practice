#Filename: exercise8.py
#Author: Kyle Post
#Date: May 11, 2017
#Purpose: Practice printing and using formatter variable

#Create a formatter variable using representation
#format character
formatter = "%r %r %r %r"

#Create print statements to test formatter
#Use integers
print formatter % (1, 2, 3, 4)
#Use strings
print formatter % ("one", "two", "three", "four")
#Use booleans
print formatter % (True, False, False, True)
#Use the formatter variable itself
print formatter % (formatter, formatter, formatter, formatter)
#Use longer strings
print formatter % (
		"I hade this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight"
		)