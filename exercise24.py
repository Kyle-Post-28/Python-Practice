#FIlename: exercise24.py
#Author: Kyle Post
#Date: May 15, 2017
#Purpose: To practice more with functions
# and the return statement and reviewing 
#the last couple of exercises

print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do\n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------------"
print poem
print "-------------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	cups = crates / 5
	return jelly_beans, jars, crates, cups

start_point = 10000
beans, jars, crates, solo = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates, and %d cups." % (beans, jars, crates, solo)

start_point = start_point / 2

print "We can also do that this way:"
print "We'd have %d beans, %d jars, %d crates, and %d cups." % secret_formula(start_point)