#Colt Bradley
#1.31.16
#part 2 of the homework

#import numpy
import numpy as n

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
print n.loadtxt("mult_table.txt")