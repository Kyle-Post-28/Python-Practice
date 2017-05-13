#Filename: exercise14.py
#Author: Kyle Post
#Date: May 12, 2017
#Purpose: Comtinue practicing using argv and raw_input
# with some simple prompts and intigrate them
# into output statements.

from sys import argv

script, user_name, code_name = argv
#Prompt was originally '> '
prompt = '(*) '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "\nDo you like me %s?" % user_name
likes = raw_input(prompt)

print "\nWhere do you live %s?" % user_name
lives = raw_input(prompt)

print "\nWhat kind of computer do you have?"
computer = raw_input(prompt)

print """\n
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

print """\n
But after everything %s...you would
rather be called %r, instead of your
real name. You make no sense.
""" % (user_name, code_name)

