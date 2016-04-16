#Colt Bradley
#1.26.16
#Working through lesson 5

#import essential packages
import numpy as n

#exercise 1
color = raw_input("What's your favorite Color? ")

if color == "blue":
    print "That's my favorite color too!"
elif color == "red":
    print "Just like the NCSU wolfpack!"
elif color == "gray":
    print "That's actually kinda depressing"
elif color == "grey":
    print "Are you English?"
elif color == "black":
    print "Are you scandinavian?"
else:
    print "We don't have that color yet, but I'm sure it's a great choice!"
    
#Exercise 2
LastName = raw_input("What is your last name? ")
FirstName = raw_input("What is your first name? ")

if (LastName == "Simpson") and FirstName:
    print "I see you are part of the Siimpson Family"
    if FirstName[0] == 'M':
        if ('r' in FirstName):
            print 'you must be Marge'
        else:
            print 'You Must be Maggie'
    elif (FirstName[0] == 'H') or (FirstName[0] == 'B'):
        if not (FirstName[0] == 'B'):
            print "Hello Homer"
        else:
            print "Hello Bart"
    else:
        print "Hi Lisa"
else:
    print "You\'re not part of the Simpson Family"
    
#exercise 3
for i in range(1,20,1):
    if i < 5:
        continue
    elif i > 10:
        break
    print i

for i in range(1,20,1):
    if i < 5:
        pass
    elif i > 10:
        pass
    else: print i