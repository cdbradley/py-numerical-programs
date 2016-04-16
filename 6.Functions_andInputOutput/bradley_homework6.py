#Colt Bradley
#1.31.16
#Lesson 6 Homework

#import essential packages
import numpy as n
import bradley_functions as f

###############
#HW 1
#asks for a base, exponent, combines in user-defined functions
###############

#ask the user for input for each of these values
N = raw_input("Give me an integer as a base: ")
N = int(N)
r = raw_input("Give me an integer as an exponent: ")
r = int(r)

#Use functions and user arguments to answer
print f.power(f.factorial(N),r)

###############
#HW 2
#creates nxn dimension multiplication table and saves it
##############

#Interact with the user
print "We\'ll create a square multiplication table."
size = raw_input("What size should it be? ")
size = int(size)

#Create matrix placeholder
mat = n.zeros((size+1,size+1))
#Create list up to size
rng = range(0,size+1)

#Create "Titles" for the matrix
mat[0,0] = size

#fills in the interior of the matrix
#exterior will be lined by zeros, size will be in top right corner
for i in range(1,size+1):
    for j in range(1,size+1):
        mat[i,j] = rng[j]*rng[i]

n.savetxt("mult_table.txt",mat)

################
#HW 3
#ask for a fruit, write it to a list
###############

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