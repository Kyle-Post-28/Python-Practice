#Filename: exercise28.py
#Author: Kyle Post
#Date: May 16, 2017
#Purpose: To practice with Boolean expressions.
#I am going to comment my guesses before
#running the program.

answer1 = True and True
print "1: ", answer1 #True

answer2 = False and True
print "2: ", answer2 #False

answer3 = 1 == 1 and 2 == 1
print "3: ", answer3 #False

answer4 = "test" == "test"
print "4: ", answer4 #True

answer5 = 1 == 1 or 2 != 1
print "5: ", answer5 #True

answer6 = True and 1 == 1
print "6: ", answer6 #True

answer7 = False and 0 != 0
print "7: ", answer7 #False

answer8 = True or 1 == 1
print "8: ", answer8 #True

answer9 = "test" == "testing"
print "9: ", answer9 #False

answer10 = 1 != 0 and 2 == 1
print "10: ", answer10 #False

answer11 = "test" != "testing"
print "11: ", answer11 #True

answer12 = "test" == 1
print "12: ", answer12 #False

answer13 = not (True and False)
print "13: ", answer13 #True

answer14 = not (1 == 1 and 0 != 1)
print "14: ", answer14 #False

answer15 = not (10 == 1 or 1000 == 1000)
print "15: ", answer15 #False

answer16 = not (1 != 10 or 3 == 4)
print "16: ", answer16 #False

answer17 = not ("testing" == "testing" and "Zed" == "Cool Guy")
print "17: ", answer17 #True

answer18 = 1 == 1 and not ("testing" == 1 or 1 == 0)
print "18: ", answer18 #True

answer19 = "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print "19: ", answer19 #False

answer20 = 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
print "20: ", answer20 #False