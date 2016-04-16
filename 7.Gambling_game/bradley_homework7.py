#Colt Bradley
#2.2.16
#Homework 7

#import random
import random as r

#Interact with the user, explain what is going on. 
print "Welcome to the Casino! We've a special on the martingale"
print "betting system, want to play? I see you have $20, buy in"
print "is $2."

ans = " "
#Determine starting values for the variables
while ans != ("n" or "N" or "no" or "No" or "y" or "Y" or "yes" or "Yes"):
    ans = raw_input("Would you like to use default values? Bet = $2, Goal = $40 (Y or N): ")
    if ans == ("n" or "N" or "no" or "No"):
        goal = raw_input("How much money would you like to win? ")
        goal = int(goal)
        bet1 = raw_input("What do you want as your starting bet? ($2 min, $20 max) ")
        bet1 = int(bet1)
    elif ans == ("y" or "Y" or "yes" or "Yes"):
        goal = 40
        bet1 = 2
        break
    else:
        print "What? It's a simple yes or no question!"
    

#define vars
money = 20
bet = bet1
it = 0

#while loop to simulate betting. 
while (0 < money < goal): 
    rand = r.randint(1,38)
    #this section defines the 0 and 00 numbers
    if rand == 37:
        rand = 0
    elif rand == 38:
        rand = 39 #We'll change this to 00 later 
    else:
        if rand%2 == 0: #this case is if the number is even
            money = money + bet
            rand = str(rand)
            print "Your bet is {}".format(bet)
            print "ball lands on {}".format(rand)
            print "you win {}, you have {} dollars".format(bet,money)
            print
            bet = bet1
            it = it+1 
        elif rand%2 ==1: #This is the cas tha tthe number is odd
            money = money - bet
            if rand == 39:
                rand = "00"
            else:
                rand = str(rand)
            it = it+1
            print "Your bet is {}".format(bet)
            print "ball lands on {}".format(rand)
            print "you lose {}, you have {} dollars".format(bet,money)
            print
            bet = 2*bet
 
#when money is outside of selected values, we get results as follows  
if money <= 0:
        print "You've lost everything after {} tries!".format(it)
        print "What will you tell the kids?"
else:
    print "Congrats! It took you {} tries, but now you have {} dollars!".format(it,money)