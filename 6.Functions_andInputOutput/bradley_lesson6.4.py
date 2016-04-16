#Colt Bradley
#1.31.16
#Working on HW part 3

#import packages
import numpy as n

#open fruit file
fruits = open("new_fruits.txt","w")
fruits1 = open("fruits.txt","r")

#ask user for a fruit
user_fruit = raw_input("Enter a fruit: ")

#write the old and new fruits to the new file
string = fruits1.read()
fruits.write(string)
fruits.write(user_fruit)
fruits.close()
fruits1.close()

#open new fruits file and save a string
fruitss = open("new_fruits.txt","r")
string = fruitss.read()
    
#print necessary information
print "My favorite fruits are..."
print string