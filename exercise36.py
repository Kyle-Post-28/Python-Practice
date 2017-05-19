#Filename: exercise36.py
#Author: Kyle Post
#Date: May 18, 2017
#Purpose: To design game similar to the
#exercise 35 and practice all the different
#if and else statement, while and for loops
#functions, and branches

#I decided to make a game from my bartending
#experience. Enjoy!

from sys import exit

def vodka_vitality():
	print "You mix in some top-shelf vodka with the soda. The customer takes a swig."
	print "He says 'This is amazing' and he wants to tip you."
	print "He asks 'Do you have change for 20?'"
	customers_tip = False
	
	while True:
		change = raw_input("You say: ")
	
		if "no" in change:
			fired("You lied to a customer.")
		elif "check" in change and not customers_tip:
			print "You find enough money in the register, will you give him change?"
			customers_tip = True
		elif "check" in change and customers_tip:
			fired("The customer gets annoyed and leaves. You make no tip.")
		elif change == "yes" and customers_tip:
			print "'Excellent I just need one dollar back and the rest is yours' he says."
			print "You got a great tip, you win!"
			exit(0)
		else:
			print "That doesn't make sense"

def absinthe_adventure():
	print "You mix in some top-shelf absinthe with the soda. The customer takes a sip."
	print "The customer immediately gets drunk and runs away."
	print "Do you follow the customer or stay to take the next customer's order?"
	
	choice = raw_input("You choose: ")
	
	if choice == "follow":
		print "You follow the customer into the bathroom, in which your manager takes notice."
		print "The customer pukes in agony and points at you."
		fired("The customer says 'It's your fault', which your manager sees.")
	elif choice == "stay":
		begin()
	else:
		fired("You do nothing which means you aren't working.")

def fired(reason):
	print reason, "You're fired!"
	exit(0)

def begin():
	print "A customer approaches you with an empty cup."
	print "He asks if you could mix soda and some sort of alcohol together."
	print "Do you pick the bottle to the right or left?"
	
	choice = raw_input("You choose: ")
	
	if choice == "right":
		absinthe_adventure()
	elif choice == "left":
		vodka_vitality()
	else:
		fired("You didn't serve the customer and he complains to your manager.")
begin()