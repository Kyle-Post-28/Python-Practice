#Filename: exercise39.py
#Author: Kyle Post
#Date: May 20, 2017
#Purpose: To learn about, use, and practice
#with dictionaries aka hashes.

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detriot',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York City'
cities['OR'] = 'Portland'

line ='-' * 10
print line
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print line
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print line
for state, abbrev in states.items():
	print "%s abbreviated %s" % (state, abbrev)
	
print line
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
print line
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print line
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."
	
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is : %s" % city