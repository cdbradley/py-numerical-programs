#Colt Bradley
#1.19.16
#Working through lesson 4

import numpy as n

#Create array begins at 2, writes 5 elements in equal intervals to 4
x = n.linspace(2,4,5)
print x
#replace element 4
x[3]=17.
print x

#create a new list
w = n.arange(6,15,1)
print w[3:6]
print w[:5]
print w[5:]

#playing with variables
x=n.linspace(1,5,5)
y=x
print y
x[1] = 7
print y