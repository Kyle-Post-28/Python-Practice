#Filename: exercise26.py
#Author: Kyle Post
#Date: May 15, 2017
#Purpose: To fix an entire python file
#created by Zed Shaw. Find and fix all 
#errors.

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#This was missing a colon after the function
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #This was missing a second parenthesis
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#Used a dash instead of an underscore for start_point
#Also, used double equals instead of just one
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#Missing an end parenthesis 
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont)


sentence = "All god\tthings come to those who weight."

words = exercise25.break_words(sentence)
sorted_words = exercise25.sort_words(words)

print_first_word(words)
print_last_word(words)
#This had an extra period in the beginning
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = exercise25.sort_sentence(sentence)
#This was missing a "t" for print and an underscore after print
print_sorted_words
#This was missing an "f" for first
print_first_and_last(sentence)
#This was indented improperly and forgot the word "and"
print_first_and_last_sorted(senence)

#In this file I found a total of 9 errors
